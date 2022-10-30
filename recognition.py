import cv2
import numpy as np
import datetime
import serial
import RPi.GPIO as GPIO
from time import sleep
ser = serial.Serial('/dev/ttyS0', 9600)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay=23
GPIO.setup(relay,GPIO.OUT)
recognizer=cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
def upload(Id):
f = open("Test.txt", "w");
f.write(Id)
n= datetime.datetime.now()
f.write("%s"%n)
f.close()
f = open("Test.txt", "r");
contents = f.read()
print (contents)
print ("%s"%n)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
    if(conf<50):
    if(Id==1):
        Id="#enter your id"
        upload(Id)
    cv2.destroyAllWindows()
    e=input("Password:")
    if(e=="batman"): #custom password
        print("Place Finger")
        u=ser.read()
        print(u)
        if(u==b'1'):
            GPIO.output(relay,GPIO.HIGH)
            print ("Switched On")
            sleep(2) # Delay in seconds
            GPIO.output(relay,GPIO.LOW)
        else:
            print("Unauthorized")
        else:
            print("Unauthorized")
            if(Id==5):
            print("Unauthorized")
        upload(Id)
    cv2.putText(im,str(Id), (x,y+h),font,fontscale,fontcolor)
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    cam.release()
    cv2.destroyAllWindows()