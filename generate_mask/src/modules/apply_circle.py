import cupy as cp


def apply_circle(img,x, y, r, power,tag):
    c = r - 1
    s = c * 2 + 1
    circle_img =  cp.clip(r - cp.sqrt(cp.sum((cp.stack((
        cp.tile(cp.arange(s), (s, 1)),
        cp.repeat(cp.arange(s), s).reshape((-1, s))
    )) - c) ** 2, axis=0)), 0, 1)


    if y-c < 0:
        y11 = 0
        y12 = c - y
    else:
        y11 = y - c
        y12 = 0

    if y+c > img.shape[0]-1:
        y21 = img.shape[0]
        y22 = c + img.shape[0]- y
    else:
        y21 = y + c + 1 
        y22 = s + 1  

    if x-c < 0:
        x11 = 0
        x12 = c - x
    else:
        x11 = x - c
        x12 = 0
    if x+c > img.shape[1]-1:
        x21 = img.shape[1]
        x22 = c + img.shape[1]- x
    else:
        x21 = x + c + 1 
        x22 = s + 1  
    if tag == 0:
        img[y11:y21,x11:x21] = img[y11:y21,x11:x21] * cp.around(circle_img[y12:y22,x12:x22])*power
    elif tag == 1:
        img[y11:y21,x11:x21] = img[y11:y21,x11:x21] - cp.around(circle_img[y12:y22,x12:x22])*power
    else:
        img[y11:y21,x11:x21] = img[y11:y21,x11:x21] + cp.around(circle_img[y12:y22,x12:x22])*power
    return img

