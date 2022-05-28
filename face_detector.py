import cv2
from random import randrange

"""
#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('C:\\Users\DELL\Desktop\\haarcascade_frontalface_default.xml')


#Choose an image to detect faces in
#img = cv2.imread('C:\\Users\DELL\Desktop\\robert.jpeg')


#Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangle around the faces
for(x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y),(x+w, y+h), (randrange(225),randrange(225),randrange(225)), 2)


#print(face_coordinates)

#display the images with the faces
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
"""
#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# To capture video from webcam.
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    #Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


    #Draw rectangle around the faces
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (randrange(225),randrange(225),randrange(225)), 10)

    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    # stop if Q key is pressed
    if key==81 or key==113:
        break

# release the videocapture object
webcam.release()

print("Code Completed")
