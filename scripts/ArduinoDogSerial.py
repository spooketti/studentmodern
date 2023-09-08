import firebase_admin
import time
from firebase_admin import credentials
cred = credentials.Certificate("credent.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://arduinodoglure-default-rtdb.firebaseio.com/"
})
from firebase_admin import db
from serial import Serial
called = False
toggle = "a"
arduino = Serial(port='COM3',   baudrate=9600, timeout=.1)

"""
if ser.isOpen():
	while(True):
		input_data=ser.readline().strip().decode("utf-8")
		input_data = int(input_data)
		
"""


def listener(message):
    global called
    global toggle
    if not called:
        called = True
        return
    toggle += "a"
    #print(toggle)
    arduino.write(bytes(toggle,   'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    print(data)
    #print(str(int(toggle)).encode())
    #time.sleep(0.1)
    #print(ser.readline())
    #print(str(int(toggle)).encode())
    #print(str(incri).encode())
    #print(ser.readline().strip().decode("utf-8"))
   

my_stream = db.reference("main/event").listen(listener)



