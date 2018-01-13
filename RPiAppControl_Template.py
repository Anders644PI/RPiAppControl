# Import Libraries
import pyrebase

# Firebase Configuration
config = {
  "apiKey": "apiKey", #----- Change to customize! -----
  "authDomain": "[YOUR PROJECT ID].firebaseapp.com", #----- Change to customize! -----
  "databaseURL": "[YOUR PROJECT ID].firebaseio.com", #----- Change to customize! -----
  "storageBucket": "[YOUR PROJECT ID].appspot.com" #----- Change to customize! -----
}

firebase = pyrebase.initialize_app(config)

# Firebase Database Intialization
db = firebase.database()

# While loop
while(True):
    # Getting num(number) from Firebase
    num1 = db.child("num1").get()
    num2 = db.child("num2").get()

    # Sorts through children of num(number)
    for user in num1.each():
        # Check value of child(which is 'state')
        if(user.val() == "ON"):
            print("Button 1 is: ON") #----- Change to customize! -----
        else:
            print("Button 1 is: OFF") #----- Change to customize! -----

    # Sorts through children of num(number)
    for user in num2.each():
        # Check value of child(which is 'state')
        if(user.val() == "ON"):
            print("Button 2 is: ON") #----- Change to customize! -----
        else:
            print("Button 2 is: OFF") #----- Change to customize! -----