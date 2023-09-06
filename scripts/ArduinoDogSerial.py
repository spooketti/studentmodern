import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("credent.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://arduinodoglure-default-rtdb.firebaseio.com/"
})
from firebase_admin import db
from serial import Serial
called = False
incri = 0
#ser = Serial('COM3',9600) 

"""
if ser.isOpen():
	while(True):
		input_data=ser.readline().strip().decode("utf-8")
		input_data = int(input_data)
		
"""


def listener(message):
    global called
    if not called:
        called = True
        return
    incri+=1
    Serial.write(incri)
   

my_stream = db.reference("main/event").listen(listener)

