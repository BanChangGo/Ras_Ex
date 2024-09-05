import gpiod
import time


chip = gpiod.Chip('gpiochip0') 
line = chip.get_line(17)  

config = gpiod.line_request()
config.consumer = 'button-monitor'
config.request_type = gpiod.line_request.DIRECTION_INPUT
config.flags = gpiod.line_request.FLAG_BIAS_PULL_UP 


line.request(config)

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
