import bpy
import random
import numpy as np
import csv
from pathlib import Path




base_dir = Path(__file__).resolve().parent.parent.parent
csv_path = base_dir / "generate_mask" / "output" / "mask" / "dataset.csv"


with csv_path.open(newline="") as f:
    c_data = list(csv.reader(f))
         
     
 #HDR
base_dir2 = Path(__file__).resolve().parent.parent
hdr_dir  = base_dir2 / "assets" / "HDR"
pathlist = list(hdr_dir.rglob("*.hdr"))

output_dir  = base_dir2 / "output" / "images"

 
for lp in range(50):
    print(lp)
    #gender
    ge = int(c_data[lp+1][1])
    if ge > 0:
        bpy.data.objects['age'].data.body = "Male"
    else:
        bpy.data.objects['age'].data.body = "Female"  
    #age
    age = int(c_data[lp+1][2])
    bpy.data.objects['gender'].data.body = str(age) + " years old"


    # faceオブジェクトの情報を取得
    obj = bpy.data.objects["Average Head"]
    shape_keys = obj.data.shape_keys

    # toothオブジェクトの情報を取得
    obj_tooth = bpy.data.objects["tooth"]
    shape_keys_tooth = obj_tooth.data.shape_keys


    # 顔形状の決定

    ## shapekeys
    fat_rate =  int(c_data[lp+1][20])
    #fat_rate = 9
    far_rate_01 = 70
    far_rate_02 = 85
    far_rate_03 = 98

    infant_age = 12

    DEFAULT = False
    for block in shape_keys_tooth.key_blocks:
        if block.name == "歯茎の大きさ":
            
            value = 1-abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*0.1   
        else:
            value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*0.1       
            
        block.value = value
        
        if DEFAULT:
            block.value = 0
            
    #表情の決定

    e_e = random.randint(0, 20) 
    e_n_e = 0
    e_rate = random.randint(0, 1)
    #azian
    eye_posiy_rate = random.randint(0,3)

        
    eye_value =random.uniform(0, 1)



    #男女の違いを適用する確率 ?/(?+3)
    ge_apply0 = 1
    ge_applys1 = -5
    ge_applys2 = -5
    #年齢の違いを適用するか
    age_apply0 = 4#random.randint(0, 1) 
    age_applys1 = 0
    age_applys2 = 0

    #シェイプキー
    for block in shape_keys.key_blocks:

        #男女の違いを適用するか
        ge_apply = random.randint(ge_applys1, ge_apply0) 
        age_apply = random.randint(age_applys1, age_apply0) 
            
        if block.name == "のどぼとけ":
            if ge == 1:
                if fat_rate > far_rate_02:
                    value = 0
                else:
                    value = random.uniform(block.slider_min, block.slider_max)
            else:
                value = 0
            
        
        if (block.name == "小鼻の開きの幅"  or  block.name == "鼻筋のそり" or  block.name == "頬骨の高さ" or  block.name == "顔横のふくらみ" or  block.name == "顎先の前後" ) and ge_apply > 0:
            if ge == 1:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_min*0.1 + random.uniform(block.slider_min*0.1, block.slider_max*0.2)
            else:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.2, block.slider_max*0.1)
                                        
        elif block.name == "鼻筋の幅(根)":
            if shape_keys.key_blocks["鼻筋の幅"].value < 0:
                if ge_apply > 0:
                    if ge == 1:
                        value = abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*block.slider_min*0.1 
                    else:
                        value = abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*(shape_keys.key_blocks["鼻筋の幅"].value*0.9+1.15)*0.1 
                                                
                    
                else:
                        
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_min*0.1 + abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*(shape_keys.key_blocks["鼻筋の幅"].value*0.9+1.15)*0.1
            elif ge_apply > 0:
                if ge == 1:
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_min*0.1 + random.uniform(block.slider_min*0.1, block.slider_max*0.2)
                else:
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.2, block.slider_max*0.1)
            else: 
                value = np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*0.1
                
    
        
        elif block.name == "鼻筋の幅" and ge_apply > 0:
            if ge == 1:
                value = np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*block.slider_min*0.1 
            else:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.2, block.slider_max*0.1)
                
        
        elif (block.name == "小鼻の幅" or block.name == "頬骨(横)の幅" or block.name == "えらの幅" or block.name == "けつ顎" or block.name == "目の上の前後") and ge_apply > 0:
            if ge == 0:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_min*0.1 + random.uniform(block.slider_min*0.1, block.slider_max*0.2)
            else:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.2, block.slider_max*0.1)
        
        
        
        
        elif block.name == "鼻の高さ" :
            if ge_apply > 0:
                if ge == 0:
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_min*0.1 + random.uniform(block.slider_min*0.1, block.slider_max*0.2)
                else:
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.2, block.slider_max*0.1)
            else:
                value = random.uniform(-0.5,1) - abs(np.random.normal(
                                                                    loc   = 0,      # 平均
                                                                    scale = 3,      # 標準偏差
                                                                    ))*0.5*0.1
        
                
            

        
        
        elif block.name == "眉間の高さ" :
                if age_apply > 0 and age < infant_age:
                    value = random.uniform(block.slider_min,block.slider_min*0.8)
                else:
                    value = random.uniform(block.slider_min,block.slider_max) 
                    
        elif block.name == "鼻先の上下" :
            if  random.randint(0,20) > 0:
                if random.randint(0,1) > 0:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_max*0.05
                else:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_min*0.02  
            else:       
                if random.randint(0,1) > 0:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_max*0.1
                else:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_min*0.1                  
                    
                    
                    
                    
                                    
        elif block.name == "頬骨のたるみ"  and age_apply > 0:
            if age > 40:
                value = (-block.slider_min +block.slider_max)*age*0.01 + random.uniform(-0.1*(-block.slider_min+block.slider_max),0.1*(-block.slider_min+block.slider_max))
            else:
                value = random.uniform(block.slider_min,0)
                    
                                        
        elif block.name == "頬のたるみ" and age_apply > 0:
            if 75 > age > 50:
                value = random.uniform(0,(age-20)*0.0077)
            elif age > 60:
                value = random.uniform(0,age*0.0077)
            else:
                value = 0 
            
            
                
                
        elif (block.name == "顎の幅") and ge_apply > 0:
            if ge == 0:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_min*0.1 + random.uniform(block.slider_min*0.1, block.slider_max*0.4)
            else:
                value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1 + random.uniform(block.slider_min*0.4, block.slider_max*0.1)
                                            
        
        elif block.name == "頬のふくらみ":
            if age_apply > 0 and  age < 20:
                value = ((20 - age)*0.05)*block.slider_max  + abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1
            else:
                if fat_rate <= far_rate_01:
                    value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_min*0.1 + random.uniform(0, 0.1)
                else:
                    value = random.uniform(0, block.slider_max)
            

        elif block.name == "顎の肉00":
            if fat_rate <= far_rate_01:
                if age_apply > 0 and  age < infant_age:
                    value = random.uniform(0, block.slider_max*0.1)
                else:
                    value = random.uniform(0, block.slider_max)
            else:
                value = 0.0    
    
        elif block.name == "顎の肉01":
            if fat_rate <= far_rate_01:
                value = 0
            elif fat_rate <= far_rate_02:
                value = random.uniform(0, block.slider_max)
            else:
                value = 1.0
                            
        elif block.name == "顎の肉02":
            if fat_rate <= far_rate_02:
                value = 0
            elif fat_rate <= far_rate_03:
                value = random.uniform(block.slider_min, block.slider_max)
            else:
                value = 1.0
            
        elif block.name == "顎の肉03":
            if fat_rate <= far_rate_03:
                value = 0
            else:
                value = random.uniform(block.slider_min, block.slider_max)
            




    
        elif block.name == "首の太さ":
            if fat_rate <= far_rate_01:
                value = random.uniform(block.slider_min, 0.5)+ abs(np.random.normal(
                                                            loc   = 0,      # 平均
                                                            scale = 3,      # 標準偏差
                                                            ))*0.14
            else:
                value = random.uniform(-0.4, 0)+ abs(np.random.normal(
                                                            loc   = 0,      # 平均
                                                            scale = 3,      # 標準偏差
                                                            ))*0.15


                
            
        elif block.name == "顎の肉11": 
            if shape_keys.key_blocks["首の太さ"].value < 0.2 and  fat_rate <= far_rate_01:
            
                if random.randint(0,1) > 0:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_max*0.1
                else:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_min*0.1     
            else:
                value = 0       
                
                
        elif block.name == "首の筋": 
            if fat_rate <= far_rate_01 and age > 30:
                if age < 70:
                    if random.randint(0,1) > 0:
                        value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_max*0.1
                    else:
                        value = abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*block.slider_min*0.1     
                else:
                    value = random.uniform(0.5*(block.slider_min+block.slider_max), block.slider_max)
                    
            else:
                value = 0   
                            
                
        elif block.name == "顔横の肉":
            if fat_rate <= far_rate_01:
                value = random.uniform(block.slider_min, 0)+ abs(np.random.normal(
                                                            loc   = 0,      # 平均
                                                            scale = 3,      # 標準偏差
                                                            ))*block.slider_max*0.02   
            else:
                value = + abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*block.slider_max*0.01
                            
                
            
        elif block.name == "ほうれい線の位置":
            #value = random.uniform(block.slider_max*age*0.011-0.3, block.slider_max*age*0.011)
            #value = 0
            if shape_keys.key_blocks["頬のふくらみ"].value > 0.3 and  random.randint(0,   15) > 0:
                value = random.uniform(0.4, 1.0)
            elif age_apply > 0:
                if age < 60 or random.randint(0,   5) < 1:
                    value = random.uniform(block.slider_min, 0.8)
                else:
                    value = random.uniform(block.slider_max*age*0.011-0.3, block.slider_max*age*0.011)
                    
        elif block.name == "くちびるの厚さ(下)" :
            #value = random.uniform(block.slider_min, block.slider_max)
            if random.randint(0, 20) > 0:
                value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_min*0.1+random.uniform(0, block.slider_max)
            else:
                value = random.uniform(block.slider_min, block.slider_max)
                
                
        elif block.name == "くちびるの厚さ(上)":
                
                if ge_apply > 0:
                    if ge == 0:
                        value = shape_keys.key_blocks["くちびるの厚さ(下)"].value*0.9 + 0.8 + random.uniform(-0.1, 0.1)
                    else:
                        value = shape_keys.key_blocks["くちびるの厚さ(下)"].value*0.9 + 0.5 + random.uniform(-0.1, 0.1)
                else:
                    if random.randint(0, 20) > 0:
                        value = random.uniform(shape_keys.key_blocks["くちびるの厚さ(下)"].value,  block.slider_max)
                    else:
                        value = random.uniform(block.slider_min, block.slider_max)
                    
                
                        
        elif block.name == "くちびるの形2(上)": 
            max_lips2 = -4*shape_keys.key_blocks["くちびるの厚さ(上)"].value+6 
            if  random.randint(0, 20) > 0: 
                value_lip_s2 = 0
            else:
                value_lip_s2 = random.uniform(0, max_lips2-1) + abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*0.1
            if value_lip_s2 <= 1:
                value = value_lip_s2 
            else:
                value = 0
        
                    
        elif block.name == "くちびるの形3":
            if value_lip_s2 <= 1:
                value = 0
            else:
                value = value_lip_s2 - 1
                
                

    
        elif block.name == "目内の形(右)": 
            if (e_e == 3 or e_e == 4 or e_e == 7 or e_e == 9) :
                value = 0
            else:    
                value = eye_value  
            
        elif block.name == "目内の形(左)": 
            if (e_e == 3 or e_e == 4 or e_e == 8 or e_e == 9) :
                value = 0
            else:    
                value = eye_value  
            
                    
                    
        elif block.name == "鼻穴の大きさ" or block.name == "鼻穴の見え方" or block.name == "鼻先の大きさ" or block.name == "くちびるの厚さ(下)" or block.name == "くちびるの厚さ(上)" or block.name == "くちびるの形2(上)"   or block.name == "人中の深さ": 
            value = random.uniform(block.slider_min, block.slider_max)
            
            
        elif block.name == "二重の形１" : 
            if int(c_data[lp+1][17]) == 2 or int(c_data[lp+1][17]) == 4:
                if random.randint(0, 1) > 0 and int(c_data[lp+1][40]) >  0:
                    value = random.uniform(0, 2)
                else:
                    value = random.randint(0, 1)
            else:
                value = 0
            double_eye_value1 = value

            
        elif block.name == "二重の形２":
            if int(c_data[lp+1][17]) > 2 and random.randint(0, 1) > 0:
                if random.randint(0, 2) > 0:
                    value = random.uniform(block.slider_min, block.slider_max)
                else:
                    value = 1
            else:
                value = 0                  
            double_eye_value2 = value
            
        elif block.name == "二重の形３":
            if int(c_data[lp+1][17]) > 2 and double_eye_value2 == 0:
                if random.randint(0, 2) > 0:
                    value = random.uniform(block.slider_min, block.slider_max)
                else:
                    value = 1
            else:
                value = 0            
                
                
        elif block.name == "目の内の入り込み" : 
            if int(c_data[lp+1][40]) >  0:
                value = 1
            else:
                value = 0
                
        elif block.name == "目の内の位置" : 
            if int(c_data[lp+1][40]) >  0:
                value = random.uniform(block.slider_min, block.slider_max)
            else:
                value = 0
        
            
                
        elif block.name == "二重の位置(外)": 
            value = random.uniform(block.slider_min, block.slider_max)
                        
        elif block.name == "二重の位置(内)": 
            value = 0
            
            
        elif block.name == "二重の位置(up)" : 
            if int(c_data[lp+1][17]) == 1:
                value_double_eye_posi = random.uniform(-0.25, 2)
            elif int(c_data[lp+1][17]) == 0:
                value_double_eye_posi = 0
            else:
                value_double_eye_posi = random.uniform(-0.25, 1)
                
            if value_double_eye_posi > 0:
                value = value_double_eye_posi
            else:
                value = 0
                
            
            if double_eye_value1 > 0:
                value = 0
                
        elif block.name == "二重の位置(down)" : 
            if value_double_eye_posi > 0:
                value = 0
            else:
                value = -value_double_eye_posi
                
            if double_eye_value1 > 0:
                value = 0
        
        elif block.name == "二重の溝" : 
            value = 0
            
            
            
            
            
            
            
                                        
        else:

            if random.randint(0,100) > 0:
                if random.randint(0,1) > 0:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_max*0.1
                else:
                    value = abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*block.slider_min*0.1           
            else:
                value = random.uniform(block.slider_min, block.slider_max)


        if block.name == "鼻筋のそり" and age_apply > 0 and age < infant_age:
                value = abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*block.slider_max*0.1

        if block.name == "鼻の高さ" and age_apply > 0 and age < infant_age:
                value = -0.2 + np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*block.slider_min*0.03   
                            
        if block.name == "顔横のふくらみ" and age_apply > 0 and age < infant_age:
                value = random.uniform(block.slider_max*0.3, block.slider_max)
                
        if block.name == "鼻先の上下" and age_apply > 0 and age < infant_age:
                value = -0.3 + np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*block.slider_min*0.02  
                                                
                                    

        block.value = value
        if DEFAULT:
            block.value = 0
        
    
    ## rig
    #現在のフレームを設定
    bpy.context.scene.frame_current = 0


    # アクティブなオブジェクトを取得する
    obj_rig = bpy.data.objects["rig"]


    #表情の決定
    e_m = random.randint(0, 38) 


    e_n_m = 0
    if random.randint(0, 2) > 1:
        e_s = random.randint(0, 10) 
    else:
        e_s = 0
    e_n_s = 0

    ratio = random.randint(0,50)

    random_value_smile_eye = random.uniform(1, 100)





    # NLAストリップを取得する
    nla_tracks = obj_rig.animation_data.nla_tracks


    for track in nla_tracks:
        for strip in track.strips:
            # NLAストリップを取得する
            strip.scale = 100
            
            #顔形状の決定
            if '0FS' in strip.name:
                
                #男女の違いを適用するか
                ge_apply = random.randint(ge_applys2, ge_apply0) 
                age_apply = random.randint(age_applys2, age_apply0)
                
                if ratio > 49:
                    random_value = 50+np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    )*5   
                elif ratio > 40:                
                    random_value = 50+np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    )*5
                elif ratio > 30:
                    random_value = 50+np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    )*3.5   
                else:
                    random_value = 50+np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    )*1.5  

                #random_value = random.uniform(1, 100)           
                    
                if strip.name == "0FS_mouth_posi(y)" :
                    if random.randint(0,50) > 2:
                        
                        random_value = 50+abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*2.0 -abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        ))*4.0  
                    else:
                        random_value = 50+np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5 
            
                    
                    
                elif strip.name == "0FS_mouth_size":
                    if  ge_apply > 0:
                        if ge == 0:
                            random_value =  47 + np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        )*2.0  
                        else:
                            if random.randint(0,20) > 0:
                                random_value =  50 + np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                )*3.0  
                            else:
                                random_value =  50 + np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                )*5.0  							

                    else:
                        random_value =   50 + np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        )*2.0 
                        
                    if age_apply > 0 and age < infant_age:
                        random_value =  30 - abs(np.random.normal(
                                    loc   = 0,      # 平均
                                    scale = 3,      # 標準偏差
                                    ))*2.0 

                    
                                                            
                                                            
                elif strip.name == "0FS_eye_size":
                    if ge_apply > 0: 
                        if ge == 0:
                            random_value = 52+abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*0.5 - abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*1
                        else:
                            random_value = 48+abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*0.5 - abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*1         
                    else:
                        if random.randint(0, 20) > 0:
                            random_value = 50+abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*1.0 - abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*1
                        
                        else:  
                            random_value = 50+np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                )*5              
                        
                    if age_apply > 0 and random.randint(0,20) > 0: 
                        random_value -= random.uniform(((age*0.1)**2)*0.2,((age*0.1)**2)*0.3)
                                            
                        
                elif strip.name == "0FS_eye_up_posi(z)":
    #                if ge_apply > 0:
    #                    if ge == 0:
    #                        #random_value = random.uniform(40, 100)                         
    #                        random_value = random.uniform(0, 100)      
    #                    else:
    #                        random_value = random.uniform(1, 60)          
                    #else:
                    random_value = random.uniform(1, 100)  
                    
                    
                    
                elif strip.name == "0FS_eye_posi(y)":
                    if eye_posiy_rate > 0:

                        random_value = 50-abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*5) + abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*2)       
                    else:
                        random_value = random.uniform(40, 60)        
                    #random_value = random.uniform(0, 70)  
                    eye_posiy_value = random_value
                    
                elif strip.name == "0FS_eye_posi(x)":
                    if age_apply > 0 and age < infant_age:
                        random_value = 40-abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*4+abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*1                         
                    else:
                        random_value = 50+np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*5           
                                            
                elif strip.name == "0FS_eye_posi(z)":       
                    if random.randint(0,10) > 0:
                        random_value = 50+np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*3                                            
                    else:
                        
                        random_value = 50+np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*5
                            
                elif strip.name == "0FS_nose_posi(z)":
                    if age_apply > 0 and age < infant_age:
                            random_value = 50 + np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                )*2                   
                    
                    
                    else:                                            
                        if random.randint(0,10) > 0:
                            random_value = 50+np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                )*3                                             
                        else:
                            random_value = 50+np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                )*5                                                          

                elif strip.name == "0FS_mouth_posi(z)":
                    if random.randint(0,20) > 0:
                        random_value = 50+abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*4 -abs(np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            ))*0.5
                    else:
                        
                        random_value = 50+np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*5                                                                        

                elif strip.name == "0FS_eye_shape03":
                    random_value = 50-abs(np.random.normal(
                    loc   = 0,      # 平均
                    scale = 3,      # 標準偏差
                    ))*3       
                    
                elif strip.name == "0FS_eye_shape04":
                    range1 = 100 - nla_tracks["0FS_eye_shape03"].strips["0FS_eye_shape03"].action_frame_start
                    random_value = random.uniform(max([40,range1 -20]), range1 + 20)             
                        
                    
            
                    
                elif strip.name == "0FS_eye_up_posi(y)":
                    if eye_posiy_rate > 0:
                        if int(c_data[lp+1][17]) == 3:
                            random_value = random.uniform(max((30,-eye_posiy_value + 25)),90- eye_posiy_value)  
                        elif  int(c_data[lp+1][17]) == 0:
                            random_value = random.uniform(max((40,-eye_posiy_value + 25)),100- eye_posiy_value)  
                        else:
                            random_value = random.uniform(max((40,-eye_posiy_value + 25)),100- eye_posiy_value)  
                    else:
                        if int(c_data[lp+1][17]) == 3:
                            random_value = random.uniform(max((30,-eye_posiy_value + 90)),90-eye_posiy_value) 
                        elif  int(c_data[lp+1][17]) == 0:
                            random_value = random.uniform(max((40,-eye_posiy_value + 25)),100- eye_posiy_value)  
                        else:
                            random_value = random.uniform(max((40,-eye_posiy_value + 90)),100-eye_posiy_value)                        
                                                        
                elif strip.name == "0FS_headside_shape01": 
                    random_value = 50                
                    
                    
                elif strip.name == "0FS_jaw_length":
                    if ge_apply > 0:
                        if ge == 0:
                            random_value =  50 + abs(np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        ))*4.0  + random.uniform(-5, 5)
                        else:
                            random_value =   50 + abs(np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        ))*3.0  - abs(np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        ))*2.0 + random.uniform(-5, 5)  
                    else:              
                        random_value = 50+np.random.normal(
                            loc   = 0,      # 平均
                            scale = 3,      # 標準偏差
                            )*5  
                            
                    
                    random_value = 70


                                        
                elif strip.name == "0FS_face_length":
                                            

                    if random.randint(0,40) > 0:
                        if ge_apply > 0:
                            if ge == 0:
                                random_value = 50 - abs(np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                ))*3 + abs(np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                ))*1.5
                            else:
                                random_value = 50 - abs(np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                ))*1.5 + abs(np.random.normal(
                                                loc   = 0,      # 平均
                                                scale = 3,      # 標準偏差
                                                ))*1
                        else:
                            random_value = 50 - abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*2 + abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*1                                             
                    else:
                        random_value = 50 + np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        )*5                   

                                        
                    
                elif strip.name == "0FS_neck_length":
                    #random_value = random.uniform(1, 70)   
                    if age_apply > 0 and age < infant_age:
                        random_value =  abs(np.random.normal(
                                loc   = 0,      # 平均
                                scale = 3,      # 標準偏差
                                ))*age*0.1
                    else:      
                        if random.uniform(0, 50)  > 0:
                            random_value =  50 + abs(np.random.normal(
                                    loc   = 0,      # 平均
                                    scale = 3,      # 標準偏差
                                    ))*3 - abs(np.random.normal(
                                    loc   = 0,      # 平均
                                    scale = 3,      # 標準偏差
                                    ))*3
                        else:
                            random_value =  50 + np.random.normal(
                                    loc   = 0,      # 平均
                                    scale = 3,      # 標準偏差
                                    )*5
                        
                elif strip.name == "0FS_eye_up_posi(y)2":
                    if random.uniform(0, 50)  > 0:
                        random_value =  50 + np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*3.0  
                    else:
                        random_value =  50 + np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*5.0                  
                        

                elif strip.name == "0FS_head_size":
                    random_value = 50+abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*8) -abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5) 
            
                        
                elif strip.name == "0FS_jowside_posi(y)":
                    random_value = 50+np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5        

                elif strip.name == "0FS_jowside_posi(z)":
                    random_value = 50+abs(np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5)             
                    
                    
                elif strip.name == "0FS_jow_size":
                    

                    if ge_apply > 0:
                        if ge == 0:
                            random_value =  30 + np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*5.0  + random.uniform(0, 10)
                        else:
                            random_value =   50 + random.uniform(-10, 0)+ np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*5.0   
                    else:              
                        random_value =  50 + np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        )*5.0  
                
                    if age_apply > 0 and age < infant_age:
                        random_value =  random.uniform(41, 50)
                    
                    
                elif strip.name == "0FS_nose_size":
                    if age_apply > 0 and age < infant_age:
                        random_value = 40-abs(np.random.normal(
                                        loc   = 0,      # 平均
                                        scale = 3,      # 標準偏差
                                        ))*3                
                    else:
                        if random.uniform(0, 5)  > 0:
                            random_value = 50-abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*5       
                        else:
                            random_value = 50+np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*5                                              
                        
                elif strip.name == "0FS_face_posi(z)": 
                    if ge_apply > 0:
                        if ge == 0:
                            random_value = 1 + abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*5.0  
                        else:
                            random_value = 50 - abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*5.0
                    else:
                        random_value = random.uniform(1, 50) 
                    if age_apply > 0 and age < infant_age:
                            random_value = 1 + abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            ))*2.0                       
                        
                elif strip.name == "0FS_face_size(x)": 
                    random_value = 50 + np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*3.0  
                        
                elif strip.name == "0FS_eye_up_posi(z)2":

                    random_value = 50 + np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*5.0                     
                                            
                                                                                
                elif (strip.name == "0FS_eye_shape03" or strip.name == "0FS_eye_shape04" or strip.name == "0FS_eye_shape07" or strip.name == "0FS_eye_shape05"or strip.name == "0FS_eye_shape06"or strip.name == "0FS_eye_shape08") and(6 < e_e < 10 or 2 < e_e < 5):
                    random_value = 50  
    
    

                    
            #角度の決定
            if '0FA' in strip.name:
                #random_value = random.uniform(1, 100) 
                if random.randint(0, 3) < 1:
                    random_value = 50+np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5               
                else:
                    random_value = 50
                    
                if strip.name == "0FA_head_Rot(z)" and random.randint(0, 3) > 0:                
                    random_value = 50+np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*5                  
            
                if strip.name == "0FA_eye_Rot(x)":
                    random_value = 50+np.random.normal(
                        loc   = 0,      # 平均
                        scale = 3,      # 標準偏差
                        )*2  
                    eye_Rotx_value = random_value 
                    
                    if e_e == 7 or ((e_e == 5 or e_e == 4 or e_e == 3 or e_e == 2 ) and random_value_smile_eye > 70):
                        random_value = 50
                if strip.name == "0FA_eye_Rot(z)" and (abs(eye_Rotx_value - 50)+abs(random_value - 50)) > 50:
                    random_value  = 50+np.random.normal(
                                    loc   = 0,      # 平均
                                    scale = 3,      # 標準偏差
                                    )*(50 - abs(eye_Rotx_value - 50))*0.1   
                if strip.name == "0FA_eye_Rot(z)":              
                    if  e_e == 7 or ((e_e == 5 or e_e == 4 or e_e == 3 or e_e == 2 ) and random_value_smile_eye > 70):
                        random_value = 50
                    eye_Rotz_value = random_value 
                
            
                                    
                                    
            #表情の決定
            if '0FE' in strip.name:
                                        
                if "sub" in strip.name:
                    e_n_s += 1
                    if e_n_s == e_s:
                        if random.randint(0, 1) > 0:
                            random_value = abs(np.random.normal(
                                            loc   = 0,      # 平均
                                            scale = 3,      # 標準偏差
                                            )*10)
                        
                        else:
                            
                            random_value = random.uniform(1, 100)
                        
                    else:
                        random_value = 1 
                        
                else:
                
                    if 'mouth' in strip.name:
                        e_n_m += 1
                        if e_n_m == e_m:
                            random_value = random.uniform(1, 100)
                        else:
                            random_value = 1 
                        

                                            
                    elif 'eye' in strip.name:
                        e_n_e += 1
                        if e_n_e == e_e:    
                            if 'close' in strip.name:
                                if e_rate > 0:
                                    if random.randint(0,3) > 0:
                                        random_value = 100
                                    else:
                                        random_value = random.uniform(1, 100)
                                else:
                                    random_value = 1
                            else:
                                if (e_e == 5 or e_e == 4 or e_e == 3 or e_e == 2 ) :
                                    random_value = random_value_smile_eye
                                else:
                                    random_value = random.uniform(1, 100)
                        else:
                            random_value = 1 

                                    
        
            if DEFAULT:
                random_value = 50
                if '0FE' in strip.name:
                    random_value = 1
                    
            strip.action_frame_start = 1
            strip.action_frame_end = 200
            #print("random_value" + str(random_value))
            strip.action_frame_start = random_value
            strip.action_frame_end = 200#random_value

    


    #肌の決定
    main_dir = base_dir  / "generate_mask" / "output" / "mask" 


    material_name = "Skin_03"

    #毛穴の深さ

    #bpy.data.materials[material_name].node_tree.nodes["毛穴"].outputs[0].default_value = random.uniform(0.0, 0.35)

    #肌の凹凸

    #bpy.data.materials[material_name].node_tree.nodes["凹凸"].inputs[1].default_value = random.uniform(0.002, 0.003)

    #肌の色

    bpy.data.materials[material_name].node_tree.nodes["skin_color"].outputs[0].default_value = (float(c_data[lp+1][3])/255, float(c_data[lp+1][4])/255, float(c_data[lp+1][5])/255, 1)

    #bpy.data.materials["M_cube"].node_tree.nodes["RGB"].outputs[0].default_value = (float(c_data[lp+1][3])/255, float(c_data[lp+1][4])/255, float(c_data[lp+1][5])/255, 1)

    #顔面の明るさ補正
    bpy.data.materials[material_name].node_tree.nodes["skin_light"].inputs[1].default_value = float(c_data[lp+1][18])
    #bpy.data.materials["M_cube"].node_tree.nodes["skin_light"].inputs[1].default_value = float(c_data[lp+1][18])

    #肌の青むら
    bpy.data.materials[material_name].node_tree.nodes["skin_blue"].inputs[0].default_value =random.uniform(0.3, 0.5)
    bpy.data.materials[material_name].node_tree.nodes["skin_blue2"].inputs[0].default_value = random.uniform(0.3, 0.7)
    bpy.data.materials[material_name].node_tree.nodes["skin_blue3"].inputs[1].default_value = random.uniform(0.5, 1.2)
    bpy.data.materials[material_name].node_tree.nodes["skin_blue4"].inputs[1].default_value = random.uniform(0.5, 1.0)

    #肌の赤むら
    bpy.data.materials[material_name].node_tree.nodes["skin_red"].inputs[0].default_value =random.uniform(0.2, 0.4)

    #肌の黄むら
    bpy.data.materials[material_name].node_tree.nodes["skin_yellow"].inputs[1].default_value = random.uniform(0.0, 2.0)


    #肌の細かいしみ
    bpy.data.materials[material_name].node_tree.nodes["small_mark1"].inputs[0].default_value = random.uniform(0, 1)


    #肌のテカリ
    bpy.data.materials[material_name].node_tree.nodes["skin_specular"].inputs[1].default_value = random.uniform(0.3, 1.0)

    #肌の詳細
    bpy.data.materials[material_name].node_tree.nodes["skin_detail1"].inputs[1].default_value = random.uniform(0, 2)
    bpy.data.materials[material_name].node_tree.nodes["skin_detail2"].inputs[1].default_value = random.uniform(0, 2.5)

    #肌の凹凸
    bpy.data.materials[material_name].node_tree.nodes["skin_wrinkles_power"].outputs[0].default_value = random.uniform(0.7, 1.5)+abs(np.random.normal(
                                                                                                                        loc   = 0,      # 平均
                                                                                                                        scale = 3,      # 標準偏差
                                                                                                                        )*0.15)

    bpy.data.materials[material_name].node_tree.nodes["skin_wrinkles_power2"].inputs[1].default_value = random.uniform(0.0, 1.0)

    bpy.data.materials[material_name].node_tree.nodes["skin_wrinkles_power3"].inputs[1].default_value = random.uniform(0.0, 1.0)



    #くちびるの色

    bpy.data.materials[material_name].node_tree.nodes["lip_color"].inputs[7].default_value = (float(c_data[lp+1][6])/255., float(c_data[lp+1][7])/255., float(c_data[lp+1][8])/255., 1.)
    if int(c_data[lp+1][9]) > 0:
        bpy.data.materials[material_name].node_tree.nodes["lip_color.black"].inputs[0].default_value = random.uniform(0.0, 0.5)

    else:
        bpy.data.materials[material_name].node_tree.nodes["lip_color.black"].inputs[0].default_value = random.uniform(0.2, 1.0)


    #くちびるのテカリ

    if int(c_data[lp+1][9]) > 0:
        lip_roughness = random.uniform(0, 1.0)
    else:
        lip_roughness = random.uniform(0.0, 0.5)

    #bpy.data.materials[material_name].node_tree.nodes["lip_roughness"].outputs[0].default_value = lip_roughness
    bpy.data.materials[material_name].node_tree.nodes["lips_roughness"].inputs[1].default_value = lip_roughness


    #くちびるの凹凸
    bpy.data.materials[material_name].node_tree.nodes["lip_wrink_power"].outputs[0].default_value = random.uniform(0.0, 3.0)





    #肌の赤み

    bpy.data.materials[material_name].node_tree.nodes["red01"].inputs[0].default_value = float(c_data[lp+1][10])
    bpy.data.materials[material_name].node_tree.nodes["red02"].inputs[0].default_value = float(c_data[lp+1][11])
    bpy.data.materials[material_name].node_tree.nodes["red03"].inputs[0].default_value = float(c_data[lp+1][12])
    bpy.data.materials[material_name].node_tree.nodes["red04"].inputs[0].default_value = float(c_data[lp+1][13])
    bpy.data.materials[material_name].node_tree.nodes["red05"].inputs[0].default_value = float(c_data[lp+1][14])
    bpy.data.materials[material_name].node_tree.nodes["red06"].inputs[0].default_value = float(c_data[lp+1][15])
    bpy.data.materials[material_name].node_tree.nodes["red07"].inputs[0].default_value = float(c_data[lp+1][16])
    bpy.data.materials[material_name].node_tree.nodes["red08"].inputs[0].default_value = float(c_data[lp+1][41])
    bpy.data.materials[material_name].node_tree.nodes["red09"].inputs[0].default_value = float(c_data[lp+1][42])



    #しみとほくろとそばかすの決定
    mark_category  = ["mark","mark_black","acne","mole","wart","freckles"]
    for category in mark_category:
        img_path = main_dir / "mark" / category / f"{lp}.png"
        bpy.data.images[category].filepath = str(img_path)
        bpy.data.images[category].reload()

    #teeth_color
    bpy.data.materials["M_teeth.001"].node_tree.nodes["ミックス"].inputs[0].default_value = random.uniform(0.0, 0.4)+abs(np.random.normal(
                                                                                                                        loc   = 0,      # 平均
                                                                                                                        scale = 3,      # 標準偏差
                                                                                                                        )*0.03)



    #肌のwrinkles

    # Brow
    img_brow = main_dir / "wrinkles" / "01_brow" / f"{lp}.png"
    bpy.data.images["wrinkles_borw"].filepath = str(img_brow)
    bpy.data.images["wrinkles_borw"].reload()

    # Brow Expression
    img_brow_e = main_dir / "wrinkles" / "01_brow_E" / f"{lp}.png"
    bpy.data.images["wrinkles_borw_E"].filepath = str(img_brow_e)
    bpy.data.images["wrinkles_borw_E"].reload()
    value = max([nla_tracks["0FE_surprise_eye01"].strips["0FE_surprise_eye01"].action_frame_start/100 , -(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start-50)/100])
    bpy.data.materials[material_name].node_tree.nodes["w_brow_E_value"].outputs[0].default_value = value - 0.01


    # 眉のシワ 02_eyebrows1
    img_eyebrows1   = main_dir / "wrinkles" / "02_eyebrows1"   / f"{lp}.png"
    img_eyebrows1_E = main_dir / "wrinkles" / "02_eyebrows1_E" / f"{lp}.png"

    bpy.data.images["wrinkles_eyebrows1"].filepath   = str(img_eyebrows1)
    bpy.data.images["wrinkles_eyebrows1_E"].filepath = str(img_eyebrows1_E)

    # 変更を反映したい場合
    bpy.data.images["wrinkles_eyebrows1"].reload()
    bpy.data.images["wrinkles_eyebrows1_E"].reload()


    if nla_tracks["0FE_sad_eye01"].strips["0FE_sad_eye01"].action_frame_start > 1:
        value = nla_tracks["0FE_sad_eye01"].strips["0FE_sad_eye01"].action_frame_start/100
    elif nla_tracks["0FE_angry_eye01"].strips["0FE_angry_eye01"].action_frame_start > 1:
        value = nla_tracks["0FE_angry_eye01"].strips["0FE_angry_eye01"].action_frame_start/100
    else:
        value = 0
    bpy.data.materials[material_name].node_tree.nodes["w_eyebrows1_E_value"].outputs[0].default_value = value


    # 03_glabella
    img_glabella   = main_dir / "wrinkles" / "03_glabella"   / f"{lp}.png"
    img_glabella_E = main_dir / "wrinkles" / "03_glabella_E" / f"{lp}.png"

    bpy.data.images["wrinkles_glabella"].filepath   = str(img_glabella)
    bpy.data.images["wrinkles_glabella_E"].filepath = str(img_glabella_E)

    # 変更を反映させる
    bpy.data.images["wrinkles_glabella"].reload()
    bpy.data.images["wrinkles_glabella_E"].reload()

    if nla_tracks["0FE_angry_eye01"].strips["0FE_angry_eye01"].action_frame_start > 1:
        value = nla_tracks["0FE_angry_eye01"].strips["0FE_angry_eye01"].action_frame_start/100
    else:
        value = 0
    bpy.data.materials[material_name].node_tree.nodes["w_glabella_E_value"].outputs[0].default_value = value




    # パスを pathlib.Path で組み立て → 最後に str() で文字列化
    img_double_eye  = main_dir / "wrinkles" / "04_double_eye"  / f"{lp}.png"
    img_double_eye2 = main_dir / "wrinkles" / "04_double_eye2" / f"{lp}.png"

    bpy.data.images["wrinkles_double_eye"].filepath  = str(img_double_eye)
    bpy.data.images["wrinkles_double_eye2"].filepath = str(img_double_eye2)

    # 変更を反映させる
    bpy.data.images["wrinkles_double_eye"].reload()
    bpy.data.images["wrinkles_double_eye2"].reload()

    #Expression
    #close eye
    if nla_tracks["0FE_close_eye01"].strips["0FE_close_eye01"].action_frame_start > 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = (100 - 0.8*nla_tracks["0FE_close_eye01"].strips["0FE_close_eye01"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = (100 - 0.8*nla_tracks["0FE_close_eye01"].strips["0FE_close_eye01"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0
    elif nla_tracks["0FE_close_eye01_R"].strips["0FE_close_eye01_R"].action_frame_start > 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = 1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value =1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0.8*nla_tracks["0FE_close_eye01_R"].strips["0FE_close_eye01_R"].action_frame_start/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye_Iv"].inputs[0].default_value = 1
    elif nla_tracks["0FE_close_eye01_L"].strips["0FE_close_eye01_L"].action_frame_start > 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = 1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value =1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0.8*nla_tracks["0FE_close_eye01_L"].strips["0FE_close_eye01_L"].action_frame_start/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye_Iv"].inputs[0].default_value = 0
    elif nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start > 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = (100 - 0.6*nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = (100 - 0.6*nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0
    elif nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start > 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = (100 - 0.5*nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = (100 - 0.5*nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start)/100
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0

    else:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value = 1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value =1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye3"].inputs[0].default_value = 0

    if nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start > 50:
        if not nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start > 1 and not nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start > 1: 
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value =  1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = 1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
        elif nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start > 1:
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value =  min([ 1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
                                                                                                                , (100 - 0.6*nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start)/100])
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = min( [1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
                                                                                                                , (100 - 0.6*nla_tracks["0FE_happy_eye03"].strips["0FE_happy_eye03"].action_frame_start)/100])
        elif nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start > 1:
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye2"].inputs[0].default_value =  min( [1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
                                                                                                                , (100 - 0.5*nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start)/100])
            bpy.data.materials[material_name].node_tree.nodes["wrinkles_double_eye1"].outputs[0].default_value = min( [1 - 0.9*(nla_tracks["0FA_eye_Rot(z)"].strips["0FA_eye_Rot(z)"].action_frame_start - 50)/50
                                                                                                                , (100 - 0.5*nla_tracks["0FE_happy_eye02"].strips["0FE_happy_eye02"].action_frame_start)/100])
                                                                                                                


    # 05_under_eye
    img_under_eye   = main_dir / "wrinkles" / "05_under_eye"   / f"{lp}.png"
    img_under_eye2  = main_dir / "wrinkles" / "05_under_eye2"  / f"{lp}.png"

    bpy.data.images["wrinkles_under_eye"].filepath   = str(img_under_eye)
    bpy.data.images["wrinkles_under_eye2"].filepath  = str(img_under_eye2)

    # 06_nasolabial
    img_naso1 = main_dir / "wrinkles" / "06_nasolabial_v"   / f"{lp}.png"
    img_naso2 = main_dir / "wrinkles" / "06_nasolabial_^"   / f"{lp}.png"

    bpy.data.images["wrinkles_nasolabial"].filepath   = str(img_naso1)
    bpy.data.images["wrinkles_nasolabial2"].filepath  = str(img_naso2)

    # 変更を反映
    for name in ["wrinkles_under_eye", "wrinkles_under_eye2",
                "wrinkles_nasolabial", "wrinkles_nasolabial2"]:
        bpy.data.images[name].reload()


    c = 0
    if int(c_data[lp+1][19]) < 1:
        #Expression
        Exp = ["0FE_happy_mouth05","0FE_happy_mouth04","0FE_happy_mouth03","0FE_happy_mouth02","0FE_happy_mouth01","0FE_abc_mouth04","0FE_abc_mouth02","0FE_abc_mouth01"]
        biasl = [0.5,0.7,0.5,0.8,0.9,0.8,1.0,1.0]
        
        for i in range(len(Exp)):
            if nla_tracks[Exp[i]].strips[Exp[i]].action_frame_start > 1:
                
                c += 1
                bpy.data.images["wrinkles_nasolabial"].filepath = str(main_dir / "wrinkles/06_nasolabial_v_E" / f"{lp}.png")
                bpy.data.images["wrinkles_nasolabial2"].filepath = str(main_dir / "wrinkles/06_nasolabial_^_E" / f"{lp}.png")
                bpy.data.materials[material_name].node_tree.nodes["wrinkles__nasolabial"].outputs[0].default_value = biasl[i]*(float(nla_tracks[Exp[i]].strips[Exp[i]].action_frame_start)/100)
                bpy.data.materials[material_name].node_tree.nodes["wrinkles__nasolabial2"].outputs[0].default_value = biasl[i]*(float(nla_tracks[Exp[i]].strips[Exp[i]].action_frame_start)/100)

    if c < 1:
        bpy.data.materials[material_name].node_tree.nodes["wrinkles__nasolabial"].outputs[0].default_value = 1
        bpy.data.materials[material_name].node_tree.nodes["wrinkles__nasolabial2"].outputs[0].default_value = 1
        
        


    # 07_mouth
    img_mouth = main_dir / "wrinkles" / "07_mouth" / f"{lp}.png"
    bpy.data.images["wrinkles_mouth"].filepath = str(img_mouth)
    bpy.data.images["wrinkles_mouth"].reload()

    # 08_neck
    img_neck = main_dir / "wrinkles" / "08_neck" / f"{lp}.png"
    bpy.data.images["wrinkles_neck"].filepath = str(img_neck)
    bpy.data.images["wrinkles_neck"].reload()



    #cosmetic
    # 01_eyeshadow
    img_eyeshadow = main_dir / "cosmetic" / "01_eyeshadow" / f"{lp}.png"
    bpy.data.images["cosmetic_eyeshadow"].filepath = str(img_eyeshadow)
    bpy.data.images["cosmetic_eyeshadow"].reload()

    # 02_eyeline
    img_eyeline   = main_dir / "cosmetic" / "02_eyeline"   / f"{lp}.png"
    bpy.data.images["cosmetic_eyeline"].filepath   = str(img_eyeline)
    bpy.data.images["cosmetic_eyeline"].reload()
    #eyeshadow_color
    bpy.data.materials[material_name].node_tree.nodes["eyeshadow_color"].inputs[7].default_value = (float(c_data[lp+1][22])/255, float(c_data[lp+1][23])/255, float(c_data[lp+1][24])/255, 1)



    #Hair

    #brow
    img_brow = main_dir / "hair" / "03_brow" / f"{lp}.png"
    bpy.data.images["hair_brow"].filepath = str(img_brow)
    bpy.data.images["hair_brow"].reload()

    #eyelashes
    obj_eyelashes_up = bpy.data.objects["eyelashes"]
    obj_eyelashes_up2 = bpy.data.objects["eyelashes.001"]
    obj_eyelashes_dw = bpy.data.objects["eyelashes.002"]

    obj_eyelashes_up.modifiers["Surface Deform"]["Input_4"] = float(c_data[lp+1][43])
    obj_eyelashes_up.modifiers["Surface Deform"]["Input_10"] = float(c_data[lp+1][45])
    obj_eyelashes_up2.modifiers["Surface Deform"]["Input_4"] = float(c_data[lp+1][43])

    obj_eyelashes_dw.modifiers["Surface Deform"]["Input_4"] =float(c_data[lp+1][44])

    obj_eyelashes_up.modifiers["Surface Deform"]["Input_11"] = int(c_data[lp+1][46])


    #eye_color
    bpy.data.materials["M_eye.R"].node_tree.nodes["out_eye_rgb"].inputs[7].default_value = (float(c_data[lp+1][47])/255, float(c_data[lp+1][48])/255, float(c_data[lp+1][49])/255, 1)

    bpy.data.materials["M_eye.R"].node_tree.nodes["in_eye_rgb"].inputs[7].default_value = (float(c_data[lp+1][50])/255, float(c_data[lp+1][51])/255, float(c_data[lp+1][52])/255, 1)


    bpy.data.materials["M_eye.L"].node_tree.nodes["out_eye_rgb"].inputs[7].default_value = (float(c_data[lp+1][53])/255, float(c_data[lp+1][54])/255, float(c_data[lp+1][55])/255, 1)

    bpy.data.materials["M_eye.L"].node_tree.nodes["in_eye_rgb"].inputs[7].default_value = (float(c_data[lp+1][56])/255, float(c_data[lp+1][57])/255, float(c_data[lp+1][58])/255, 1)


    #eye_size
    bpy.data.shape_keys["Key.076"].key_blocks["EYE_B_size"].value = float(c_data[lp+1][60])
    bpy.data.shape_keys["Key.076"].key_blocks["EYE_C_size"].value = float(c_data[lp+1][59])

    bpy.data.shape_keys["Key.074"].key_blocks["EYE_B_size"].value = float(c_data[lp+1][60])
    bpy.data.shape_keys["Key.074"].key_blocks["EYE_C_size"].value = float(c_data[lp+1][59])



    #set_HDR
    enviroment = random.randint(0, len(pathlist) - 1)        
    bpy.data.images['enviroiment'].filepath = str(pathlist[enviroment])
    #enviroment += 1

    #if random.randint(0,3) > 0:
    #    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = random.uniform(0.5, 1)
    #else:
    #    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = random.uniform(0.2, 1)
    #   


    #現在のフレームを設定
    bpy.context.scene.frame_current = 0


    #rendering
    save_path = output_dir / f"{lp}.png"

    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render( filepath =str(save_path))