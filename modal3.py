import streamlit as st
from google.cloud import texttospeech
import tempfile

from google.colab import files
uploaded = files.upload()  # Upload 'credentials.json'
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"


# Function to convert text to speech using Google Cloud Text-to-Speech
def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Standard-C"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Create a temporary file for the audio output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        temp_audio_file.write(response.audio_content)

    return temp_audio_file.name  # Return the temporary audio file path

# Streamlit App Interface
def main():
    st.title("Text-to-Speech with Google Cloud")

    # Config (if needed)
    config = {
        "include_colab_link": True  # Correct boolean syntax
    }

    # Input for the user to enter text
    user_text = st.text_input("Enter text to convert to speech:")

    # If the user provides text, convert it to speech
    if user_text:
        audio_file = text_to_speech(user_text)
        st.write("Audio Generated Successfully!")
        st.audio(audio_file)  # Play the generated audio in Streamlit

# Run the Streamlit App
if __name__ == "__main__":
    main()
