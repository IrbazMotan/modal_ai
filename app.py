{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyPMGjqZqrbnBOnesfjjyjDt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IrbazMotan/modal_ai/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Title of the app\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# Function to add two numbers\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "# Function to subtract two numbers\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "# Function to multiply two numbers\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "# Function to divide two numbers\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Error! Division by zero.\"\n",
        "\n",
        "# User input for selecting the operation\n",
        "operation = st.selectbox(\"Select Operation\", (\"Add\", \"Subtract\", \"Multiply\", \"Divide\"))\n",
        "\n",
        "# Input for numbers\n",
        "num1 = st.number_input(\"Enter first number\", value=0.0, format=\"%f\")\n",
        "num2 = st.number_input(\"Enter second number\", value=0.0, format=\"%f\")\n",
        "\n",
        "# Perform the selected operation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "        st.write(f\"Result: {num1} + {num2} = {result}\")\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "        st.write(f\"Result: {num1} - {num2} = {result}\")\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "        st.write(f\"Result: {num1} * {num2} = {result}\")\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "        st.write(f\"Result: {num1} / {num2} = {result}\")\n"
      ],
      "metadata": {
        "id": "94_yD5iCE2t_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8mqT0BDlhQYc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "jE6WNVD4hCDG"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}