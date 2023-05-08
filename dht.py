import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D27,use_pulseio=False)


while True:
    try:
        temp_c=dhtDevice.temperature
        humidity=dhtDevice.humidity
        print("Temperature: {} C  humidity:{}%" .format(temp_c,humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2)



#blinking LED
import RPi.GPIO as GPIO
import sleep

GPIO.setmode(BCM)
GPIO.setup(7,GPIO,OUT)
GPIO.setup(8,GPIO,OUT)
GPIO.setup(9,GPIO,OUT)
GPIO.setup(10,GPIO,OUT)

while True:
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    time.sleep(1)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(9,GPIO.LOW)
    
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    time.sleep(1)