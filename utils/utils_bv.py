import numpy as np

def conv2d(img, kernel):
    ii, jj, nn = img.shape
    ki, kj = kernel.shape
    out = np.zeros_like(img)
    for n in range(nn):
        im = img[:,:,n]
        img_padded = pad(im, rand=(2*int(ki/2), 2*int(kj/2)))
        for i in range(ki):
            for j in range(kj):
                out[:,:,n] += img_padded[i:ii+i, j:jj+j]*kernel[i,j]
    return out

def conv2d_normed(im, kernel):
    ii, jj, nn = im.shape
    ki, kj = kernel.shape
    img_padded = pad(im[:,:,0], rand=(2*int(ki/2), 2*int(kj/2)))
    out = np.zeros([*im[:,:,0].shape, ki, kj])
    for i in range(ki):
        for j in range(kj):
            out[:,:,i,j] = img_padded[i:ii+i, j:jj+j]
    out = np.reshape(out, (ii, jj, ki*kj))
    out = out/np.linalg.norm(out, axis=-1, keepdims=True)
    kernel = kernel.flatten()
    kernel = kernel/np.linalg.norm(kernel)
    out = out@kernel
    return out

def pad(img, mode="zeros", rand=(2,2)):
    r = (int(rand[0]/2), int(rand[1]/2))
    out = np.zeros([img.shape[0]+rand[0], img.shape[1]+rand[1]])
    out[r[0]:-r[0],r[1]:-r[1]] = img
    return out

