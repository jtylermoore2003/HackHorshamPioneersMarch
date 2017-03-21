from gpiozero import OutputDevice, MotionSensor
from time import sleep

pir = MotionSensor(4)

popped = 0 
balloon = OutputDevice(2)
buzzer = OutputDevice(15)


while popped == 0:
    if pir.motion_detected:
        print("You moved")
        balloon.on()
        buzzer.on()
        sleep(5)
        balloon.off()
        buzzer.off()
        print("Pop!")
        popped = 1
