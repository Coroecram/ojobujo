import glob
from picamera import PiCamera
import os
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip = True
camera.hflip = False

curr_time = int(time.time())
print(curr_time)
new_img = 'img/bujo_' + str(curr_time) + '.jpg';
latest_img = 'img/bujo_' + 'latest.jpg';
camera.start_preview()
time.sleep(5)
camera.capture(new_img)
camera.capture(latest_img)
camera.stop_preview()
