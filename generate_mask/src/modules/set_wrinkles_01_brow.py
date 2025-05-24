
import cupy as cp
import random
from .apply_circle import apply_circle
from .vertical_distortion import VertDis
from cupyx.scipy import ndimage


def set_wrinkles_01_brow(lp,c_data,c_img,img_size,use_image):

    mask = cp.zeros((img_size,img_size), dtype=cp.float32)
      # しわのある確率
    if c_data[lp][2] < 15:
        prob = random.randint(int(c_data[lp][2]-90)*2,1) 
    else:
        prob = random.randint(int(c_data[lp][2]-90),20) 
        
    #prob = 1
    
    #しわある時→表情時のしわはmust  しわない時→表情時のしわは確率
    if prob  > 0 or random.randint(-1,2) > 0 :
        for i in range(5):

            if random.randint(0,20) < 1:
                continue

            add_mask = use_image[2]
            
            # 平行移動            
            add_mask = cp.roll(add_mask, int(img_size*0.011*i)+cp.random.randint(int(-img_size*0.002), int(img_size*0.002)), axis=0)   
     
                       
            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)

            x = int(img_size*0.5)
            y = int(img_size*0.3662)
            
            
            if i == 4:
                r = random.randint(int(img_size*0.05),r) 
                power = random.uniform(0.7,power)
            else:
                r = random.randint(int(img_size*0.05),int(img_size*0.25)) 
                power = random.uniform(0.7,1)

            mask_c = apply_circle(mask_c,x, y, r, power,2)

            #小さい黒丸を作成し除外する 

            for i in range(random.randint(-1,5)):
                rm = int(img_size*0.012*i)+random.randint(int(-img_size*0.002), int(img_size*0.002))
                x = random.randint(int(img_size*0.36),img_size - int(img_size*0.36))
                y = random.randint(int(img_size*0.35)+rm,int(img_size*0.40)+rm)
                r2 = random.randint(int(img_size*0.002),int(img_size*0.07))
                power2 = random.uniform(0.7,1)

                mask_c = apply_circle(mask_c,x, y, r2, power2,1)

            
            #ぼかし
            mask_c = ndimage.gaussian_filter(mask_c, (37, 37))


            #マスクからaddmask部分を切り取り
            add_mask = cp.clip(add_mask * mask_c , a_min = 0, a_max = 1)  

            # しわの追加
            mask = mask + add_mask

        #remove
        mask = mask * use_image[1]

        #垂直歪み
        for i in range( random.randint(0,4)):
            x = random.randint(int(img_size*0.44),img_size - int(img_size*0.44))
            r = random.randint(int(img_size*0.05),int(img_size*0.13))
            move = random.choice((random.randint(-int(img_size*0.005),-int(img_size*0.001)),random.randint(int(img_size*0.001),int(img_size*0.005))))
            mask = VertDis(mask,x,r,move,axis = 0)

        #ぼかし
        #mask = ndimage.gaussian_filter(mask, (2, 2))



    if prob  > 0:
        if c_data[lp][2] < 80 and random.randint(0,50) > 0:
            power = random.randint(120 , 220) 
        else:
            power = random.randint(120 , 255)
       
        c_img[lp][6] = cp.clip(mask * power, a_min = 0, a_max = 255).astype(cp.uint8)
    else:
        c_img[lp][6] = cp.zeros((img_size,img_size), dtype=cp.uint8)
    c_img[lp][7] = ndimage.gaussian_filter(cp.clip(mask * 255, a_min = 0, a_max = 255).astype(cp.uint8), (4, 4))


