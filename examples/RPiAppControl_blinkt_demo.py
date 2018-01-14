# Import Libraries
import time
import random
import pyrebase
import blinkt
import colorsys

blinkt.set_clear_on_exit()

# Firebase Configuration
config = {
  "apiKey": "[your_apiKey]",
  "authDomain": "[your_project_id].firebaseapp.com",
  "databaseURL": "[your_project_id].firebaseio.com",
  "storageBucket": "[your_project_id].appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Firebase Database Intialization
db = firebase.database()

# Script on start
def start_run():
    for x in range(4):
        for i in range(8):
            blinkt.clear()
            blinkt.set_pixel(i, 255, 0, 0)
            blinkt.show()
            time.sleep(0.05)
    blinkt.clear()
    blinkt.show()

# While loop
while(True):
    # Running start script, so we now it's ready
    start_run()
    while (True):
        # Getting num(number) from Firebase
        num1 = db.child("num1").get()
        num2 = db.child("num2").get()
        num3 = db.child("num3").get()
        num4 = db.child("num4").get()
        num5 = db.child("num5").get()

        # Sorts through children of num(number)
        for user in num1.each():
            # Check value of child(which is 'state')
            if(user.val() == "ON"):
                # Blinkt sets all colors // Change this to customize!
                blinkt.set_all(128, 0, 0)
                blinkt.set_brightness(0.1)
                blinkt.show()
                time.sleep(0.3)
                blinkt.set_brightness(0.8)
                blinkt.show()
                time.sleep(0.3)
            else:
                blinkt.clear()
                blinkt.show()
                #time.sleep(0.1)

        # Sorts through children of num(number)
        for user in num2.each():
            # Check value of child(which is 'state')
            if(user.val() == "ON"):
                # Blinkt sets all colors // Change this to customize!
                blinkt.set_all(0, 128, 0)
                blinkt.set_brightness(0.1)
                blinkt.show()
                time.sleep(0.3)
                blinkt.set_brightness(0.8)
                blinkt.show()
                time.sleep(0.3)
            else:
                blinkt.clear()
                blinkt.show()
                #time.sleep(0.1)

        # Sorts through children of num(number)
        for user in num3.each():
            # Check value of child(which is 'state')
            if(user.val() == "ON"):
                # Blinkt sets all colors // Change this to customize!
                blinkt.set_all(0, 0, 128)
                blinkt.set_brightness(0.1)
                blinkt.show()
                time.sleep(0.3)
                blinkt.set_brightness(0.8)
                blinkt.show()
                time.sleep(0.3)
            else:
                blinkt.clear()
                blinkt.show()
                #time.sleep(0.1)

        # Sorts through children of num(number)
        for user in num4.each():
            # Check value of child(which is 'state')
            if(user.val() == "ON"):
                # Blinkt sets all colors // Change this to customize!
                blinkt.set_all(128, 128, 128)
                blinkt.set_brightness(0.1)
                blinkt.show()
                time.sleep(0.3)
                blinkt.set_brightness(0.8)
                blinkt.show()
                time.sleep(0.3)
            else:
                blinkt.clear()
                blinkt.show()
                #time.sleep(0.1)

        # Sorts through children of num(number)
        for user in num5.each():
            spacing = 360.0 / 16.0
            hue = 0
            # Check value of child(which is 'state')
            if(user.val() == "ON"):
                # Blinkt makes 'rainbows' // Change this to customize!
                for z in range(8):
                    hue = int(time.time() * 100) % 360
                    for x in range(blinkt.NUM_PIXELS):
                        offset = x * spacing
                        h = ((hue + offset) % 360) / 360.0
                        r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
                        blinkt.set_pixel(x, r, g, b)
                    blinkt.show()
            else:
                blinkt.clear()
                blinkt.show()
                #time.sleep(0.1)
