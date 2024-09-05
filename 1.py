from gpiozero import OutputDevice
from time import sleep


solenoid = OutputDevice(12)

try:
    while True:
        
        solenoid.on()
        print("솔레노이드 켜짐")
        sleep(1) 
        
       
        solenoid.off()
        print("솔레노이드 꺼짐")
        sleep(1) 
        
except KeyboardInterrupt:

    solenoid.off()
    print("프로그램 종료")
