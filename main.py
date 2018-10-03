import cv2
import numpy as np
import time
#from tkinter import messagebox
import ctypes
import os


#console clearing ... not working still
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#cascades
boxer_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\cascade_boxer.xml')
hero_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\hero_dee.xml')
#hero_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\cascades_part3\\20.xml')


#Video source 0/1/2
cap = cv2.VideoCapture(0)
#initial count of objects counted
boxer_count=0
hero_count=0

#input video stream
while True:
    ret, img = cap.read()
    if ret is True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        boxer = boxer_cascade.detectMultiScale(gray,1.3,5)
        hero = hero_cascade.detectMultiScale(gray,1.3,5)
       
        #detecting different objects
        for (x,y,w,h) in hero:
            #cls()
            font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img,'HERO',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
            #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            print ("hero_        ",hero_count)
            hero_count=hero_count+1
            #time.sleep(0.5)

            
        for (x,y,w,h) in boxer:
            #cls()
            font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img,'BOXER',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
            #cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            print ("boxer_",boxer_count)
            boxer_count=boxer_count+1
            #time.sleep(0.5)

        
            
        
        cv2.imshow('Detecting', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
          break
      

    
cap.release()
cv2.destroyAllWindows()


img_rgb = cv2.imread('main.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res1.png',img_rgb)
cv2.waitKey()



#confidence of a object
if(boxer_count>hero_count):
 # messagebox.showinfo("Item Detected", "B104 FOUND!", )
 ctypes.windll.user32.MessageBoxW(0,"BOXER FOUND", "Item Detected",5)
elif (boxer_count<hero_count):
 # messagebox.showinfo("Item Detected", "HERO SILVER FOUND!")
  ctypes.windll.user32.MessageBoxW(0,"HERO FOUND", "Item Detected",5)
else:
 # messagebox.showinfo("WARNING", "No Object Found.")
 ctypes.windll.user32.MessageBoxW(0,"NO OBJECT FOUND", "RESULT",5)