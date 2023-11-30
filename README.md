# AI-Powered Voiceover Creation from Videos 🎬

## Overview

"AI-Powered Voiceover Creation from Videos" is a Streamlit application that leverages OpenAI's advanced GPT-4 and Text-to-Speech models. This tool enables users to upload videos, extract frames, and generate voiceover scripts that are then converted into audio narrations. It's particularly useful for content creators, educators, and marketers who want to create engaging narrations for their videos.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your computer. If you don’t have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository**:
   - Get a copy of the source code on your local machine by cloning the repository:
     ```
     git clone <repository-url>
     ```

2. **Create a Virtual Environment**:
   - Navigate to the cloned directory and create a Python virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**:
   - Install the required libraries using pip:
     ```
     pip install -r requirements.txt
     ```

4. **Set Up OpenAI API Key**:
   - Obtain an API key from [OpenAI](https://beta.openai.com/signup/).
   - When running the application, you will be prompted to enter this API key in the Streamlit UI.

### Running the Application

- Start the application by running:

Replace `your_script_name.py` with the name of your Python script.

## How to Use

1. **Enter API Key**: Input your OpenAI API key in the provided text input field.
2. **Upload Video**: Use the file uploader to choose and upload your video file (MP4 format recommended).
3. **Process Video**: Click the "Process Video" button to extract frames from the video.
4. **Generate Script**: After processing, click "Create Script" to generate a voiceover script based on the video frames.
5. **Produce Audio**: Click "Produce Audio" to convert the script into an audio file.
6. **Download**: You can listen to the generated audio directly in the app and download it in MP3 format.

## Contributing

Your contributions are always welcome! If you have any improvements or suggestions, feel free to fork the repository and submit a pull request.



## Acknowledgments

- Thanks to OpenAI for providing the GPT-4 and Text-to-Speech models.
- Streamlit for their incredible framework that simplifies the creation of web applications.

## Contact

Feel free to contact me for any questions or feedback regarding this project.
