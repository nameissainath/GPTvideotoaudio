import streamlit as st
import cv2  # Required for video processing
import base64
import tempfile
from openai import OpenAI
import os
import requests

# Function to encode video frames
@st.cache
def encode_video_frames(video_file):
    """
    Encodes video frames to base64.
    Processes the video file and converts each frame into a base64 encoded string.
    """
    encoded_frames = []
    video_bytes = video_file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_bytes)
        temp_filename = temp_file.name

    cap = cv2.VideoCapture(temp_filename)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        encoded_frames.append(base64.b64encode(buffer).decode("utf-8"))
    cap.release()
    os.remove(temp_filename)
    return encoded_frames

# Streamlit UI setup
st.title("🎙️ AI-Powered Voiceover Creation from Videos 🎬")
st.markdown("🔍 Explore the magic of OpenAI's Vision and TTS models to transform your videos into captivating narrations! 🌟")

# Define session state for storing video frames, scripts, and the OpenAI API key
if "video_frames" not in st.session_state:
    st.session_state.video_frames = []
if "generated_script" not in st.session_state:
    st.session_state.generated_script = ""
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

# UI for OpenAI API key input
st.session_state.openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Proceed only if the API key is entered
if st.session_state.openai_api_key:
    openai_client = OpenAI(api_key=st.session_state.openai_api_key)

    video_upload = st.file_uploader("Choose a Video File", type=["mp4"])
    if video_upload:
        st.video(video_upload)

    if video_upload and st.session_state.openai_api_key:
        if st.button("Process Video"):
            with st.spinner("Processing..."):
                st.session_state.video_frames = encode_video_frames(video_upload)
                st.success(f"Processed {len(st.session_state.video_frames)} frames.")
            st.image(base64.b64decode(st.session_state.video_frames[0].encode("utf-8")), caption="Sample Frame")

    if st.session_state.video_frames and st.button("Create Script"):
        script_prompt = [
            {
                "role": "user",
                "content": [
                    "This video showcases a cooking show. Create a narration script that is engaging and descriptive of the cooking process.",
                    *map(
                        lambda frame: {"image": frame, "resize": 768},
                        st.session_state.video_frames[0::50]
                    ),
                ],
            },
        ]
        with st.spinner("Crafting the script..."):
            script_response = ""
            script_display = st.empty()
            for response in openai_client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=script_prompt,
                max_tokens=500,
                stream=True,
            ):
                if response.choices[0].delta.content:
                    script_response += response.choices[0].delta.content
                    script_display.markdown(script_response + "▌")
            st.session_state.generated_script = script_response

    if st.session_state.generated_script and st.button("Produce Audio"):
        with st.spinner("Generating narration..."):
            audio_resp = requests.post(
                "https://api.openai.com/v1/audio/speech",
                headers={"Authorization": f"Bearer {st.session_state.openai_api_key}"},
                json={"model": "tts-1", "input": st.session_state.generated_script, "voice": "fable"},
            )
            if audio_resp.status_code == 200:
                audio_content = audio_resp.content
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_file:
                    audio_file.write(audio_content)
                    audio_file.seek(0)
                    st.audio(audio_file.name, format="audio/mp3")
                    audio_file.seek(0)
                    st.download_button("Download Narration", audio_file.read(), "narration.mp3", "audio/mp3")
                os.unlink(audio_file.name)  # Cleanup temp file
else:
    st.warning("Please enter your OpenAI API Key to proceed.")
