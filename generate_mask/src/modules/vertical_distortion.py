
import cupy as cp
import cv2 
import numpy as np

#vertical distortion
def VertDis(img,x,r,maxmove,axis,liner = False):

    move_all = 0

    maxmove *= 2
    r *= 2
    x *= 2

    img = cp.asarray(cv2.resize(cp.asnumpy(img),(int(img.shape[1]*2),int(img.shape[0]*2))))


    for i in range(r):

        if not liner:  
            move = ((np.exp(-((r-(i+1))*(4/(r-1)))**2 / 2) / np.sqrt(2 * np.pi))*2.5*maxmove)

        else:
            move = -(r-(i+1))*maxmove/r + maxmove


        move = round(move - move_all)

        #print(move)

        if axis < 1:
            img[:,x-(r-(i+1)):x+(r-(i+1))] = cp.roll(img, int(move) , axis=0)[:,x-(r-(i+1)):x+(r-(i+1))]
        
        else:
            img[x-(r-(i+1)):x+(r-(i+1)),:,] = cp.roll(img, int(move) , axis=1)[x-(r-(i+1)):x+(r-(i+1)),:]
        
        move_all += move

    img = cp.asarray(cv2.resize(cp.asnumpy(img),(int(img.shape[1]*0.5),int(img.shape[0]*0.5))))

    return img
