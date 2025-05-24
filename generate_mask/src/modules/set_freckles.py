import cv2 
import numpy as np
import cupy as cp
from copy import copy
import random


def set_freckles(lp,c_img,img_size,use_image):
    mask_freckles = np.zeros((img_size,img_size), dtype=np.uint8)
    freckle_rate = random.uniform(2, 20)
    freckle_rate2 = random.uniform(1.0, 1.2)
    for i in range(random.randint(-5,1)):
        for j in range(10):
            for k in range(random.randint(int(7*freckle_rate),int(9*freckle_rate))):


                x = int(abs(np.random.normal(loc = 0,scale = 3,  
                    ))) * 0.1*int(img_size*0.1) + np.random.randint(int(img_size*0.36)+int(img_size*0.015*j),int(img_size*0.36)+int(img_size*0.015*(j+1)))
                y = int(abs(np.random.normal(loc = 0,scale = 3,  
                    ))) * 0.1*int(img_size*0.05)  + np.random.randint(int(img_size*0.46)-int(img_size*0.002*j),int(img_size*0.54)-int(img_size*0.009*j))         

                minsize = 1
                mark_size = 0.8

                r = int(abs(np.random.normal(loc = 0,scale = 3,  
                        )*mark_size)) + minsize
                r2 = r + r*int(abs(np.random.normal(loc = 0,scale = 3,  
                        ))) * 0.01

                power = np.random.randint(int(240*freckle_rate2),int(255*freckle_rate2))
            
                cv2.ellipse(mask_freckles, ((x, y), (r ,r2), int(np.random.randint(0,360))), (power, power, power), thickness=-1)
                cv2.ellipse(mask_freckles, ((img_size - x + np.random.randint(0,int(img_size*0.01)), y + np.random.randint(0,int(img_size*0.01))), (r ,r2), int(np.random.randint(0,360))), (power, power, power), thickness=-1)
                

    k = 3
    mask_freckles = cv2.blur(mask_freckles, (k, k))
    mask_freckles = (cp.asarray(mask_freckles)/ 255.).astype(cp.float32)
    mask_freckles = mask_freckles * use_image[0]
    c_img[lp][5] = copy(cp.clip(mask_freckles * random.randint(200,255), a_min = 0, a_max = 255).astype(cp.uint8))

