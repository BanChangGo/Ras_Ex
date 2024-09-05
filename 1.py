import RPi.GPIO as GPIO  
import time 


BUTTON_PIN = 17


GPIO.setmode(GPIO.BCM)  
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

try:
    while True:
        
        button_state = GPIO.input(BUTTON_PIN)
        
        if button_state == GPIO.LOW: 
            print("Button Pressed!")
        else:
            print("Button Released!")
        
        time.sleep(0.1) 

except KeyboardInterrupt:
   
    print("Exiting...")

finally:
    GPIO.cleanup()  
