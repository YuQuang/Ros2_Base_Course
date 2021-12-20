#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS

fromLanguage = "zh-TW"
toLanguage = "en"
 
try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        
        sttTXT_org = r.recognize_google(audio, language = fromLanguage)
        print("Google Speech Recognition thinks you said:" + sttTXT_org)
        
        sttTXT_tblob = TextBlob(sttTXT_org)
        
        blobTranslated = sttTXT_tblob.translate(to=toLanguage)
        print("Translated -- " + blobTranslated.raw)
        
        tts = gTTS(blobTranslated.raw + ".", lang=toLanguage)
        tts.save("tts.mp3")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))