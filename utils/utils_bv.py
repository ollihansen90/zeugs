import numpy as np

def conv2d(img, kernel):
    ii, jj, nn = img.shape
    ki, kj = kernel.shape
    out = np.zeros_like(img)
    for n in range(nn):
        im = img[:,:,n]
        img_padded = pad(im)
        for i in range(ki):
            for j in range(kj):
                #print(img_padded[i:ii+i, j:jj+j].shape)
                out[:,:,n] += img_padded[i:ii+i, j:jj+j]*kernel[i,j]
    return out

def pad(img, mode="zeros"):
    out = np.zeros([img.shape[0]+2, img.shape[1]+2])
    out[1:-1,1:-1] = img
    return out
