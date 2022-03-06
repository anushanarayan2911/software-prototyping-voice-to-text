import speech_recognition as sr

class Model:

    def getSpeech(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
        
        try:
            speech = r.recognize_google(audio_text)
            return speech
        except:
            print("Sorry, I did not get that")

        