import pyttsx3

print(help(pyttsx3))

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 100)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("All systems are functional.")

print("Available voices: ")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} - {voice.id}")