from yeelight import *
import random
import cv2
import datetime
import time

bulb = [Bulb('192.168.1.102'), Bulb('192.168.1.101')]
camera = cv2.VideoCapture(0)


while True :
    time.sleep(random.randint(3, 10))
    for b in bulb:
        b.turn_on()
    time.sleep(1)
    return_value, image = camera.read()
    cv2.imwrite('capture-yeelight/opencv'+str(time.time())+'.png', image)
    time.sleep(random.randint(3, 10))
    for b in bulb:
        b.set_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        b.turn_off()