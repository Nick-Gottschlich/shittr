import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play
import time

flush_noise = AudioSegment.from_wav("toilet.wav")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Flushed yo shit')
        time.sleep(2)
