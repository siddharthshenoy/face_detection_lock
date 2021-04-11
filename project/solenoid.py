import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(2.5)                    
try:
    while 1:                    # Loop will run forever
        p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
        sleep(1)                # Delay of 1 sec
        p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
        sleep(1)                
        p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
        sleep(1)
        
        
# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
    pass   # Go to next line
GPIO.cleanup()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''i = input("sex me tonight")

if i==1:
    servo1.start(0)
    servo1.ChangeDutyCycle(7)
    sleep(2)
    GPIO.output(11, 0)
else:
    servo1.start(0)
    servo1.ChangeDutyCycle(2)
    sleep(2)
    GPIO.output(11, 0)

#except KeyboardInterrupt:
servo1.stop()
GPIO.cleanup()'''