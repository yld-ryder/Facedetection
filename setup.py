
import cv2           
import numpy as np    
from tkinter import *    
import sys                
from time import sleep     

 


def videoanalyze():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    

    eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

    cap=cv2.VideoCapture(0)

    while True:
        count=0
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
           count=count+1
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
           roi_gray=gray[y:y+h, x:x+w]
           roi_color=img[y:y+h, x:x+w]
           eyes=eye_cascade.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eyes:
               cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)
           
        


        cv2.imshow('img',img)
        print("the number of faces found=",count)
        k=cv2.waitKey(30)&0xff
        if k==27:
            break        

    cap.release()
    cv2.destroyAllWindows()



def imageanalyze():
    print("enter your footage name.extension")
    get = input()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    imgage = cv2.imread(get)
    gray = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(imgage,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = imgage[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    
    cv2.imshow('image',imgage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def quit():
    print('termination in progress !!!')
    sleep(0.9)
    exit()



def created_by():
    print("ABHISHEK TIWARI")
    print("emailmefella@gmail.com")
    print("7007409032")


def about():
    print(" this is a prototype of a face detection program which currently only marks out faces predent in any givemn image or video"

    
widget=Button(None,text='analyze videos',command=videoanalyze).pack(side=LEFT,expand=YES)
widget=Button(None,text='analyze images',command=imageanalyze).pack(side=RIGHT,expand=YES)
widget=Button(None,text='made by ',command=created_by).pack(side=BOTTOM,expand=YES)
widget=Button(None,text='about this small prototype',command=about).pack(side=BOTTOM,expand=YES)
widget=Button(None,text='kill it',command=quit).pack(side=TOP,expand=YES)
root.title('face detection')
widget.mainloop()


##    --(THE END)----

