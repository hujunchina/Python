import cv2
import numpy as np
import math

path = 'D:\projtest'


# 图像反转变化，并保存图像,公式：S=L-1-r
def reverse_img(img):
    reverse_img = 255 - img
    picpath = path + "\_reverse.png"
    cv2.imwrite(picpath, reverse_img)


# 图像对数变化，并保存图片，公式：s=clog(1+r)
def logTransform(img):
    c=1.0  #c为常数
    # 3通道RGB
    # '''h,w,d = img.shape[0],img.shape[1],img.shape[2]
    # new_img = np.zeros((h,w,d))
    # for i in range(h):
    #     for j in range(w):
    #         for k in range(d):
    #             new_img[i,j,k] = c*(math.log(1.0+img[i,j,k]))'''
    # 灰度图专属
    h, w = img.shape[0], img.shape[1]
    new_img = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.log(1.0 + img[i, j]))
    new_img = cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
    picpath = path + "\_logtransform.png"
    cv2.imwrite(picpath, new_img)
    return new_img

# 图像gamma变化，并保存图片，公式：s=cr^γ,其中c、γ 为常数。考虑偏移量上式可写为 s=c(ε+r)^γ
def gammaTranform(image):
    c=1
    gamma=0.1
    h,w,d = image.shape[0],image.shape[1],image.shape[2]
    new_img = np.zeros((h,w,d),dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j,0] = c*math.pow(image[i, j, 0], gamma)
            new_img[i,j,1] = c*math.pow(image[i, j, 1], gamma)
            new_img[i,j,2] = c*math.pow(image[i, j, 2], gamma)
    cv2.normalize(new_img,new_img,0,255,cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    picpath = path + "\_gamma0.1.png"
    cv2.imwrite(picpath, new_img)
    return new_img


if __name__ == "__main__":
    img = cv2.imread(r'D:\projtest\14.png', 1)  # 为0是灰度图，1是三通道图，2是深度图
    new_img = gammaTranform(img)