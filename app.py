import speech_recognition as sr
from google.cloud import speech, texttospeech
import openai
from huggingface_hub import pipeline
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def speech_to_text(audio_file):
    """Converts speech to text using Google Cloud Speech-to-Text."""
    client = speech.SpeechClient()
    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(   

        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,   

        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript   


def generate_script(text):
    """Generates a script using a pre-trained NLP model."""
    model = pipeline("text-generation", model="gpt2")
    script = model(text, max_length=500, num_beams=4)
    return script[0]["generated_text"]

def create_video(script, audio_file=None):
    """Creates a video from the script."""
    # Create video clips for each scene or dialogue
    video_clips = []
    for scene in script.split("\n"):
        text_clip = TextClip(scene, font="Arial", fontsize=30, color="white")
        video_clips.append(text_clip)
    # Combine video clips and add background music
    final_clip = CompositeVideoClip(video_clips, size=(1280, 720))
    final_clip = final_clip.set_duration(10)  # Adjust duration as needed
    # Add background music (optional)
    if audio_file:
        background_music = VideoFileClip(audio_file)
        final_clip = final_clip.set_audio(background_music.audio)
    # Save the video
    final_clip.write_videofile("output.mp4")

def text_to_speech(text):
    """Converts text to speech using Google Cloud Text-to-Speech."""
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(   

        name="en-US-Standard-C",
        language_code="en-US",
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )
    response = client.synthesize_speech(
        input=synthesis_input,   
 voice=voice, audio_config=audio_config
    )
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)   
def main(audio_file):
    text = speech_to_text(audio_file)
    script = generate_script(text)
    create_video(script)
    text_to_speech(script)
    if __name__ == "__main__":
    audio_file = "your_audio_file.wav"
    main(audio_file)
