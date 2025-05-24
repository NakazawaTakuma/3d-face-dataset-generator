import cupy as cp
import random
from .apply_circle import apply_circle
from .vertical_distortion import VertDis
from cupyx.scipy import ndimage



def set_wrinkles_03_glabella(lp,c_data,c_img,img_size,use_image):
    
    mask = cp.zeros((img_size,img_size), dtype=cp.float32)
    # しわのある確率
    if c_data[lp][2] < 20:
        prob = 0
    else:
        prob = random.randint(int(c_data[lp][2]-90),5) 

 

    aa0 = random.randint(3,4)
    move = 0


    if random.randint(0,1) > 0:
        prob1 = random.randint(4,10-aa0)
        if random.randint(int(c_data[lp][2]-90),10) > 0 and c_data[lp][2] > 50:
            prob2 = 0
        else:
            prob2 = 1

    else:
        prob1 = random.randint(1,3)
        prob2 = 0

    for i in range(prob1):

        if i < 1:
            aa = aa0
        else:
            aa = 1

        for a in range(aa):   

            if random.randint(-3,1) > 0 and i == 0:
                continue

            add_mask = use_image[7]
 
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
            y = int(img_size*(0.435))
            
            if i < 1:
            
                x = int(img_size*(0.5+random.uniform(-0.02,0.02)))
                r = random.randint(int(img_size*(0.005)),int(img_size*(0.02))) 
                power = 1#random.uniform(0.6,1)
                mask_c = apply_circle(mask_c,x, y, r, power,2)
                #ぼかし
                mask_c = ndimage.gaussian_filter(mask_c, (7, 7))
                #マスクからaddmask部分を切り取り
                add_mask = cp.clip(add_mask *(1-mask_c) , a_min = 0, a_max = 1)

            else:
                x = int(img_size*(0.5+random.uniform(-0.002,0.002)))
                r = random.randint(int(img_size*(0.012)),int(img_size*(0.024))) 
                power = 1
                mask_c = apply_circle(mask_c,x, y, r, power,2)
                #ぼかし
                mask_c = ndimage.gaussian_filter(mask_c, (7, 7))

                #マスクからaddmask部分を切り取り
                add_mask = cp.clip(add_mask *(1-mask_c) , a_min = 0, a_max = 1)


            # 平行移動    
            if i == 0: 
                if a < 1:  
                    add_mask = cp.roll(add_mask, int(img_size*0.004)+a*int(img_size*0.005) + cp.random.randint(0, int(img_size*0.002)), axis=0)   
                else:
                    add_mask = cp.roll(add_mask, int(img_size*0.004)+a*int(img_size*0.005) + cp.random.randint(int(-img_size*0.002), int(img_size*0.002)), axis=0)   
            else: 
                add_mask = cp.roll(add_mask, int(img_size*0.004)+(aa0-2)*int(img_size*0.005)+(i+1)*int(img_size*0.002) + cp.random.randint(int(-img_size*0.001), int(img_size*0.001)), axis=0)     

                #歪み
                x = int(img_size*(0.5))
                r = int(img_size*(0.07))
                move = int(img_size*i*0.008)
                add_mask = VertDis(add_mask,x,r,move,axis = 0)





            power = 1#random.uniform(0.9,1)  
            # しわの追加
            mask = cp.maximum(mask, add_mask*power)


            if prob2 > 0 and ((i == 1 and aa0 < 4) or (i == 0 and aa0 > 3) ):
                if c_data[lp][2] < 80 and random.randint(0,50) > 0:
                    power = random.randint(120 , 220)  
                else:
                    power = random.randint(150 , 255)
      
                c_img[lp][10] =cp.clip(mask * power, a_min = 0, a_max = 255).astype(cp.uint8)



    if prob  > 0:
        if prob2 < 1:
            if c_data[lp][2] < 80 and random.randint(0,50) > 0:
                power = random.randint(120 , 220) 
            else:
                power = random.randint(150 , 255)
         
            c_img[lp][10] = cp.clip(mask * power, a_min = 0, a_max = 255).astype(cp.uint8)
    else:
        
        c_img[lp][10] = cp.zeros((img_size,img_size), dtype=cp.uint8)
    c_img[lp][11] = ndimage.gaussian_filter(cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8), (3, 3))


        
