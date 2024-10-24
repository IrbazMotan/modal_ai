{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoFBeXNe0nmku406S3WjG8",
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
        "<a href=\"https://colab.research.google.com/github/IrbazMotan/modal_ai/blob/main/modal3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install google-cloud-texttospeech streamlit moviepy localtunnel()\n"
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
        "from google.colab import files\n",
        "uploaded = files.upload()  # This prompts you to upload 'credentials.json'\n"
      ],
      "metadata": {
        "id": "Y98e2uF5c0Di"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.environ[\"GOOGLE_APPLICATION_CREDENTIALS\"] = \"credentials.json\"  # Replace with your file name if it's different\n"
      ],
      "metadata": {
        "id": "daIISn7Ze3xX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from google.cloud import texttospeech\n",
        "import tempfile\n",
        "\n",
        "# Function to convert text to speech using Google Cloud Text-to-Speech\n",
        "def text_to_speech(text):\n",
        "    client = texttospeech.TextToSpeechClient()\n",
        "    synthesis_input = texttospeech.SynthesisInput(text=text)\n",
        "    voice = texttospeech.VoiceSelectionParams(\n",
        "        language_code=\"en-US\", name=\"en-US-Standard-C\"\n",
        "    )\n",
        "    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)\n",
        "\n",
        "    # Create a temporary file for the audio output\n",
        "    with tempfile.NamedTemporaryFile(delete=False, suffix=\".mp3\") as temp_audio_file:\n",
        "        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)\n",
        "        temp_audio_file.write(response.audio_content)\n",
        "\n",
        "    return temp_audio_file.name  # Return the temporary audio file path\n",
        "\n",
        "# Streamlit App Interface\n",
        "def main():\n",
        "    st.title(\"Text-to-Speech with Google Cloud\")\n",
        "\n",
        "    # Input for the user to enter text\n",
        "    user_text = st.text_input(\"Enter text to convert to speech:\")\n",
        "\n",
        "    # If the user provides text, convert it to speech\n",
        "    if user_text:\n",
        "        audio_file = text_to_speech(user_text)\n",
        "        st.write(\"Audio Generated Successfully!\")\n",
        "        st.audio(audio_file)  # Play the generated audio in Streamlit\n",
        "\n",
        "# Run the Streamlit App\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "id": "5ALrdErfe8j3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}