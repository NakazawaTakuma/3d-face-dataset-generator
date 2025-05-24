
from re import I
import cv2 
import numpy as np
import cupy as cp
import random
from cupyx.scipy import ndimage
from copy import copy
from copy import deepcopy
from .utility import spline3
from .apply_circle import apply_circle


def set_hair_brow(lp,c_img,img_size,use_image):
    brows_lengh = 170
    brows_angle_rate =  random.randint(0,8)
    brows_angle_rate2 =  random.randint(0,50)
    bfore_move = 0
    borws_posi_x = [None]*6
    borws_posi_y = [None]*6
    if random.randint(0,8) > 0:
        borws_posi_x[0] = random.randint(int(img_size*0.47),int(img_size*0.48))
    else:
        borws_posi_x[0] = random.randint(int(img_size*0.45),int(img_size*0.50))

    if random.randint(0,8) > 0:
        borws_posi_x[5] = random.randint(int(img_size*0.37),int(img_size*0.40))
    else:
        borws_posi_x[5] = random.randint(int(img_size*0.35),int(img_size*0.43))

    dx_brow =  int((borws_posi_x[0] - borws_posi_x[5])/5.0)

    for i in range(1,5,1):
        borws_posi_x[i] = copy(borws_posi_x[0])-deepcopy(dx_brow)*i

        
    borws_posi_y[0] = random.randint(int(img_size*0.4175),int(img_size*0.4325))



    if brows_angle_rate > 0:
        borws_down_posi_y = random.randint(3,5)
    else:
        borws_down_posi_y = random.randint(2,5)



    for i in range(1,6,1):
        if i > borws_down_posi_y-1:
            if brows_angle_rate < 1:
                dy_brow = random.randint(0,int(img_size*0.01))
            elif brows_angle_rate2 > 0:
                dy_brow = random.randint(copy(bfore_move),int(img_size*0.01))
                bfore_move = copy(dy_brow)
            else:
                dy_brow = random.randint(-int(img_size*0.01),copy(bfore_move))
                bfore_move = copy(dy_brow)
            
        else:
            if brows_angle_rate > 0:
                dy_brow = random.randint(-int(img_size*0.0017),0)

            else:
                if  brows_angle_rate2 < 2:
                    dy_brow = random.randint(-int(img_size*0.015),0)
                else:
                    dy_brow = random.randint(-int(img_size*0.006),0)



        borws_posi_y[i] = deepcopy(borws_posi_y[i-1])  + dy_brow


    borws_t = [None]*6
    if random.randint(0,1)> 0:
        borws_t[0] = random.randint(int(img_size*0.005),int(img_size*0.0074))
    else:
        borws_t[0] = random.randint(int(img_size*0.003),int(img_size*0.013))

    if random.randint(0,3) > 0:
        dt_brow =  -int(borws_t[0]* random.uniform(0.0,0.2))
    else:
        dt_brow =  int(borws_t[0]* random.uniform(0.0,0.2))

   

    for i in range(1,6,1):
        if i == borws_down_posi_y:
            dt_brow =  -int(borws_t[0]* random.uniform(0.0,0.5))


        if borws_t[i-1] + dt_brow < int(img_size*0.0001):
            borws_t[i] = 0#int(img_size*0.0001)
        else:
            borws_t[i] = borws_t[i-1] + dt_brow

    borws_posi_cx = [None]*12
    borws_posi_cx[0:6] =  list(reversed(borws_posi_x))
    borws_posi_cx[6:12] =  borws_posi_x


    borws_posi_cy = [None]*12
    for i in range(0,6,1):

        borws_posi_cy[i] = borws_posi_y[5-i] - borws_t[5-i]
        borws_posi_cy[11-i] = borws_posi_y[5-i] +  borws_t[5-i]


    borws_posi_cx.append(borws_posi_cx[0])
    borws_posi_cy.append(borws_posi_cy[0])

    borws_posi_cx = np.asarray(borws_posi_cx)
    borws_posi_cy = np.asarray(borws_posi_cy)


    borws_posi_x_sp,borws_posi_y_sp = spline3(borws_posi_cx,borws_posi_cy,100,3) 

    points = [None]*len(borws_posi_x_sp)
    for i in range(len(borws_posi_x_sp)):
        points[i] = [borws_posi_x_sp[i],borws_posi_y_sp[i]]

    mask_borws = np.zeros((img_size,img_size), dtype=np.uint8)
    
    points = np.array(points)

    points = points.reshape((-1,1,2)).astype(np.int32)

    cv2.fillPoly(mask_borws, [points], (brows_lengh, brows_lengh, brows_lengh))

    mask_borws =(((cp.array(mask_borws)).astype(cp.float32))/255)


    #白丸を作成し除外する  
    mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
    if random.randint(0,2) > 0:
        x = borws_posi_x[0]
        y = borws_posi_y[0]+int(img_size*0.005)
        r = random.randint(int(img_size*(0.01)),int(img_size*(0.018))) 
        power = random.uniform(0.1,0.7)
        mask_c = apply_circle(mask_c,x, y, r, power,2)

    if random.randint(0,2) > 0:
        x = borws_posi_x[5] - int(img_size*(0.03))  
        y = borws_posi_y[0]
        r = random.randint(int(img_size*(0.02)),int(img_size*(0.05))) 
        power = random.uniform(0.1,0.7)
        mask_c = apply_circle(mask_c,x, y, r, power,2)

    #ぼかし
    k = random.randint(14,20)
    mask_c = ndimage.gaussian_filter(mask_c, (k, k))

    #マスクからaddmask部分を切り取り
    mask_borws = cp.clip(mask_borws*(1-mask_c) , a_min = 0, a_max = 1)
        

    #ぼかし
    k = random.randint(2,15)
    mask_borws = ndimage.gaussian_filter(mask_borws, (k, k))
    mask_borws = mask_borws*use_image[26]


    #左右にコピー
    mask_borws[:,int(mask_borws.shape[1]*0.5):] = cp.fliplr(mask_borws[:,:int(mask_borws.shape[1]*0.5)])  
    

    #配列の保存
    c_img[lp][26] = cp.clip(mask_borws * 255, a_min = 0, a_max = 255).astype(cp.uint8)
