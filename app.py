import whisper
import openai

# Load pre-trained Whisper model
model = whisper.load_model("base")

# Transcribe audio file to text
result = model.transcribe("path_to_audio_file.wav")

# Print the transcription
print(result["text"])

# import openai

# Your OpenAI API key here
openai.api_key = "your-api-key"

# Function to generate story
def generate_story(prompt):
    response = openai.Completion.create(
      engine="text-davinci-004",  # Use GPT-4 variant
      prompt=prompt,
      max_tokens=500
    )
    return response.choices[0].text.strip()

# Provide text or transcribed speech to generate a story
story = generate_story("Once upon a time in a futuristic city...")
print(story)
