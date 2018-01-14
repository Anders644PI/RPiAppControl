# Import Libraries
import pyrebase

# Firebase Configuration
config = {
  "apiKey": "[your_apiKey]", #----- Change to customize! -----
  "authDomain": "[your_project_id].firebaseapp.com", #----- Change to customize! -----
  "databaseURL": "https://[your_project_id].firebaseio.com", #----- Change to customize! -----
  "storageBucket": "[your_project_id].appspot.com" #----- Change to customize! -----
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
