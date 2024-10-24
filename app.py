import whisper

# Load pre-trained Whisper model
model = whisper.load_model("base")

# Transcribe audio file to text
result = model.transcribe("path_to_audio_file.wav")

# Print the transcription
print(result["text"])

