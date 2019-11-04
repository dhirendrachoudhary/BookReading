import cv2
import numpy as np
def read_N_crop(img):

    blurred = cv2.blur(img, (3,3))
    canny = cv2.Canny(blurred, 50, 200)

    ## find the non-zero min-max coords of canny
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)

    ## crop the region
    cropped = img[y1:y2, x1:x2]
    cv2.imwrite("cropped.png", cropped)
    tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
    return tagged

def convert_arr(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return gray_img

crop_img = cv2.imread("cropped.png")
img = cv2.imread("test.jpeg")
num_arr = read_N_crop(img)
print(num_arr.shape)