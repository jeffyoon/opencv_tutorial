#!/usr/bin/env python

import cv2
import numpy as np

'''
In OpenCV you can easily read in images with different file formats (JPG, PNG, TIFF, etc.) using
imread.
The basic usage is shown below.

C++ : Mat imread(const string& filename, int flags = IMREAD_COLOR);
Python : image = cv2.imread(fileanme, flags = cv2.IMREAD_COLOR)

The flags option is used to control how the image is read.
Let's look at some common example.
In all the example below, make sure you use right namespace of C++ and import OpenCV for Python.

C++ : using namespace cv;
Python : import cv2

** Read as 8 -bit / channel color image (without Alpha channel). **
A vast majoriry of images are 8-bit per channel (or 24-bit) images.
They can be read using default flags.

C++ : Mat image = imread("image.jpg");
Python : image = cv2.imread("image.jpg")

** Read as 8-bit Grayscale Image. **
C++ : Mat image = imread("image.jpg", IMREAD_GRAYSCALE);
Python : image = imread("image.jpg", IMREAD_GRAYSCALE)

** Read as 16-bit / channel Color image. **
Most digital SLR cameras are capable of recording images at a higer bit depth than 8-bits channel.
The raw images from these cameras can be converted to 16-bit / chnnale PNG or TIFF images.
These 16-bit/channel images can be read using

C++ : Mat image = imread("image.png", IMREAD_ANYCOLOR | IMREAD_ANYDEPTH);
Python : cv2.imread("image.png", cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

You may also use the flag IMREAD_UNCHANGED instead. See an exmple below.

** Read a Transparent PNG or TIFF in OpenCV. **
A transparent image has four channels - 3 for color, and one for transparency.
These images can be read in OpenCV using the IMREAD_UNCHANGED flag.

C++ : Mat image = imread("image.png", IMREAD_UNCHANGED);
Python : cv2.imread("image.png", cv2.IMREAD_UNCHANGED)
'''

img = cv2.imread("sample.jpg", cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('test.jpg', img)
    cv2.destroyAllWindows()

