import googletrans
from googletrans import Translator

import RPi.GPIO as GPIO

pIn = 3
pOut = 5
GPIO.setmode(GPIO.BCM) #pin numbering declaration
GPIO.setup(pIn, GPIO.IN) #input
GPIO.setup(pOut, GPIO.OUT) #output

pwm = GPIO.PWM(pIn, 50) #50 is frequency, need to change this later

input = GPIO.input(pIn)
print(input)

print(googletrans.LANGUAGES)
translator = Translator()
word = translator.translate(input, dest= 'en')

print(word.text) 