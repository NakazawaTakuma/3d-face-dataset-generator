import cupy as cp
import random

def set_skin_rgb(lp,c_data):

    if cp.random.randint(0,200) > 0:

        R = cp.random.randint(45,255)
        
        c = int((R-45)/15)

        if c > 13:
            c = cp.random.randint(14,17)


        G = 34 + c*11 + int(c/2) 
        B = 30 + c*10 + cp.random.randint(c-20,c-10)  

        if R < G:
            c2 = int((R-55)/15)
            G = 34 + 11*c2


        if G < 34:
            G = 34
        if B < 30:
            B = 30

        if G > 255:
            G = 255
        if B > 255:
            B = 255

        if cp.random.randint(0,1) > 0:
            bis = cp.random.uniform(0.05, 1.0)
        else:
            bis = cp.random.uniform(0.5, 1.0)
     
        c_data[lp][3] = int(R*bis)
        c_data[lp][4] = int(G*bis)
        c_data[lp][5] = int(B*bis)            

    else:
        c_data[lp][3] = cp.random.randint(0,255)
        c_data[lp][4] = cp.random.randint(0,255)
        c_data[lp][5] = cp.random.randint(0,255)



    # skin light
    c_data[lp][18] = random.uniform(1.0,2.5)  
