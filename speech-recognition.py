#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:42:27 2020

@author: harshvardhansingh
"""

import speech_recognition as sr
import webbrowser as wb

#from gtts import gTTS
#import os
#
#videoText = "Search for Videos"
#googleText = "Search on Google"
#language = 'en'
#
#videoSearch = gTTS(videoText, language)
#videoSearch.save("video.mp3")
#os.system("mpg321 video.mp3")
#
#googleSearch = gTTS(googleText, lang=language)
#googleSearch.save("google.mp3")

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search google : search youtube]')
    print('speak now')
    
    
    audio = r3.listen(source)

if 'video' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
#        os.system("mpg321 video.mp3")
        print('Search for videos')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            print(get)
            
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.Request_Error as e:
            print('failed'.format(e))
            
if 'Google' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
#        os.system("mpg321 google.mp3")
        print('Search on Google')
        audio = r1.listen(source)
        
        try:
            get = r1.recognize_google(audio)
            print(get)
            
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.Request_Error as e:
            print('failed'.format(e))