import cupy as cp
import random
import numpy as np

def set_redness(lp,c_data):

    redness_type_num = 7 
    redness_ratio = random.randint(1,8) 
    for i in range(10,redness_type_num+10):
        
        if i == 16:
            c_data[lp][i] = random.uniform(0.0, 0.4)+0.3+abs(np.random.normal(
                loc   = 0,      # 平均
                scale = 3,      # 標準偏差
                ))*0.03  
        else:
            if cp.random.randint(0,redness_ratio) > 0:  

                c_data[lp][i] = 0
            else:
                c_data[lp][i] = random.uniform(0.0, 0.3)+0.4+abs(np.random.normal(
                loc   = 0,      # 平均
                scale = 3,      # 標準偏差
                ))*0.03  

    for i in range(41,43):
        
        if cp.random.randint(0,redness_ratio) > 0:  

            c_data[lp][i] = 0
        else:
            c_data[lp][i] = random.uniform(0.0, 0.3)+0.4+abs(np.random.normal(
            loc   = 0,      # 平均
            scale = 3,      # 標準偏差
            ))*0.03  