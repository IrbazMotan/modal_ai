{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOs/TpZF3uXV+o0lzjcT+rt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IrbazMotan/modal_ai/blob/main/modal2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 1: Install required libraries\n",
        "!pip install google-cloud-texttospeech moviepy transformers streamlit\n",
        "!apt-get install -y libsndfile1  # Required for moviepy\n",
        "\n",
        "# Step 2: Upload your Google Cloud credentials\n",
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()  # This will prompt you to upload the credentials.json file\n",
        "\n",
        "# Step 3: Set the environment variable for Google Cloud credentials\n",
        "import os\n",
        "\n",
        "# Replace 'credentials.json' with the name of your uploaded file if different\n",
        "os.environ[\"GOOGLE_APPLICATION_CREDENTIALS\"] = \"credentials.json\"\n",
        "\n",
        "# Step 4: Import necessary libraries\n",
        "import streamlit as st\n",
        "from google.cloud import texttospeech\n",
        "from moviepy.editor import TextClip, CompositeVideoClip\n",
        "from transformers import pipeline\n",
        "import tempfile\n",
        "\n",
        "# Function to generate text using Hugging Face's GPT-2 model\n",
        "def generate_script(input_text):\n",
        "    \"\"\"Generates a script using a pre-trained NLP model.\"\"\"\n",
        "    model = pipeline(\"text-generation\", model=\"gpt2\")\n",
        "    script = model(input_text, max_length=500, num_beams=4)\n",
        "    return script[0][\"generated_text\"]\n",
        "\n",
        "# Function to create a video from the generated script\n",
        "def create_video(script):\n",
        "    \"\"\"Creates a video from the script text.\"\"\"\n",
        "    with tempfile.NamedTemporaryFile(delete=False, suffix=\".mp4\") as temp_video_file:\n",
        "        video_clips = []\n",
        "        for scene in script.split(\"\\n\"):\n",
        "            # Creating text clip for each scene\n",
        "            text_clip = TextClip(scene, font=\"Arial\", fontsize=30, color=\"white\", size=(1280, 720))\n",
        "            text_clip = text_clip.set_duration(5)  # Set each clip's duration to 5 seconds\n",
        "            video_clips.append(text_clip)\n",
        "\n",
        "        # Combine video clips into one\n",
        "        final_clip = CompositeVideoClip(video_clips)\n",
        "        final_clip.write_videofile(temp_video_file.name, codec=\"libx264\")\n",
        "\n",
        "    return temp_video_file.name  # Return the video file path\n",
        "\n",
        "# Function to convert text to speech using Google Cloud Text-to-Speech\n",
        "def text_to_speech(text):\n",
        "    \"\"\"Converts text to speech using Google Cloud Text-to-Speech.\"\"\"\n",
        "    client = texttospeech.TextToSpeechClient()\n",
        "    synthesis_input = texttospeech.SynthesisInput(text=text)\n",
        "    voice = texttospeech.VoiceSelectionParams(\n",
        "        name=\"en-US-Standard-C\", language_code=\"en-US\"\n",
        "    )\n",
        "    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)\n",
        "\n",
        "    with tempfile.NamedTemporaryFile(delete=False, suffix=\".mp3\") as temp_audio_file:\n",
        "        response = client.synthesize_speech(\n",
        "            input=synthesis_input, voice=voice, audio_config=audio_config\n",
        "        )\n",
        "        temp_audio_file.write(response.audio_content)\n",
        "\n",
        "    return temp_audio_file.name  # Return the audio file path\n",
        "\n",
        "# Step 5: Define the Streamlit app interface\n",
        "def main():\n",
        "    st.title(\"Text-to-Video with Script Generation\")\n",
        "\n",
        "    # User Input\n",
        "    user_text = st.text_input(\"Enter text for script generation:\")\n",
        "\n",
        "    if user_text:\n",
        "        # Generate a script based on user input\n",
        "        script = generate_script(user_text)\n",
        "        st.write(\"Generated Script:\")\n",
        "        st.write(script)\n",
        "\n",
        "        # Create video from generated script\n",
        "        st.write(\"Generating Video...\")\n",
        "        video_file_path = create_video(script)\n",
        "        st.video(video_file_path)  # Display the video in Streamlit\n",
        "\n",
        "        # Generate and download audio from script (optional)\n",
        "        if st.button(\"Generate Audio\"):\n",
        "            audio_file_path = text_to_speech(script)\n",
        "            st.write(\"Audio Generated!\")\n",
        "            st.audio(audio_file_path)\n",
        "\n",
        "# Step 6: Run the Streamlit app\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "id": "VTRoZeYwcXx9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run your_script_name.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "id": "Y98e2uF5c0Di"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}