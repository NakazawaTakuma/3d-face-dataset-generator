import numpy as np
from copy import copy
from scipy import interpolate

#splprep
def spline3(x,y,point,deg):
    
    for i in range(len(x)-1):
        if [x[i],y[i]] == [x[i+1],y[i+1]]:
            if not copy(x[i+1]) + 1 > 255:
                x[i+1] = copy(x[i+1]) + 1
            else:
                x[i+1] = copy(x[i+1]) - 1
            if not copy(y[i+1]) + 1 > 255:
                y[i+1] = copy(y[i+1]) + 1
            else:
                y[i+1] = copy(y[i+1]) - 1

    try:
        tck,u = interpolate.splprep([x,y],k=deg,s=10) 
    except:
        print('Error')
        try:
            tck,u = interpolate.splprep([x,y],k=deg,s=0) 
        except:
                print('Error')
                tck,u = interpolate.splprep([x,y],k=deg,s=50) 

    u = np.linspace(0,1,num=point,endpoint=True) 
    spline = interpolate.splev(u,tck)
    return spline[0],spline[1]


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))
