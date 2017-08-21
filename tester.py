import speech_recognition as sr
import time
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source,duration=1) # Kan bruges til at tjekke noise værdien
    r.energy_threshold = 2000 # er den value der bruges til at filtrere lyden.
    # En værdi mellem 1500+ er mest optimalt, men brug ovenstående funktion til at tjekke
    print("say something " + str(r.__getattribute__("energy_threshold")))
    audio = r.listen(source)
print("audio done")
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    speech = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + speech)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

time.sleep(1)

speak.Speak(speech)
