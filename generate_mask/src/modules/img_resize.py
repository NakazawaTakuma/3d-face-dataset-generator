import cv2 
import cupy as cp

def img_resize(img,range,size):
    image = img[int(img.shape[0]*range[0][0]):int(img.shape[0]*range[0][1]) , int(img.shape[1]*range[1][0]):int(img.shape[1]*range[1][1])]
    mask = cp.zeros((img.shape[0],img.shape[1]), dtype=cp.float32)
    if size[0] < 0 and size[1] < 0:
        image_re = cp.asarray(cv2.resize(cv2.flip(cp.asnumpy(image),-1),(int(image.shape[1]*-size[1]),int(image.shape[0]*-size[0]))))
        mask[int(img.shape[0]*range[0][0])- image_re.shape[0]:
            int(img.shape[0]*range[0][0]) ,
            int(img.shape[1]*range[1][1]) :
            int(img.shape[1]*range[1][1]) + image_re.shape[1]] = image_re 
    elif size[0] < 0:
        image_re = cp.asarray(cv2.resize(cv2.flip(cp.asnumpy(image),0),(int(image.shape[1]*size[1]),int(image.shape[0]*-size[0]))))
        mask[int(img.shape[0]*range[0][0])- image_re.shape[0]:
            int(img.shape[0]*range[0][0]) ,
            int(img.shape[1]*range[1][1]) - image_re.shape[1]:
            int(img.shape[1]*range[1][1])] = image_re 
    elif size[1] < 0:
        image_re = cp.asarray(cv2.resize(cv2.flip(cp.asnumpy(image),1),(int(image.shape[1]*-size[1]),int(image.shape[0]*size[0]))))
    
        mask[int(img.shape[0]*range[0][0]):
            int(img.shape[0]*range[0][0]) + image_re.shape[0],
            int(img.shape[1]*range[1][1]) :
            int(img.shape[1]*range[1][1]) + image_re.shape[1]] = image_re 
    else:
        image_re = cp.asarray(cv2.resize(cp.asnumpy(image),(int(image.shape[1]*size[1]),int(image.shape[0]*size[0]))))     
        
        mask[int(img.shape[0]*range[0][0]):
            int(img.shape[0]*range[0][0]) + image_re.shape[0],
            int(img.shape[1]*range[1][1]) - image_re.shape[1]:
            int(img.shape[1]*range[1][1])] = image_re 
    return mask