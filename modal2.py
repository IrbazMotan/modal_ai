import streamlit as st
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip
from transformers import pipeline
import tempfile

# Flag or setting to include Colab link
include_colab_link = True  # Boolean flag

# Function to generate text using Hugging Face's GPT-2 model
def generate_script(input_text):
    """Generates a script using a pre-trained NLP model."""
    model = pipeline("text-generation", model="gpt2")
    script = model(input_text, max_length=500, num_beams=4)
    return script[0]["generated_text"]

# Function to create a video from the generated script
def create_video(script):
    """Creates a video from the script text."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
        video_clips = []
        for scene in script.split("\n"):
            # Creating text clip for each scene
            text_clip = TextClip(scene, font="Arial", fontsize=30, color="white", size=(1280, 720))
            text_clip = text_clip.set_duration(5)  # Set each clip's duration to 5 seconds
            video_clips.append(text_clip)

        # Combine video clips into one
        final_clip = CompositeVideoClip(video_clips)
        final_clip.write_videofile(temp_video_file.name, codec="libx264")
    
    return temp_video_file.name  # Return the video file path

# Function to convert text to speech using Google Cloud Text-to-Speech
def text_to_speech(text):
    """Converts text to speech using Google Cloud Text-to-Speech."""
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        name="en-US-Standard-C", language_code="en-US"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        temp_audio_file.write(response.audio_content)

    return temp_audio_file.name  # Return the audio file path

# Streamlit App Interface
def main():
    st.title("Text-to-Video with Script Generation")

    # User Input
    user_text = st.text_input("Enter text for script generation:")

    if user_text:
        # Generate a script based on user input
        script = generate_script(user_text)
        st.write("Generated Script:")
        st.write(script)

        # Create video from generated script
        st.write("Generating Video...")
        video_file_path = create_video(script)
        st.video(video_file_path)  # Display the video in Streamlit

        # Generate and download audio from script (optional)
        if st.button("Generate Audio"):
            audio_file_path = text_to_speech(script)
            st.write("Audio Generated!")
            st.audio(audio_file_path)

    # If the Colab link flag is True, include the link in the Streamlit app
    if include_colab_link:
        st.markdown("[Open in Colab](https://colab.research.google.com)", unsafe_allow_html=True)

# Run the Streamlit App
if __name__ == "__main__":
    main()
