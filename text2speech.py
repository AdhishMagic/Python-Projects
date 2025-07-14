import pyttsx3

data = input("Enter the text you want to convert to speech: ")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech(data)
