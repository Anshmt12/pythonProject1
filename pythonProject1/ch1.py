#Image mosaicing

import numpy as np  #importing numpy library to work with arrays and scientific computing
import cv2          #importing opencv library after installing it. It has optimized algorithms for our tasks
import glob         #it is used to quickly extract pathnames. like here we need paths of multiple images and it helps in that
import imutils      #this is used as it has image processing functions which can be used along with opencv

image_paths = glob.glob('resources/*.jpg') #we have selected our folder of images
images = []

for image in image_paths:   #Now we are creating a loop and appending all images in a empty repository so that we can read thrm together and stitch them
    img = cv2.imread(image)
    images.append(img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

imageStitcher = cv2.Stitcher_create()  #Now we are using a stitch function to perform image mosaicing

error, stitched_img = imageStitcher.stitch(images)  #error is boolean here and it is assigned if images are not stitched

if not error:                                        #if images are stitched that means there is no error, we can simply show stitched image
    cv2.imwrite("stitchedOutput.png", stitched_img)
    cv2.imshow("Stitched Image", stitched_img)
    cv2.waitKey(0)

    #Finally our image mosaicing is complete
