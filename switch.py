import RPi.GPIO as GPIO
import time

SWPIN = 17
LEDPIN1 = 27
LEDPIN2 = 22
SWINPUT = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # プルアップ抵抗は常時1、ボタン押下時0
GPIO.setup(LEDPIN1, GPIO.OUT)
GPIO.setup(LEDPIN2, GPIO.OUT)

def alternate(self):
    output = not GPIO.input(LEDPIN2)
    GPIO.output(LEDPIN2, output)
    
# オルタネート
# 立ち上がりエッジ(LOW→HIGH)のときにalternateを実行し300ミリ秒待ってから次のイベントを呼ぶ
GPIO.add_event_detect(SWPIN, GPIO.RISING, callback=alternate, bouncetime=300)

try:
    while True:
        SWINPUT = GPIO.input(SWPIN)
        # モーメンタリ
        if SWINPUT == 0:
            GPIO.output(LEDPIN1, GPIO.HIGH)
        else:
            GPIO.output(LEDPIN1, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.remove_event_detect(SWPIN)
GPIO.cleanup()
