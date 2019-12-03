#!/usr/bin/env python
# coding: utf-8

# In[2]:


import speech_recognition as sr
import subprocess

r = sr.Recognizer()
mic = sr.Microphone()

# check the possible values

# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# raws = r.recognize_google(audio,language='ko-KR',show_all=True)
# raws

# possible values list

WORDS1 = ['하상집','화상 집','화상집','가상 집','사상 집','상집','하상식','하상 집','화장실']
WORDS2 = ['김준표','김중표','음표']
WORDS3 = ['차의성','자위성','자 위성','자위 성','차 위성','차이성']
WORDS4 = ['현광수','변광수','형광 수','형 광수','전광수']
WORDS5 = ['박서윤','박소윤']
WORDS6 = ['이유경','이우경','유경','이효경','이윤경']
WORDS7 = ['김하은','임하은']

WORDS = [WORDS1,WORDS2,WORDS3,WORDS4,WORDS5,WORDS6,WORDS7]

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
raw = r.recognize_google(audio,language='ko-KR')

for i in WORDS:
    if raw in i:
        print(i[0])

