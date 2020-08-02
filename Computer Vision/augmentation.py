import cv2
import numpy as np
import os
import random

def RandomBrightness(img, loc):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img)
    scale = random.uniform(.8, 1.25)
    v = np.clip(v * scale, 0, 255, out=v)
    img = cv2.merge((h, s, v))
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    loc = loc + 'bright.jpg'
    cv2.imwrite(loc, img)
    

def saturation_image(image, saturation, loc):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    loc = loc + 'sat.jpg'
    cv2.imwrite(loc, image)

def hue_image(image, saturation, loc):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 + saturation, v - saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    loc = loc + 'hue.jpg'
    cv2.imwrite(loc, image)

def augment(src, dest):
    for filename in os.listdir(src):
        loc = os.path.join(dest, filename)
        image = cv2.imread(os.path.join(src, filename))
        RandomBrightness(image, loc)
        saturation_image(image, 30, loc)
        hue_image(image, 30, loc)
        

#augment('--path to source folder', '--path to destination folder')