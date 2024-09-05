from gpiozero import OutputDevice
from time import sleep

RELAY_PIN = 17  
SOLENOID_PIN = 18  


relay = OutputDevice(RELAY_PIN)
solenoid = OutputDevice(SOLENOID_PIN)

try:
    while True:
        relay.on()
        sleep(2)  

        solenoid.on()
        sleep(2)  

        solenoid.off()
        sleep(2)  

        relay.off()
        sleep(2) 

except KeyboardInterrupt:
    relay.off()
    solenoid.off()
