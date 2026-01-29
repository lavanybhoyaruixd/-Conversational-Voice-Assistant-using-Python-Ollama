import subprocess
import sounddevice as sd
import speech_recognition as sr
import pyttsx3

# ---------- TTS SETUP ----------
tts = pyttsx3.init()
tts.setProperty("rate", 170)

# ---------- SPEECH TO TEXT ----------
def listen_and_transcribe():
    recognizer = sr.Recognizer()
    fs = 16000
    duration = 5

    print("\n🎤 Speak now...")
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    audio = sr.AudioData(recording.tobytes(), fs, 2)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text 
    except sr.UnknownValueError:
        print("❌ Could not understand")
        return None

# ---------- OLLAMA CHAT ----------
def ask_ollama(conversation):
    """
    conversation = full chat history as string
    """
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=conversation,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# ---------- SPEAK ----------
def speak(text):
    print("🤖 Assistant:", text)
    tts.say(text)
    tts.runAndWait()

# ---------- MAIN CHAT LOOP ----------
def main():
    print("🟢 Conversational Voice Assistant Started")
    print("Say 'exit' or 'stop' to quit.\n")

    conversation_history = ""

    while True:
        user_text = listen_and_transcribe()
        if not user_text:
            continue

        if user_text.lower() in ["exit", "stop", "quit"]:
            speak("Goodbye! Have a nice day.")
            break

        # Add user message to history
        conversation_history += f"\nUser: {user_text}\nAssistant:"

        # Get response from Ollama
        ai_response = ask_ollama(conversation_history)

        # Add assistant response to history
        conversation_history += f" {ai_response}\n"

        speak(ai_response)

if __name__ == "__main__":
    main()