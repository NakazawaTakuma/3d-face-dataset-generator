import cupy as cp
import random
from .apply_circle import apply_circle
from cupyx.scipy import ndimage
from .img_resize import img_resize
import cv2 
import numpy as np

def set_wrinkles_05_under_eye(lp,c_data,c_img,img_size,use_image):
    
    # しわ00のある確率
    prob0 = random.randint(0 , 1) 
    # しわ01のある確率
    prob1 = random.randint(0 , 1) 

    # しわ02のある確率
    if c_data[lp][2] < 20:
        prob2 = 0
    else:
        prob2 = random.randint(int(c_data[lp][2]-90),30) 

    # しわ03のある確率
    if c_data[lp][2] < 30:
        prob3 = 0
    else:
        prob3 = random.randint(int(c_data[lp][2]-90),15) 
       
    # しわ04のある確率
    if c_data[lp][2] < 15:
        prob4 = 0
    else:
        prob4 = random.randint(int(c_data[lp][2]-90),40) 
       


    mask = cp.zeros((img_size,img_size), dtype=cp.float32)
    mask_up = cp.zeros((img_size,img_size), dtype=cp.float32)
    mask2 = cp.zeros((img_size,img_size), dtype=cp.float32)

    # しわ00(目の下の膨らみ)
    if prob0  > 0:

        if c_data[lp][2] > 40 or random.randint(0,50) < 1:
            lp0 = random.randint(1 , 4)
        else:
            lp0 = 1
    
        for _ in range(lp0):

            add_mask = use_image[11]
       
                        
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

            x = int(img_size*(0.39))#random.choice((int(img_size*(0.39)),int(img_size*(0.43))))
            y = int(img_size*(0.47))
            r = random.randint(1,int(img_size*(0.055))) 
            power = 1#random.uniform(0.4,1)

            mask_c = apply_circle(mask_c,x, y, r, power,2)
            
            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (12, 12))
            
            #マスクからaddmask部分を切り取り
            add_mask = cp.clip(add_mask *(1-mask_c) , a_min = 0, a_max = 1)


            #resize
            if random.randint(0,50) > 0:
                y = random.uniform(0.8,max((1.0,c_data[lp][2]*0.01*2.3)))
            else:
                y = random.uniform(0.8,2.3)
            x = random.uniform(0.9,1.0+(y-1.0)*0.4)
            add_mask = img_resize(add_mask,((0.455,0.50),(0.35,0.47)),(y,x))

            # 平行移動
            y = int(img_size*(random.uniform(-0.006,0.009*y*0.357)))
            x = int(img_size*(random.uniform(0.0,0.01*(x-0.75))))
            add_mask = cp.roll(add_mask,  y, axis=0)
            add_mask = cp.roll(add_mask,  x, axis=1)

    
            
            power = random.uniform(0.5,1.0) 
            #power = 1
            # しわの追加
            mask2 = cp.maximum(mask2, add_mask*power)
        

   # しわ01(目の下のしわ)
    if prob1  > 0:

        # しわ01のループ数
        if c_data[lp][2] < 30 and random.randint(0,50)  > 0:
            lp1 = random.randint(1 , 5)
        else:
            lp1 = random.randint(1,int(c_data[lp][2]*0.1)+1) +random.randint(0 , 3) 

    
        for _ in range(lp1):

            add_mask = use_image[12]            
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)


            #resize
            if random.randint(0,50) > 0:
                yss = random.uniform(0.8,max((1.0,c_data[lp][2]*0.01*2.3)))
            else:
                yss = random.uniform(0.8,2.3)



            x = int(img_size*(0.39))
            y = int(img_size*(0.47))
            if c_data[lp][2] < 25 and random.randint(0,20)  > 0:
                r = int(random.randint(int(img_size*max([((0.05)*(max([0.0,(yss-1)*0.769]))),0.035])),int(img_size*(0.065))))+1
            else:
                r = int(random.randint(int(img_size*(0.05)*(max([0.0,(yss-1)*0.769]))),int(img_size*(0.065))))+1
           
            power = 1#random.uniform(0.4,1)

            mask_c = apply_circle(mask_c,x, y, r, power,2)
            
            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (20, 20))
            
            #マスクからaddmask部分を切り取り
            add_mask = cp.clip(add_mask *(1-mask_c) , a_min = 0, a_max = 1)

            #resize
            x = random.uniform(0.9,1.0+(yss-1.0)*0.4)
            add_mask = img_resize(add_mask,((0.455,0.50),(0.35,0.47)),(yss,x))

            # 平行移動
            y = int(img_size*(random.uniform(-0.006,0.009*yss*0.357)))
            x = int(img_size*(random.uniform(0.0,0.01*(x-0.75))))
            add_mask = cp.roll(add_mask,  y, axis=0)
            add_mask = cp.roll(add_mask,  x, axis=1)
   
            power = random.uniform(0.55,0.85)  



            mask = cp.maximum(mask, add_mask*power)



    # しわ02(目の下の膨らみ２)
    if prob2  > 0:

        add_mask = use_image[11]
                    
        #resize
        y = 0.6
        x = 0.85
        add_mask = img_resize(add_mask,((0.455,0.50),(0.35,0.47)),(y,x))


        # 平行移動
        y = int(img_size*(random.uniform(-0.001,0.0015)))   
        add_mask = cp.roll(add_mask,  y, axis=0)


        power = random.uniform(0.15,0.55)  
        # しわの追加
        
        if random.randint(0,4) > 0:
            mask_up = cp.maximum(mask_up, add_mask*power)
            #mask2 = mask2*(1-add_mask)
        else:
            mask2 = cp.maximum(mask2, add_mask*power)

    #remove
    mask_remove = use_image[10]
    mask = cp.clip(mask *(1-mask_remove) , a_min = 0, a_max = 1)
    mask_up = cp.clip(mask_up *(1-mask_remove) , a_min = 0, a_max = 1)

    # しわ03(目の周りのしわ)
    
    add_mask0 = cp.zeros((img_size,img_size), dtype=cp.float32)
    if prob3  > 0:
        
        lp3 = random.randint(int(c_data[lp][2]*0.1),int(c_data[lp][2]*0.2)) + random.randint(5,7) 

        if c_data[lp][2] > 80 and random.randint(-3,1)  > 0:
            bias3 = random.uniform(0.018,0.019)
            bias32 = random.randint(0,2)
        if c_data[lp][2] > 40 and random.randint(-2,1)  > 0:
            bias3 = random.uniform(0.019,0.020)
            bias32 = random.randint(-3,2)
        else:
            bias3 = random.uniform(0.019,0.022)
            bias32 = 0
        bias322 = random.uniform(-0.01,0.02)

        end_wrinkles = False
        for i in range(lp3):
            

            p_p =0


            power = 1
            add_mask = cp.zeros((img_size,img_size), dtype=cp.float32)

            if (bias32 < 1 or bias32 > 1 ) and 0.085/lp3*i > 0.013 and random.randint(0,2) > 0 :
                add_mask1 = use_image[13]
                #白丸を作成し除外する  
                mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

                x = int(img_size*(0.445))
                y = int(img_size*(0.615))
                r = random.randint(1+int(img_size*(bias3*6.5)),int(img_size*(0.145)))
                mask_c = apply_circle(mask_c,x, y, r, power,2)
                x = int(img_size*(0.491))
                y = int(img_size*(0.464))
                r = random.randint(int(img_size*0.005),int(img_size*0.005)+int(0.5*(int(img_size*0.145) - r )))
                mask_c = apply_circle(mask_c,x, y, r, power,2)
                #ぼかし
                mask_c = ndimage.gaussian_filter(mask_c, (7, 7))
                #マスクからaddmask部分を切り取り
                add_mask1 = cp.clip(add_mask1 *(1-mask_c) , a_min = 0, a_max = 1)
                add_mask = cp.maximum(add_mask, add_mask1)
                p_p = 1


            if bias32 > 0  and not end_wrinkles  and not end_wrinkles and random.randint(0,2) > 0:
                add_mask2 = use_image[13]
                #白丸を作成し除外する  
                mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
                x = int(img_size*(0.491))
                y = int(img_size*(0.464))
                r = random.randint(int(img_size*(0.06)),int(img_size*(0.08))) + int(img_size*(bias322))
                mask_c = apply_circle(mask_c,x, y, r, power,2)
                x = int(img_size*(0.445))
                y = int(img_size*(0.615))
                r22 = random.randint(int(img_size*0.01)+int(0.35*(int(img_size*0.145) - int(img_size*(0.08)) )),int(img_size*0.01)+int(0.95*(int(img_size*0.145) - r )))
                mask_c = apply_circle(mask_c,x, y, r22, power,2)
                #ぼかし
                mask_c = ndimage.gaussian_filter(mask_c, (12, 12))
                #マスクからaddmask部分を切り取り

                add_mask2 = cp.clip(add_mask2 *(1-mask_c) , a_min = 0, a_max = 1)
                add_mask = cp.maximum(add_mask, add_mask2)
                p_p = 1

            if p_p > 0:

                if random.randint(0,12) < 1:
                    end_wrinkles = True

                #resize
                x = 1+i*0.5/lp3 + random.uniform(-0.05,0.05)
                y = 1.0 + random.uniform(-0.05,0.05)
                add_mask = img_resize(add_mask,((0.465,0.615),(0.415,0.493)),(y,x))
                

                # 平行移動
                x = -int(img_size*(0.085/lp3*i)) + random.randint(-int(img_size*0.003),int(img_size*0.003))
                y = random.randint(0,int(img_size*0.004))
                add_mask = cp.roll(add_mask,  x, axis=1)
                add_mask = cp.roll(add_mask,  y, axis=0)

                power = random.uniform(0.7,0.8)
                # しわの追加
                #mask = mask + add_mask*power
                add_mask0 = cp.maximum(add_mask0, add_mask*power)


        #remove 
        add_mask0 = cp.clip(add_mask0 *(1-mask2*0.7) , a_min = 0, a_max = 1)

        

    # if prob4  > 0:
    #     lp4 = random.randint(int(c_data[lp][2]*0.1),int(c_data[lp][2]*0.13)) + random.randint(5,7)

    #     if c_data[lp][2] > 80 and random.randint(-30,1)  > 0:
    #         bias4 = 0.0
    #     elif c_data[lp][2] > 70 and random.randint(-3,1)  > 0:
    #         bias4 = 0.01
    #     elif c_data[lp][2] > 30 and random.randint(0,1)  > 0:
    #         bias4 = 0.02
    #     else:
    #         bias4 = 0.03
  

    #     for i in range(lp4):

    #         if random.randint(0,2) < 1:
    #             continue

    #         add_mask = use_image[13]

    #         #白丸を作成し除外する
    #         mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

    #         x = int(img_size*(0.445))
    #         y = int(img_size*(0.615))
    #         r = random.randint(int(img_size*(0.105+bias4)),int(img_size*(0.12+bias4)))
       
    #         power = 1#random.uniform(0.8,1)

    #         mask_c = apply_circle(mask_c,x, y, r, power,2)


    #         x = int(img_size*(0.491))
    #         y = int(img_size*(0.464))
    #         r = random.randint(int(img_size*0.005),int(img_size*0.009))
    #         power = 1#random.uniform(0.8,1)

    #         mask_c = apply_circle(mask_c,x, y, r, power,2)

    #         #ぼかし
    #         mask_c = ndimage.gaussian_filter(mask_c, (7, 7))
            
    #         #マスクからaddmask部分を切り取り
    #         add_mask = cp.clip(add_mask *(1-mask_c) , a_min = 0, a_max = 1)

    #         #resize
    #         x = 1.5 + random.uniform(-0.05,0.05)
    #         y = 1.0-(i)*2.0/lp4 + random.uniform(-0.05,0.05)
    #         b = 0.075
    #         if 0<= y < b:
    #             y = b
    #         elif  -b < y < 0:
    #             y = -b


    #         #厚み
    #         if abs(y) < 0.3:
    #             k = int(img_size*(0.0035)*(1-2*abs(y)))
    #             kernel = np.ones((k, k), np.uint8)
    #             add_mask = cp.asarray(cv2.dilate(cp.asnumpy(add_mask), kernel, iterations=1))

    #         add_mask = img_resize(add_mask,((0.465,0.615),(0.415,0.493)),(y,x))


    #         # 平行移動
    #         x = -int(img_size*(0.085))
    #         add_mask = cp.roll(add_mask,  x, axis=1)
    #         y2 = -int(img_size*(0.01/lp4*(i+1))) + random.randint(-int(img_size*0.003),int(img_size*0.003))
    #         add_mask = cp.roll(add_mask,  y2, axis=0)



    #         power = random.uniform(0.7,0.8)
 
    #         # しわの追加
    #         #mask = mask + add_mask*power
    #         add_mask0 = cp.maximum(add_mask0, add_mask*power)


    #     if c_data[lp][2] < 80 and random.randint(0,50) > 0:
    #         power = random.uniform(0.6,0.75)
    #     else:
    #         power = random.uniform(0.6,0.75)
    #     mask = cp.maximum(mask, add_mask0*power)


    #remove 
    mask_remove = use_image[10]
    mask2 = cp.clip(mask2 *(1-mask_remove) , a_min = 0, a_max = 1)


    #凹凸画像の合成
    mask2 = mask_up*0.25+0.5 - mask2*0.5

    #左右にコピー
    mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])  
    mask2[:,int(mask2.shape[1]*0.5):] = cp.fliplr(mask2[:,:int(mask2.shape[1]*0.5)])  



    c_img[lp][14] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)
    c_img[lp][15] = cp.clip(mask2 * 255, a_min = 0, a_max = 255).astype(cp.uint8)


