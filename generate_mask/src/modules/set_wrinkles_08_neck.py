
import cupy as cp
import random
from cupyx.scipy import ndimage
import random
from .apply_circle import apply_circle

def set_wrinkles_08_neck(lp,c_data,c_img,img_size,use_image):
    c_img[lp][21] = cp.zeros((img_size,img_size), dtype=cp.uint8)
    # mask = use_image[18]
    # far_rate_02 = 75
    # しわのある確率
    # if c_data[lp][2] < 40 or c_data[lp][20] > far_rate_02:
    #     prob = 0
    # else:
    #     prob = random.randint(int(c_data[lp][2]-90),5) 
 
    
    # if prob  > 0:
    #     for l in range(3):
    #         #白丸を作成し除外する  
    #         mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
    #         x = int(img_size*(0.26)) 
    #         y = random.randint(int(img_size*(0.60)),int(img_size*(0.72))) 
    #         r = random.randint(1,int(img_size*(0.13))) 
    #         power = random.uniform(0.7,1)

    #         mask_c = apply_circle(mask_c,x, y, r, power,2)

    #         #ぼかし
    #         mask_c = ndimage.gaussian_filter(mask_c, (37, 37))

    #         #マスクからaddmask部分を切り取り
    #         mask = cp.clip(mask*(1-mask_c) , a_min = 0, a_max = 1)
            
      
    # power = random.uniform(0.9,1.1)
    # mask = mask*power

    # #平行移動
    # mask = cp.roll(mask,  random.randint(int(-img_size*0.004),int(-img_size*0.004)), axis=0) 
        
    # #左右にコピー
    # mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])  
    

    # if prob > 0:
    #     c_img[lp][21] = cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8)
    # else:
    #     c_img[lp][21] = cp.zeros((img_size,img_size), dtype=cp.uint8)




