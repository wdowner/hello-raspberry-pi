# Time Lapse Photography
# Ryan Heitz
# Take a photo at a set interval

import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    # Start taking pictures repeatedly
    for filename in camera.capture_continuous('image{counter:04d}.jpg'):
        print('Captured %s' % filename)
        # wait 3 minutes
        time.sleep(180) 
