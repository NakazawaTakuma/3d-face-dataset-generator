import random
from copy import copy
from .utility import clamp

def set_hair_and_eye_rgb(lp,c_data):

    eye_rate1 = random.randint(1,22)
   
    #Brown
    if eye_rate1 < 10:
        a_color = random.randint(0,40)
        eye_color_r = random.randint(30 + a_color, 100,)
        eye_color_g = 15 + a_color
        eye_color_b = a_color 

        d_float = random.uniform(0.1, 2)
        
        eye_color_r = int(d_float*eye_color_r)
        eye_color_g = int(d_float*eye_color_g)
        eye_color_b = int(d_float*eye_color_b)
        
        c_data[lp][47] = copy(eye_color_r)
        c_data[lp][48]  = copy(eye_color_g) 
        c_data[lp][49]  = copy(eye_color_b)
        
        c_data[lp][53] = copy(eye_color_r)
        c_data[lp][54]  = copy(eye_color_g) 
        c_data[lp][55]  = copy(eye_color_b)

        d_float = random.uniform(0.4, 0.7)

        eye_color_r = int(d_float*eye_color_r)
        eye_color_g = int(d_float*eye_color_g)
        eye_color_b = int(d_float*eye_color_b)


        eye_color_r = clamp(eye_color_r, 0, 255)
        eye_color_g = clamp(eye_color_g, 0, 255)  
        eye_color_b = clamp(eye_color_b, 0, 255) 

        c_data[lp][50] = copy(eye_color_r)
        c_data[lp][51]  = copy(eye_color_g) 
        c_data[lp][52]  = copy(eye_color_b)

        c_data[lp][56] = copy(eye_color_r)
        c_data[lp][57]  = copy(eye_color_g) 
        c_data[lp][58]  = copy(eye_color_b)
    

    #Hazel
    elif eye_rate1 < 14:
        a_color = random.randint(-100,0)
        if a_color>-15:
            a_color2 = random.randint(0,-a_color)
        else:
            a_color2 = random.randint(0,15)
        a_color3 = random.randint(-5,0)
        eye_color_r = 220 + a_color + a_color2 + a_color3
        eye_color_g = 215 + a_color + a_color2 + random.randint(0,10)
        eye_color_b = 165 + a_color + a_color3

        c_data[lp][47] = copy(eye_color_r)
        c_data[lp][48]  = copy(eye_color_g) 
        c_data[lp][49]  = copy(eye_color_b)
        
        c_data[lp][53] = copy(eye_color_r)
        c_data[lp][54]  = copy(eye_color_g) 
        c_data[lp][55]  = copy(eye_color_b)


        a_color = random.randint(0,50)

        eye_color_r = 105 + a_color + random.randint(-10,10)
        eye_color_g = 65 + a_color + random.randint(-10,10)
        eye_color_b = 20 + a_color + random.randint(-10,10)

        d_float = random.uniform(0.5, 1.0)

        eye_color_r = int(d_float*eye_color_r)
        eye_color_g = int(d_float*eye_color_g)
        eye_color_b = int(d_float*eye_color_b)

        eye_color_r = clamp(eye_color_r, 0, 255)
        eye_color_g = clamp(eye_color_g, 0, 255)  
        eye_color_b = clamp(eye_color_b, 0, 255) 

        c_data[lp][50] = copy(eye_color_r)
        c_data[lp][51]  = copy(eye_color_g) 
        c_data[lp][52]  = copy(eye_color_b)

        c_data[lp][56] = copy(eye_color_r)
        c_data[lp][57]  = copy(eye_color_g) 
        c_data[lp][58]  = copy(eye_color_b)


    #Blue
    elif eye_rate1 < 18:
        

        eye_color_b = random.randint(150,255)
            

        eye_color_r = random.randint(eye_color_b-70,eye_color_b-40)
        eye_color_g = random.randint(eye_color_b-50,eye_color_b-18)

        c_data[lp][47] = copy(eye_color_r)
        c_data[lp][48]  = copy(eye_color_g) 
        c_data[lp][49]  = copy(eye_color_b)

        c_data[lp][53] = copy(eye_color_r)
        c_data[lp][54]  = copy(eye_color_g) 
        c_data[lp][55]  = copy(eye_color_b)

        if random.randint(0,2) > 0:

            d_float = random.uniform(0.4, 1)

            eye_color_r = int(d_float*eye_color_r)
            eye_color_g = int(d_float*eye_color_g)
            eye_color_b = int(d_float*eye_color_b)

        else:

            a_color = random.randint(0,50)

            eye_color_r = 105 + a_color + random.randint(-10,10)
            eye_color_g = 65 + a_color + random.randint(-10,10)
            eye_color_b = 20 + a_color + random.randint(-10,10)



        eye_color_r = clamp(eye_color_r, 0, 255)
        eye_color_g = clamp(eye_color_g, 0, 255)  
        eye_color_b = clamp(eye_color_b, 0, 255) 


        c_data[lp][50] = copy(eye_color_r)
        c_data[lp][51]  = copy(eye_color_g) 
        c_data[lp][52]  = copy(eye_color_b)


        c_data[lp][56] = copy(eye_color_r)
        c_data[lp][57]  = copy(eye_color_g) 
        c_data[lp][58]  = copy(eye_color_b)


    #gray
    elif eye_rate1 < 22:
        

        eye_color_b = random.randint(140,200)

        

        eye_color_r = eye_color_b + random.randint(-20,3)
        eye_color_g = eye_color_b + random.randint(-20,3)

        
        c_data[lp][47] = copy(eye_color_r)
        c_data[lp][48]  = copy(eye_color_g) 
        c_data[lp][49]  = copy(eye_color_b)

        c_data[lp][53] = copy(eye_color_r)
        c_data[lp][54]  = copy(eye_color_g) 
        c_data[lp][55]  = copy(eye_color_b)

        if random.randint(0,2) > 0:

            d_float = random.uniform(0.4, 1)

            eye_color_r = int(d_float*eye_color_r)
            eye_color_g = int(d_float*eye_color_g)
            eye_color_b = int(d_float*eye_color_b)

        else:

            a_color = random.randint(0,50)

            eye_color_r = 105 + a_color + random.randint(-10,10)
            eye_color_g = 65 + a_color + random.randint(-10,10)
            eye_color_b = 20 + a_color + random.randint(-10,10)


        eye_color_r = clamp(eye_color_r, 0, 255)
        eye_color_g = clamp(eye_color_g, 0, 255)  
        eye_color_b = clamp(eye_color_b, 0, 255) 

        c_data[lp][50] = copy(eye_color_r)
        c_data[lp][51]  = copy(eye_color_g) 
        c_data[lp][52]  = copy(eye_color_b)

        c_data[lp][56] = copy(eye_color_r)
        c_data[lp][57]  = copy(eye_color_g) 
        c_data[lp][58]  = copy(eye_color_b)


    

    #random
    else:
        RL_diff = random.randint(0,50)


        eye_color_r = random.randint(0,255)
        eye_color_g = random.randint(0,255)
        eye_color_b = random.randint(0,255)
        
        c_data[lp][47] = copy(eye_color_r)
        c_data[lp][48]  = copy(eye_color_g) 
        c_data[lp][49]  = copy(eye_color_b)

        if RL_diff > 0:
            c_data[lp][53] = copy(eye_color_r)
            c_data[lp][54]  = copy(eye_color_g) 
            c_data[lp][55]  = copy(eye_color_b)

        if random.randint(0,2) > 0:

            d_float = random.uniform(0.4, 1)

            eye_color_r = int(d_float*eye_color_r)
            eye_color_g = int(d_float*eye_color_g)
            eye_color_b = int(d_float*eye_color_b)

        else:


            eye_color_r = random.randint(0,255)
            eye_color_g = random.randint(0,255)
            eye_color_b = random.randint(0,255)


        eye_color_r = clamp(eye_color_r, 0, 255)
        eye_color_g = clamp(eye_color_g, 0, 255)  
        eye_color_b = clamp(eye_color_b, 0, 255) 

        c_data[lp][50] = copy(eye_color_r)
        c_data[lp][51]  = copy(eye_color_g) 
        c_data[lp][52]  = copy(eye_color_b)


        if RL_diff > 0:
            c_data[lp][56] = copy(eye_color_r)
            c_data[lp][57]  = copy(eye_color_g) 
            c_data[lp][58]  = copy(eye_color_b)  




        if RL_diff < 1:

            eye_color_r = random.randint(0,255)
            eye_color_g = random.randint(0,255)
            eye_color_b = random.randint(0,255)
            

            c_data[lp][53] = copy(eye_color_r)
            c_data[lp][54]  = copy(eye_color_g) 
            c_data[lp][55]  = copy(eye_color_b)

            if random.randint(0,2) > 0:

                d_float = random.uniform(0.4, 1)

                eye_color_r = int(d_float*eye_color_r)
                eye_color_g = int(d_float*eye_color_g)
                eye_color_b = int(d_float*eye_color_b)

            else:


                eye_color_r = random.randint(0,255)
                eye_color_g = random.randint(0,255)
                eye_color_b = random.randint(0,255)


            eye_color_r = clamp(eye_color_r, 0, 255)
            eye_color_g = clamp(eye_color_g, 0, 255)  
            eye_color_b = clamp(eye_color_b, 0, 255) 

            c_data[lp][56] = copy(eye_color_r)
            c_data[lp][57]  = copy(eye_color_g) 
            c_data[lp][58]  = copy(eye_color_b)  
    #eye_size        
    c_data[lp][59]  = random.uniform(0.35, 0.55)
    #eye_black_size
    c_data[lp][60]  = random.uniform(-0.65, 0.25)



