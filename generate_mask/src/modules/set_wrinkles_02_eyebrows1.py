import cupy as cp
import random
from .apply_circle import apply_circle
from .vertical_distortion import VertDis
from cupyx.scipy import ndimage

def set_wrinkles_02_eyebrows1(lp,c_data,c_img,img_size,use_image):
    mask = cp.zeros((img_size,img_size), dtype=cp.float32)
     
    # しわのある確率
    if c_data[lp][2] < 20:
        prob = 0
    else:
        prob = random.randint(int(c_data[lp][2]-90),10) 

    if c_data[lp][2] > 60 and random.randint(int(c_data[lp][2]-90),1) > 0:
        lp1 = random.randint(int(c_data[lp][2]*0.1),int(c_data[lp][2]*0.2)) + random.randint(5,15) 
    else:
        lp1 = 1



    #表情のしわと連動するしわの移動量を決定

    move_x0 = random.uniform(0.002,0.001)
 
    #中心のしわの確率
    center_w_prob = random.randint(0,1)
    #中心のしわの左右の確率
    center_w_rl_prob = random.randint(0,1)
    #表情時のしわ
    mask2 = use_image[5]
    #平行移動
    mask2 = cp.roll(mask2, int(img_size*(move_x0)), axis=1)


    #白丸を作成し除外する   
    mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
    x = int(img_size*0.43)
    y = int(img_size*0.43)
    r = random.randint(1,int(img_size*0.051)) 
    power = random.uniform(0.7,1)
    mask_c = apply_circle(mask_c,x, y, r, power,2)
    #ぼかし
    k = 17
    mask_c = ndimage.gaussian_filter(mask_c, (k, k))
    #マスクからaddmask部分を切り取り
    mask2 = cp.clip(mask2 *(1-mask_c) , a_min = 0, a_max = 1)  

    #左右反転
    mask2[:,int(mask2.shape[1]*0.5):] = cp.fliplr(mask2[:,:int(mask2.shape[1]*0.5)])  

    
    #中心のしわ
    if center_w_prob > 0:
        add_mask2 = use_image[6]
        #左右反転
        if center_w_rl_prob > 0:
            add_mask2 = cp.fliplr(add_mask2) 
        # しわの追加
        power = random.uniform(0.9,1)
        mask2 =cp.maximum(mask2, add_mask2*power)


    if prob  > 0:


        for i in range(lp1):   

            if i > lp1*0.7 and i%2 == 0:
                continue


            add_mask = use_image[3]

            #白丸を作成し除外する  
            mask_c = cp.zeros((img_size,img_size), dtype=cp.float32)
            x = int(img_size*0.47)
            y = int(img_size*0.445)

            if lp1 < 2:
                r = random.randint(int(img_size*0.025),int(img_size*0.05)) 
            else:
                r = random.randint(int(img_size*0.03),int(img_size*0.085)) 

            mask_c = apply_circle(mask_c,x, y, r, 1.0,2)

            if random.randint(0,1) > 0 and lp1 < 2:
                x = int(img_size*0.47)
                y = int(img_size*0.445)
                r = random.randint(int(img_size*0.01),int(img_size*0.03)) 
                mask_c = apply_circle(mask_c,x, y, r, 1.0,1)


            #ぼかし
            k = random.randint(10,15)
            mask_c = ndimage.gaussian_filter(mask_c, (k, k))
            


            add_mask = cp.clip(add_mask * mask_c , a_min = 0, a_max = 1)  

            # 平行移動   
            if i == 0:         
                    add_mask = cp.roll(add_mask, int(img_size*(move_x0)) , axis=1)   
            else:
                move = -int(img_size*((0.095+move_x0)/lp1*i)) + random.randint(-int(img_size*0.003),int(img_size*0.003)) 
                add_mask = cp.roll(add_mask, move, axis=1)  
                    
            #歪み
            y = int(img_size*0.35)
            move = -int(img_size*i/lp1*0.1)+ random.randint(-int(img_size*0.01),int(img_size*0.01)) 
            r = int(img_size*0.09) 
            add_mask = VertDis(add_mask,y,r,move,axis = 1,liner = True)


            # しわの追加
            power = random.uniform(0.7,1)
            mask =cp.maximum(mask, add_mask*power)
            #mask = mask + add_mask*power



        #左右にコピー
        mask[:,int(mask.shape[1]*0.5):] = cp.fliplr(mask[:,:int(mask.shape[1]*0.5)])  


        #中心のしわ
        if center_w_prob > 0:
            add_mask = use_image[4]
            #左右反転
            if center_w_rl_prob > 0:
                add_mask = cp.fliplr(add_mask) 
            # しわの追加
            power = random.uniform(0.9,1)
            #mask = mask + add_mask*power
            mask =cp.maximum(mask, add_mask*power)

    #remove
    mask = mask * use_image[1]


    # #平行方向歪み
    for i in range( random.randint(1,3)):
        y = random.randint(int(img_size*0.31),int(img_size*0.44))
        r = random.randint(int(img_size*0.03),int(img_size*0.08))
        move = random.choice((random.randint(-int(img_size*0.004),-int(img_size*0.001)),random.randint(int(img_size*0.001),int(img_size*0.004))))
        if prob  > 0:
            mask = VertDis(mask,y,r,move,axis = 1)
        mask2 = VertDis(mask2,y,r,move,axis = 1)


    if c_data[lp][2] < 80 and random.randint(0,50) > 0:
        power = random.randint(120 , 150) 
      
    else:
        power = random.randint(120 , 250)
 
    c_img[lp][8] = cp.clip(mask * power, a_min = 0, a_max = 255).astype(cp.uint8)
    c_img[lp][9] = cp.clip(mask2 * 255, a_min = 0, a_max = 255).astype(cp.uint8)


