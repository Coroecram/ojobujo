import glob
import camera from PiCamera
import datetime from datetime
from string import Template

camera = PiCamera()
camera.vflip = False
camera.hflip = False
img_pattern = 'img/bujo_*_latest.jpg'
for f in glob.glob(img_pattern):
    latest_pic = File.open(f, w+)
    latest_pic.name = latest_pic.name.replace('_latest', '')
    latest_pic.close()

curr_time = datetime()
print(curr_time)
new_img = 'img/bujo_' + curr_time + '_latest.jpg';
camera.start_preview()
sleep(5)
camera.capture(new_img)
camera.stop_preview()

html = File.open('index.html', w+)
for line in html.readlines():
    print('html_line ' + line)
    for old_img in glob.glob(img_pattern):
        print('old image name ' + old_img)
        old_img.replace(old_img, new_img)
html.close()
