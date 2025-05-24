import cv2 
import numpy as np
import cupy as cp
from copy import copy
import random

def create_mark_img(c_img,lp,img_size,use_image, category_num,mask,num_rate,num_rate2,mark_size,minsize,blursize,circle_rate,wart_rate,wart,wartonly):


    if num_rate2 > 0:
        if not wartonly:
            mask01 = np.zeros((img_size,img_size), dtype=np.uint8)

        for i in range(int(abs(np.random.normal(loc = 0,scale = 3,)*num_rate))):
            if np.random.randint(1,10) < 3:
                x = np.random.randint(0,img_size)
                y = np.random.randint(0,img_size)
            else:
                x = np.random.randint(int(img_size*0.4),img_size-int(img_size*0.4))
                y = np.random.randint(int(img_size*0.36),img_size-int(img_size*0.36))            
            r = int(abs(np.random.normal(loc = 0,scale = 3,  
                    )*mark_size)) + minsize
            r2 = r + r*int(abs(np.random.normal(loc = 0,scale = 3,  
                    ))) * circle_rate
            angle = int(np.random.randint(0,360))

            power = 255   
            if not wartonly: 
                cv2.ellipse(mask01, ((x, y), (r ,r2), angle), (power, power, power), thickness=-1)

            #wart
            if wart:
                if np.random.randint(-9,wart_rate) < 1:
                    power = np.random.randint(125,255)
                    cv2.ellipse(mask, ((x, y), (r ,r2), angle), (power, power, power), thickness=-1)

        if not wartonly:
            mask01 = cv2.blur(mask01, (blursize, blursize))

            mask01 = (cp.asarray(mask01)/ 255.).astype(cp.float32)
            
            mask01 = mask01 * use_image[0]
            
            c_img[lp][category_num] = copy(cp.clip(mask01 * 255, a_min = 0, a_max = 255).astype(cp.uint8))


    else:
        if not wartonly:
            c_img[lp][category_num] = copy(cp.zeros((img_size,img_size), dtype=cp.uint8))
    if wartonly:
        mask = cv2.blur(mask, (blursize, blursize))
        mask = (cp.asarray(mask)/ 255.).astype(cp.float32)
        mask = mask * use_image[0]
        c_img[lp][category_num]  = copy(cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8))
    return mask



def set_mark(lp,c_data,c_img,img_size,use_image):

    

    mask_wart = np.zeros((img_size,img_size), dtype=np.uint8)
    #mark
    if c_data[lp][2] < 15:
        prob = random.randint(int(c_data[lp][2]-90)*2,1) 
    else:
        prob = random.randint(int(c_data[lp][2]-90),20) 

    mask_wart =  create_mark_img(c_img,lp,img_size,use_image,0,mask_wart,3,prob,6,15,30,0.05,1,False,False)
    
    mask01 = (cp.asarray(copy(c_img[lp][0]))/ 255.).astype(cp.float32)   
    c_img[lp][0] = copy(cp.clip(mask01 * 255, a_min = 0, a_max = 255).astype(cp.uint8))
    
    #mark_black
    if c_data[lp][2] < 15:
        prob = random.randint(int(c_data[lp][2]-90)*2,1) 
    else:
        prob = random.randint(int(c_data[lp][2]-90),20) 
 
    mask_wart = create_mark_img(c_img,lp,img_size,use_image,1 ,mask_wart,3,prob,6,15,30,0.05,1,False,False)
    #acne
    mask_wart = create_mark_img(c_img,lp,img_size,use_image,2,mask_wart,2.5,np.random.randint(0,2),0.8,7,4,0.0,0,True,False)
    #mole
    mask_wart = create_mark_img(c_img,lp,img_size,use_image,3,mask_wart,1.5,np.random.randint(0,2),0.5,5,4,0.0,30,True,False)
    #wart
    mask_wart = create_mark_img(c_img,lp,img_size,use_image,4,mask_wart,3,np.random.randint(-3,2),2,6,8,0.0,0,True,True)
    
