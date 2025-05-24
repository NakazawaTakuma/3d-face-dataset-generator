import cupy as cp
import random
from .apply_circle import apply_circle
from cupyx.scipy import ndimage
from copy import copy


def set_wrinkles_06_nasolabial(lp,c_data,c_img,img_size,use_image):
    
    
    # しわのある確率
    if c_data[lp][2] < 15:
        prob = 0
    elif c_data[lp][2] > 40:
        prob = random.randint(int(c_data[lp][2]-90),150) 
    else:
        prob = random.randint(int(c_data[lp][2]-90),60) 


    #ほうれい線の有無
    c_data[lp][19] = prob



    mask = use_image[14]
    mask2 = use_image[15]       
    x = int(img_size*(0.46))
    y = int(img_size*(0.61))
    
    #黒丸を作成し除外する  
    mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
    if c_data[lp][2] < 30 or random.randint(0,30) > 0:
        r = random.randint(int(img_size*(0.035)),int(img_size*(0.08))) 
    else:
        r = random.randint(int(img_size*(0.035)),int(img_size*(0.06))) 

    power = 1

    mask_c = apply_circle(mask_c,x, y, r, power,2)

    #ぼかし
    mask_c = ndimage.gaussian_filter(mask_c, (30, 30))





    #マスクからmask_c部分を切り取り
    mask = cp.clip(mask*(1-mask_c) , a_min = 0, a_max = 1)
    mask2 = cp.clip((1 - (1 - mask2)*(1-mask_c)) , a_min = 0, a_max = 1)



    #ぼかし
    k = 8
    mask = ndimage.gaussian_filter(mask, (k, k))



    if random.randint(0,25) > 0:
        power = min((random.uniform(0.8,1.0)*c_data[lp][2]*0.012 + random.uniform(0.0,0.2)+ (k-5)*0.1,1.0))
        power2 = random.uniform(0.8,1)*(1.0-c_data[lp][2]*0.01)
    else:
        power = random.uniform(0.3,1)
        power2 = random.uniform(0.3,1)      


    # しわの追加
    mask = mask*power
    mask2 = (1 - (1 - mask2)*power2)



    #左右にコピー
    mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])  
    mask2[:,int(mask2.shape[1]*0.5):] = cp.fliplr(mask2[:,:int(mask2.shape[1]*0.5)])  
    

    if prob  > 0:
        c_img[lp][16] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)
        c_img[lp][17] = cp.clip(mask2 * 255, a_min = 0, a_max = 255).astype(cp.uint8)
        c_img[lp][18] = c_img[lp][16]
        c_img[lp][19] = c_img[lp][17]
    
    
    else:
        c_img[lp][16] = cp.zeros((img_size,img_size), dtype=cp.uint8)
        c_img[lp][17] = cp.full((img_size,img_size),255, dtype=cp.uint8 )
        c_img[lp][18] = c_img[lp][16]

        # 複製
        mask_E = copy(mask)
        mask2_E = copy(mask2)  
            

        #白丸を作成し除外する  
        mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
        x = int(img_size*(0.5))
        y = int(img_size*(0.5))
        r = random.randint(int(img_size*(0.004)),int(img_size*(0.04))) 
        power = random.uniform(0.6,1)

        mask_c = apply_circle(mask_c,x, y, r, power,2)
        
        #ぼかし
        mask_c = ndimage.gaussian_filter(mask_c, (27, 27))

        #マスクからmask_c部分を切り取り
        mask_E = cp.clip(mask_E*(1-mask_c) , a_min = 0, a_max = 1)
        mask2_E = cp.clip(1-(1-mask2_E)*(1-mask_c) , a_min = 0, a_max = 1)

        c_img[lp][19] = cp.clip(mask2_E * 255, a_min = 0, a_max = 255).astype(cp.uint8)

