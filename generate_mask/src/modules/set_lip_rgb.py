

import cupy as cp

def set_lip_rgb(lp,c_data):
    
    #cosmetic of lips
    if (c_data[lp][1]  < 1 and c_data[lp][2] > 16 and cp.random.randint(-2,4) > 0):
        c_data[lp][9] = 1
        if cp.random.randint(0,10) > -1:
            #red make up
            R = cp.random.uniform(0.45, 1)
            G = cp.random.uniform(0, 0.45)
            B = G + cp.random.uniform(-0.2, 0.2)
            c_data[lp][6] = int(c_data[lp][3]*R)
            c_data[lp][7] = int(c_data[lp][4]*G*R)
            c_data[lp][8] = int(c_data[lp][5]*B*R)
        else:
            #random color
            c_data[lp][6] = cp.random.randint(0,255)
            c_data[lp][7] = cp.random.randint(0,255)
            c_data[lp][8] = cp.random.randint(0,255)   
    else:

        #natural
        R = cp.random.uniform(0.75, 1.0)
        G = cp.random.uniform(0.55, 0.95)
        B = G + cp.random.uniform(-0.1, 0.1)
        c_data[lp][6] = int(c_data[lp][3]*R)
        c_data[lp][7] = int(c_data[lp][4]*G*R)
        c_data[lp][8] = int(c_data[lp][5]*B*R)
        c_data[lp][9] = 0

