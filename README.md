# -Conversational-Voice-Assistant-using-Python-Ollama

 📌 Project Overview

This project is a voice-based conversational assistant built using Python.
The assistant listens to the user’s voice, converts it into text, sends the conversation to a local AI model (Ollama), receives a response, and then speaks the response back to the user.

The assistant supports continuous conversation and remembers the context during a session.


 🎯 Objective of the Project

The main objectives of this project are:

* To understand speech-to-text (STT) and text-to-speech (TTS)
* To integrate local AI models (Ollama)
* To build a real-time conversational system
* To practice Python modules, functions, loops, and subprocess handling
* To create a hands-free AI assistant

 🛠️ Technologies & Libraries Used

# 🔹 Programming Language

* Python

# 🔹 Libraries

* `sounddevice` → Captures microphone audio
* `speech_recognition` → Converts speech to text
* `pyttsx3` → Converts text to speech (offline)
* `subprocess` → Communicates with Ollama AI model

# 🔹 AI Model

* Ollama (llama3) – Local Large Language Model (LLM)


 ⚙️ System Requirements

* Python 3.x
* Ollama installed and running
* Microphone and speaker
* Internet (only for Google speech recognition)


 🧩 Explanation of Code Components


# 🔹 1. Text-to-Speech Setup

```python
tts = pyttsx3.init()
tts.setProperty("rate", 170)
```

Initializes the text-to-speech engine and sets the speaking speed.

# 🔹 2. `listen_and_transcribe()` Function

Purpose:
Captures voice input and converts it into text.

Working:

* Records audio using the microphone
* Converts audio into text using Google Speech Recognition
* Returns recognized text
* Handles errors if speech is unclear



# 🔹 3. `ask_ollama(conversation)` Function

Purpose:
Sends the conversation history to the Ollama AI model and gets a response.

Working:

* Uses `subprocess.run()` to execute the Ollama command
* Passes full conversation as input
* Receives AI-generated text output



# 🔹 4. `speak(text)` Function

Purpose:
Converts AI-generated text into speech.

Working:

* Prints the response
* Uses `pyttsx3` to speak the response aloud



# 🔹 5. Conversation History

```python
conversation_history = ""
```

Stores the entire conversation to maintain context, allowing the assistant to respond meaningfully in multi-turn conversations.


# 🔹 6. `main()` Function

Purpose:
Controls the overall flow of the voice assistant.

Features:

* Starts the conversational assistant
* Continuously listens for user input
* Supports exit commands (`exit`, `stop`, `quit`)
* Maintains conversation history
* Calls AI and TTS functions


 🔁 Program Flow

```
User speaks
   ↓
Speech-to-Text conversion
   ↓
Conversation history updated
   ↓
Ollama AI generates response
   ↓
Text-to-Speech output
   ↓
Loop continues
```

 🧪 Sample Interaction

```
🎤 Speak now...
You: hello
🤖 Assistant: Hello! How can I help you today?

🎤 Speak now...
You: what is python
🤖 Assistant: Python is a high-level programming language...

🎤 Speak now...
You: exit
🤖 Assistant: Goodbye! Have a nice day.
```

 ✅ Key Features

* Voice-based interaction
* Continuous conversational chat
* Context-aware responses
* Offline AI processing (Ollama)
* No API key required
* Hands-free operation

 ⚠️ Limitations

* Conversation history is temporary (lost after exit)
* Speech recognition depends on microphone quality
* Only one AI model supported at a time
* No GUI (command-line based)

 🚀 Future Enhancements

* Permanent memory using files or database
* Wake word detection (e.g., “Hey Assistant”)
* GUI interface
* Multiple language support
* Faster AI models

 📝 Conclusion

This project demonstrates how Python can be used to build a real-time conversational voice assistant by integrating speech processing and local AI models.
It is ideal for students learning full stack development, AI integration, and system-level programming.


