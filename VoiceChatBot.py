from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import speech_recognition as sr
import pyttsx3

bot= ChatBot('Bot')
bot.set_trainer(ListTrainer)

r= sr.Recognizer()
source= sr.Microphone()

try:
    engine= pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initilize')

voices= engine.getProperty('voices')
for voice in voices:
    print(voice.id)

engine.setProperty('voice',
                   'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

for files in os.listdir(r'C:\Users\sharwil\Downloads\Prerequisite\chatterbot-corpus-master\chatterbot_corpus\data\english'):
    data= open('C:/Users/sharwil/Downloads/Prerequisite/chatterbot-corpus-master/chatterbot_corpus/data/english/'+ files, 'r').readlines()
    bot.train(data)

while True:
    with sr.Microphone() as source:
        print('say something')
        audio = r.listen(source)
        print(audio)
        message= r.recognize_google(audio)
        print(message)
    if message.strip() != 'Bye':
        reply = bot.get_response(message)

    engine.say(reply)
    engine.runAndWait()
    if message.strip() == 'Bye':
        engine.say('Bye')
        engine.runAndWait()
    break
