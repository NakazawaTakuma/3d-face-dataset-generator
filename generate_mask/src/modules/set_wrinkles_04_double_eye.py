import cupy as cp
import random
from .apply_circle import apply_circle
from cupyx.scipy import ndimage


def set_wrinkles_04_double_eye(lp,c_data,c_img,img_size,use_image):
    # 二重の確率
    # 0 : 一重, 1 : 二重 , 2 : 目の内に入り込んだ二重, 3 : 目じりが垂れた二重  4 : 目じりが垂れた二重　and 目の内に入り込んだ二重
    if c_data[lp][2] < 15 and random.randint(0 , 50) > 0:  
        c_data[lp][17] = random.randint(0 , 2) 
    else:
        c_data[lp][17] = random.randint(0 , 3) 
        if c_data[lp][17] > 2 and random.randint(0 , 1) > 0:  
            c_data[lp][17] = 4


    if random.randint(0 ,1) > 0 and (c_data[lp][17] == 2 or c_data[lp][17] == 4):  
        c_data[lp][40] = 1
    else:
        c_data[lp][40] = 0
    
    power0 = random.uniform(0.8,1)

    if c_data[lp][17]  > 0:

        mask = use_image[8]

        if c_data[lp][17]  < 3 and random.randint(0,3) > 0:

            
                            
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

            x = int(img_size*(0.39))
            y = int(img_size*(0.453))
            r = random.randint(1,int(img_size*(0.05))) 
            power = 1#random.uniform(0.9,1)

            mask_c = apply_circle(mask_c,x, y, r, power,2)
                
            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (12, 12))

            #マスクからaddmask部分を切り取り
            mask = cp.clip(mask *(1-mask_c) , a_min = 0, a_max = 1)


        if  c_data[lp][17]  < 2 and random.randint(0,1) > 0  and c_data[lp][40] < 1:

                            
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

            x = int(img_size*(0.47))
            y = int(img_size*(0.46))
            r = random.randint(1,int(img_size*(0.02))) 
            power = 1#random.uniform(0.6,1)

            mask_c = apply_circle(mask_c,x, y, r, power,2)
                
            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (12, 12))

            #マスクからaddmask部分を切り取り
            mask = cp.clip(mask *(1-mask_c) , a_min = 0, a_max = 1)


        if c_data[lp][17]  < 3:
            #左右にコピー
            mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])

        

        #ぼかし
        #k = random.randint(0,2) 
        #mask = ndimage.gaussian_filter(mask, (k, k))

        c_img[lp][12] = cp.clip(mask * 255 * power0, a_min = 0, a_max = 255).astype(cp.uint8)
    else:
        c_img[lp][12] = cp.zeros((img_size,img_size), dtype=cp.uint8)



    if c_data[lp][40]  > 0:

        mask = use_image[9]
            
        #白丸を作成し除外する  
        mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

        x = int(img_size*(0.46))
        y = int(img_size*(0.47))
        r = random.randint(1,int(img_size*(0.008))) 
        power = 1#random.uniform(0.9,1)

        mask_c = apply_circle(mask_c,x, y, r, power,2)
            
        #ぼかし
        mask_c = ndimage.gaussian_filter(mask_c, (4, 4))

        #マスクからaddmask部分を切り取り
        mask = cp.clip(mask *(1-mask_c) , a_min = 0, a_max = 1)

        #左右にコピー
        mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])


        c_img[lp][13] = cp.clip(mask * 255 * power0, a_min = 0, a_max = 255).astype(cp.uint8)
    else:
        c_img[lp][13] = cp.zeros((img_size,img_size), dtype=cp.uint8)
   
