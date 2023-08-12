# import the opencv library
import cv2

#Load the Cascade Classifier File
face_cascade = cv2.CascadeClassifier('C:/Users/HP/Desktop/Python WH class/c118 Face detection/haarcascade_frontalface_default.xml') 

# Define a video capture object
vid = cv2.VideoCapture(0)
