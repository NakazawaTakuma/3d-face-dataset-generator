import cv2 
import numpy as np
import cupy as cp
import random
from .apply_circle import apply_circle
from cupyx.scipy import ndimage

def set_cosmetic(lp,c_data,c_img,img_size,use_image):
    #化粧をするか
    if (c_data[lp][1]  < 1 and c_data[lp][2] > 16 and cp.random.randint(0,1) > 0) or c_data[lp][9] > 0:
        c_data[lp][21] = 1   
    else:
        c_data[lp][21] = 0   
 
    
    #eyeshadow
    if c_data[lp][21] > 0 and random.randint(0,50) > 0:

        mask = use_image[19]
        k = random.randint(1,10)
        if random.randint(-2,1) > 0:
    
            mask = cp.maximum(mask, use_image[20])
            k = random.randint(10,25)
        if random.randint(-2,1) > 0:
      
            mask = cp.maximum(mask, use_image[21])
        if random.randint(-2,1) > 0:
           
            mask = cp.maximum(mask, use_image[22])
            k = random.randint(10,25)

        #ぼかし
        
        mask = ndimage.gaussian_filter(mask, (k, k))

        if random.randint(-3,1) > 0:

            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
            x = int(img_size*(0.49)) 
            y = random.randint(int(img_size*(0.43)),int(img_size*(0.48))) 
            r = random.randint(1,int(img_size*(0.08))) 
            power = random.uniform(0.7,1)
            mask_c = apply_circle(mask_c,x, y, r, power,2)

            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (40, 40))

            #マスクからaddmask部分を切り取り
            mask = cp.clip(mask*(1-mask_c) , a_min = 0, a_max = 1)

        #remove
        mask = cp.clip(mask*(1-use_image[24]) , a_min = 0, a_max = 1)


              
        c_img[lp][22] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)


        #eyeshadow_color
        csmetic_1_rate = random.randint(1,20)
        
        if csmetic_1_rate < 3:
            #ather color
            c_data[lp][22] = cp.random.randint(0,255)  #R
            c_data[lp][23] = cp.random.randint(0,255)  #G 
            c_data[lp][24] = cp.random.randint(0,255)  #B


        elif csmetic_1_rate < 5:
            #blue shadow
            rgb = random.uniform(0.01,1.0)
            R = cp.random.randint(-50,-40)
            G = cp.random.randint(-50,-40)
            B = cp.random.randint(40,55)
            c_data[lp][22] = int((c_data[lp][3]+R)*rgb)
            c_data[lp][23] = int((c_data[lp][4]+G)*rgb)
            c_data[lp][24] = int((c_data[lp][5]+B)*rgb)
            for i in range(22,25,1):
                if c_data[lp][i] > 255:
                    c_data[lp][i] = 255
                elif c_data[lp][i] < 0:
                    c_data[lp][i] = 0

        elif  csmetic_1_rate < 9:

            #red shadow

            rgb = random.uniform(0.01,1.0)
            R = cp.random.randint(25,45)
            G = random.uniform(0.3,0.5)
            B = random.uniform(0.3,1.0)
            c_data[lp][22] = int((c_data[lp][3]+R)*rgb)
            c_data[lp][23] = int((c_data[lp][4]*G)*rgb)
            c_data[lp][24] = int((c_data[lp][5]*B)*rgb)
            for i in range(22,25,1):
                if c_data[lp][i] > 255:
                    c_data[lp][i] = 255
                elif c_data[lp][i] < 0:
                    c_data[lp][i] = 0
        else:                            
            #dark shadow
            R = random.uniform(0.01,0.4)
            G = random.uniform(0.3,1.0)
            B = random.uniform(0.3,1.5)
            c_data[lp][22] = int(c_data[lp][3]*R)
            c_data[lp][23] = int(c_data[lp][4]*G*R)
            c_data[lp][24] = int(c_data[lp][5]*B*R)
            for i in range(22,25,1):
                if c_data[lp][i] > 255:
                    c_data[lp][i] = 255
                elif c_data[lp][i] < 0:
                    c_data[lp][i] = 0

    else:
        c_img[lp][22] = cp.zeros((img_size,img_size), dtype=cp.uint8)
        c_data[lp][22] = int(c_data[lp][3])
        c_data[lp][23] = int(c_data[lp][4])
        c_data[lp][24] = int(c_data[lp][5])



    #eyeline
    if c_data[lp][21] > 0 and random.randint(-1,1) > 0:
        
        
        main_dir = "E:/CNN/"
        #up
        theck = random.randint(0,3)*10 + 1 + min((int(abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*0.4),3)) 

        mask = cp.array(cv2.resize(cv2.imread(main_dir + "3Dface/eye_line/up/"+str(theck).zfill(3)+".png",cv2.IMREAD_GRAYSCALE), (img_size,img_size)))
        mask = (mask / (255.)).astype(cp.float32)



        #ぼかし
        bl = random.randint(-1,1)

        #down 
        if  random.randint(-1,1) > 0:
            num = random.randint(1,10)

            mask2 = cp.array(cv2.resize(cv2.imread(main_dir + "3Dface/eye_line/down/"+str(num)+"_0.png",cv2.IMREAD_GRAYSCALE), (img_size,img_size)))
            mask2 = (mask2 / (255.)).astype(cp.float32)

            #mask2 = VertDis(mask2,x,r,move,axis = 0)
            mask = cp.maximum(mask, mask2)
            
        # #ぼかし
        if bl > 0 or random.randint(0,1) > 0:
            k = random.randint(0,3)
            mask = ndimage.gaussian_filter(mask, (k, k))
            
            


        #左右にコピー
        mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])  
    
    else:
        mask = cp.zeros((img_size,img_size), dtype=cp.float32)

    c_img[lp][23] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)


    #eyelashes_length
    #up
    if c_data[lp][21] > 0 :
        c_data[lp][43]  = random.uniform(0.0,1.0)
    else:
        if random.randint(0,20) > 0:
            c_data[lp][43]  = random.uniform(0.0,0.7)       
        else:
            c_data[lp][43]  = random.uniform(0.0,1.0)

    #down
    c_data[lp][44]  = random.uniform(0.0,min((c_data[lp][43]*1.5,1)))


    #eyelashes_angle
    if c_data[lp][17] > 2:  
        c_data[lp][45]  = 1.0
    else:
        if random.randint(0,3) > 0:
             c_data[lp][45]  = random.uniform(0.0,0.1)
        else:
            c_data[lp][45]  = random.uniform(0.0,1.0)

    #eyelashes_density
    if c_data[lp][21] > 0 :
        if random.randint(0,1) > 0:
             c_data[lp][46]  = random.randint(0,3)
        else:
            c_data[lp][46]  = random.randint(0,8)
    else:   
        c_data[lp][46]  = random.randint(0,3)

