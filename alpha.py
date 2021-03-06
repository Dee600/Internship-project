# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:28:32 2017

@author: Durgesh Reddiyar

"""

from tkinter import *
import cv2
import numpy as np
import time
#from tkinter import messagebox
import ctypes
import os
from datetime import datetime
from PIL import Image
from appJar import gui
app = gui()


#temporary area






def callback():
    
    
 
    #cascades
    boxer_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\boxer_25.xml')
    hero_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\hero_dee.xml')
    #hero_cascade=cv2.CascadeClassifier('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\cascades_part3\\20.xml')


    #camera source 
    cam_source = 0
    
    cap = cv2.VideoCapture(cam_source)
    boxer_count=0
    hero_count=0
    
  #  ti=datetime.datetime.now()
  #  string_i_want=('%02d'%(ti.second))[:-4]
  #  print(string_i_want)
  
    termination_time_system1 = datetime.now()
    termination_time_start = termination_time_system1.second % 10
    print ("start",termination_time_start)
    
    time.sleep(1)
  
    while True:
        
        
        termination_time_system2 = datetime.now()
        termination_time_check = termination_time_system2.second % 10
        print ("current",termination_time_check)      
        select = 0
        
        ret, img = cap.read()
        if ret is True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            boxer = boxer_cascade.detectMultiScale(gray,1.3,5)
            hero = hero_cascade.detectMultiScale(gray,1.3,5)
       
        
            for (x,y,w,h) in boxer:
                #cls()
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img,'BOXER',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                print ("boxer_",boxer_count)
                boxer_count=boxer_count+1
                #select=2
                #time.sleep(0.5)
        
  
            for (x,y,w,h) in hero:
                #cls()
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img,'HERO',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                print ("hero_        ",hero_count)
                hero_count=hero_count+1
                #select=1
                #time.sleep(0.5)

            
            

        
            
        
            cv2.imshow('Detecting', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27 or termination_time_start == termination_time_check:
                
              break
      
    
    ret,img=cap.read()
   # cv2.imshow('capture.jpg',img)
    cv2.imwrite('C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\capture.jpg',img)
       
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    if(boxer_count>hero_count):
    
     print("boxer found")
     select=2
    elif (boxer_count<hero_count):
     print("hero found")
     select=1
    else:
     print("no object detected")
     
     
     
     
     
     
     
     
     
     

    img_rgb = cv2.imread('capture.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template_array2 = ["temp1_1.jpg","temp1_2.jpg"]
    
    if select == 1:
        item = template_array2[0]
    if select == 2:
        item = template_array2[1]
        
    template=cv2.imread(item,2)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.75
    loc = np.where( res >= threshold)
    counter1 = 0
    temp_ptx=999
    temp_pty=999
    for pt in zip(*loc[::-1]):
            
        im = Image.open("C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\capture.jpg")
        rgb_im = im.convert('RGB')
            
        ptx = int(pt[0] + w - 2)
        pty = int(pt[1] + h )
            
            
        posx = abs(temp_ptx - ptx)
        posy = abs(temp_pty - pty)
            
        if posx >5 and posy >5:
            print(ptx,pty)
            temp_ptx = ptx
            temp_pty = pty
            r, g, b = rgb_im.getpixel((ptx,pty))
            print ("RGB",r, g, b)
            if r>200 and g<50 and b<50:
                continue
            else:
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
                    counter1 = counter1 +1
            
    cv2.imwrite('res1.jpg',img_rgb)
    print ("first ",counter1) 
    cv2.waitKey()
    if(select==1 and first==1):
        app.infoBox(title, "hero passed")
    if(select==2 and first==5):
        app.infoBox(title, "boxer passed")
    if(select==1 and first != 1):
        app.infoBox(title, "fault detected in hero")
    if(select==2 and first != 5):
        app.infoBox(title, "fault detected in boxer")
        
        

callback()
