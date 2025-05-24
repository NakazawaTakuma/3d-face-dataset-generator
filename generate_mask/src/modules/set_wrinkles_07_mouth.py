import cupy as cp
import random

def set_wrinkles_07_mouth(lp,c_data,c_img,img_size,use_image):
    
    
    # しわのある確率
    if c_data[lp][2] < 65:
        prob = 0
    else:
        prob = random.randint(int(c_data[lp][2]-90),2) 

    mask = use_image[17]
    power = random.uniform(0.6,1)
    mask = mask*power
 

    if prob > 0:
        c_img[lp][20] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)
    else:
        c_img[lp][20] = cp.zeros((img_size,img_size), dtype=cp.uint8)
 
