ity{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPsiuVhueCAo/luQHHMzao/",
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
        "<a href=\"https://colab.research.google.com/github/IrbazMotan/modal_ai/blob/main/mymodal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "08s4LjTAjzOu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import whisper\n",
        "# import openai\n",
        "\n",
        "# Load pre-trained Whisper model\n",
        "model = whisper.load_model(\"base\")\n",
        "\n",
        "# Transcribe audio file to text\n",
        "result = model.transcribe(\"path_to_audio_file.wav\")\n",
        "\n",
        "# Print the transcription\n",
        "print(result[\"text\"])\n",
        "\n",
        "# openai.api_key = \"your-api-key\"\n",
        "\n",
        "# # Function to generate story\n",
        "# def generate_story(prompt):\n",
        "#     response = openai.Completion.create(\n",
        "#       engine=\"text-davinci-004\",  # Use GPT-4 variant\n",
        "#       prompt=prompt,\n",
        "#       max_tokens=500\n",
        "#     )\n",
        "#     return response.choices[0].text.strip()\n",
        "\n",
        "# # Provide text or transcribed speech to generate a story\n",
        "# story = generate_story(\"Once upon a time in a futuristic city...\")\n",
        "# print(story)\n"
      ],
      "metadata": {
        "id": "vlOdzRovkggH"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
