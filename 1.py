import gpiod
import time


chip = gpiod.Chip('gpiochip0')  
line = chip.get_line(17)  


line.request(consumer='button-monitor', type=gpiod.LINE_REQ_DIR_IN, flags=[gpiod.LINE_REQ_FLAG_BIAS_PULL_UP])

try:
    while True:
        
        button_state = line.get_value()
        
        if button_state == 0: 
            print("Button Pressed!")
        else:
            print("Button Released!")
        
        time.sleep(0.1) 

except KeyboardInterrupt:
    
    print("Exiting...")

finally:
    line.release() 
