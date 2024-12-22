import speech_recognition
import pyttsx3
from os import system
from daniwled import *
import requests


f = open("token.txt", "r")
token = f.read()
url = "https://ha.kopaszhegy:8443/api/conversation/process"
headers = {
    "Authorization": "Bearer "+token,
}




PREFIXUM = "hey"
PREFIXUM = PREFIXUM.lower()
LEVEL_2_PREFIXUM = "hey computer"
LEVEL_2_PREFIXUM = LEVEL_2_PREFIXUM.lower

kiadott_parancsok = []

def main():
    # TTS motor inicializálása
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[35].id)

    recognizer = speech_recognition.Recognizer()
    while True:
        
        try:
            
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=2)
                print("Beszélj...")
                audio = recognizer.listen(mic,phrase_time_limit=10)
                
            # Alapértelmezett Google Speech API használata
            text = recognizer.recognize_google(audio, language="en-EN")
            text = text.lower()
            system("clear")
            print("======================")
            print(f"Felismerve: {text}")
            print("======================")
            kiadott_parancsok.append(text)
            response = requests.request("POST", url, headers=headers, verify=False, data='{"text": "'+text+'","language": "hu"}')
            if PREFIXUM not in text:
                print(f"Nem használtad a '{PREFIXUM}' prefixumot")
            else:
                
                if text == f"{PREFIXUM} turn off the light":
                    wled_off()
                    engine.say("A fények kikapcsolva.")
                    engine.runAndWait()
                elif text == f"{PREFIXUM} turn on the lamp":
                    response = requests.request("POST", url, headers=headers, verify=False, data='{"text": Kapcsold fel a lámpát a dani szobában,"language": "hu"}')
                elif text == f"{PREFIXUM} turn off the lamp":
                    response = requests.request("POST", url, headers=headers, verify=False, data='{"text": Kapcsold le a lámpát a dani szobában,"language": "hu"}')
                elif text == f"{PREFIXUM} turn off the effect":
                    wled_off()
                    engine.say("A fények effekt módból kikapcsolva.")
                    engine.runAndWait()
                elif text == f"{PREFIXUM} turn on the light":
                    wled_on(255)
                    engine.say("A fények bekapcsolva.")
                    engine.runAndWait()
                elif text == f"{PREFIXUM} turn on the effect":
                    wled_aurora(255)
                    engine.say("A fények effekt módba kapcsolva.")
                    engine.runAndWait()
                elif text == f"{PREFIXUM} turn on the night effect":
                    wled_aurora(10)
                    engine.say("Az éjszakai effekt bekapcsolva.")
                    engine.runAndWait()
                elif text == f"{PREFIXUM} turn off the effect":
                    wled_on(255)
                    engine.say("A fények effekt módból kikapcsolva.")
                    engine.runAndWait()
                elif text == f"{LEVEL_2_PREFIXUM} stop":
                    print("A program sikeresen leállt")
                    txt_szoveg = open("beszed.txt", "w")
                    txt_szoveg.write(f"Kiadott parancsok: {kiadott_parancsok}\n")
                    engine.say("A program sikeresen leállt")
                    engine.runAndWait()
                    break
                elif text == f"{PREFIXUM} clear the data":
                    engine.say("Az adatok törölve.")
                    engine.runAndWait()
                    kiadott_parancsok.clear()
                elif text == f"{PREFIXUM} save the data":
                    engine.say("Az adatok elmentve.")
                    engine.runAndWait()
                    txt_szoveg = open("beszed.txt", "w")
                    txt_szoveg.write(f"Kiadott parancsok: {kiadott_parancsok}\n")
                else:
                    print("=====================\n=====================\n    Nem felismerhető a parancs    \n=====================\n=====================")
            
                
        except speech_recognition.UnknownValueError:
            print("Nem érthető, kérlek ismételd meg!")
            continue
        except Exception as e:
            print(f"Hiba történt: {e}")
            break
        except KeyboardInterrupt:
            print("A program leállt")
            txt_szoveg = open("beszed.txt", "w")
            txt_szoveg.write(f"Kiadott parancsok: {kiadott_parancsok}\n")
            break

if __name__ == "__main__":
    main()
