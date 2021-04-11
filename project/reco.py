import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
import RPi.GPIO as GPIO
from time import sleep
import os
#from pushbullet import Pushbullet

'''relay=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
GPIO.output(relay, False)
'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(7.5)

#pb = Pushbullet("o.KD2bOAMxqX9Vdfg0zKNSwpgNUAy8L46O")
#print(pb.devices)

with open('labels', 'rb') as f:
	dict = pickle.load(f)
	f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

font = cv2.FONT_HERSHEY_SIMPLEX

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	frame = frame.array
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
	for (x, y, w, h) in faces:
		roiGray = gray[y:y+h, x:x+w]

		id_, conf = recognizer.predict(roiGray)

		for name, value in dict.items():
			if value == id_:
				print(name)

		if conf <= 70:
                        p.ChangeDutyCycle(2.5)
                        print("unlocked")
                        os.system('/home/pi/project/pushbullet.sh "Alert!the door was unlocked"')
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)
                        sleep(3)
                        p.ChangeDutyCycle(7.5)

		else:
			print("unauthenticated person detected")
			os.system('/home/pi/project/pushbullet.sh "Intruder Alert!"')
			p.ChangeDutyCycle(7.5)
			sleep(1)

	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)

	rawCapture.truncate(0)

	if key == 27:
                GPIO.cleanup()
                break
                
cv2.destroyAllWindows()