# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
import streamlit as st
from google.cloud import speech, texttospeech
print(google.cloud.__version__)
from huggingface_hub import pipeline
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from transformers import pipeline

# Text from pre-processed audio (replace with your actual text)
text = "This is the transcribed text from your audio file."  # Modify this

# Hugging Face equivalent (optional):
nlp = pipeline("text-generation", model="gpt2")
generated_text = nlp(
    prompt="Write a poem about a robot who dreams of becoming a human.",
    max_length=100,
    num_beams=4,
)

def generate_script(input_text):
    """Generates a script using a pre-trained NLP model."""
    model = pipeline("text-generation", model="gpt2")
    script = model(input_text, max_length=500, num_beams=4)
    return script[0]["generated_text"]

def create_video(script, audio_file=None):
    """Creates a video from the script."""
    # Create video clips for each scene or dialogue
    video_clips = []
    for scene in script.split("\n"):
        text_clip = TextClip(scene, font="Arial", fontsize=30, color="white")
        video_clips.append(text_clip)

    # Combine video clips and add background music (optional)
    final_clip = CompositeVideoClip(video_clips, size=(1280, 720))
    final_clip = final_clip.set_duration(10)  # Adjust duration as needed

    # Add background music (optional)
    if audio_file:
        background_music = VideoFileClip(audio_file)
        final_clip = final_clip.set_audio(background_music.audio)

    # Save the video (consider temporary file for Streamlit)
    final_clip.write_videofile("output.mp4")

def text_to_speech(text):
    """Converts text to speech using Google Cloud Text-to-Speech."""
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        name="en-US-Standard-C", language_code="en-US"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)


# Streamlit App
st.title("Text-to-Video with Script Generation")

# User Input (consider audio upload from previous session)
user_text = st.text_input("Enter text or provide previous audio transcript")

if user_text:
    # Generate script
    script = generate_script(user_text)

    # Generate video
    create_video(script)

    # Text-to-Speech (optional)
    text_to_speech(script)

    # Display results in Streamlit
    st.write("Generated Script:")
    st.write(script)

    st.write("Generated Video:")
    st.video("output.mp4")  # Consider temporary video handling
def exec_func_with_error_handling(func):
    try:
        result = func()
    except Exception as e:
        # Handle the exception gracefully
        print(f"Error executing function: {e}")
        # You can add more specific error handling here, such as logging or raising a custom exception
    return result
    # Optional: Download links for video and audio (securely)
    # ...

# st.markdown(
    # """**Note:** This is a simplified
