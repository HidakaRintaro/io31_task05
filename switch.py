import RPi.GPIO as GPIO
import time

SWPIN = 17
LEDPIN1 = 27
LEDPIN2 = 22

SWINPUT = 1
BEFORE = 1
MOMFLG = False
ALTFLG = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # プルアップ抵抗は常時1、ボタン押下時0
GPIO.setup(LEDPIN1, GPIO.OUT)
GPIO.setup(LEDPIN2, GPIO.OUT)

# def alternate(self):
#     output = not GPIO.input(LEDPIN2)
#     GPIO.output(LEDPIN2, output)
    
# オルタネート
# 立ち上がりエッジ(LOW→HIGH)のときにalternateを実行し300ミリ秒待ってから次のイベントを呼ぶ
# GPIO.add_event_detect(SWPIN, GPIO.RISING, callback=alternate, bouncetime=300)
CNT = 0
try:
    while True:
        SWINPUT = GPIO.input(SWPIN)
        MOMFLG = not SWINPUT

        # オルタネート処理
        if SWINPUT == 0 and BEFORE == 1:
            ALTFLG = not ALTFLG
        
        # 1つ前の入力状態を保持する
        BEFORE = SWINPUT
        
        # モーメンタリ出力
        GPIO.output(LEDPIN1, MOMFLG)
        
        # オルタネート出力
        GPIO.output(LEDPIN2, ALTFLG)
        
except KeyboardInterrupt:
    pass

GPIO.remove_event_detect(SWPIN)
GPIO.cleanup()
