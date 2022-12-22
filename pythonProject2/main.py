#LOGIC FOR DOING IMAGE SEGMENTATION FOR A RED ARROW IN VIDEO
#1. We will extract frames of video and store it in a new directory. We will run a loop in a directory such that all images are selected
#2. We will do shape detection now. An arrow will be having 7 corners and contour function can help in identifying a arrow.
#3. we will scan for red colour i.e colour identification. For that we have to create a trackbar and set it values accordingly for colour we need

#Finally a frame having red colour arrow will be displayed by imshow function

#Lets start
import cv2             #importing opencv library
import os              #it is a module which provides functions for interacting with operating systems and change/identify a directory
import numpy as np     #for importing numpy

#1
vid = cv2.VideoCapture("videos/vid1.mp4")   #we are selecting a video under operation which has to be scanned for red arrow
currentframe = 0                            #it is variable, we will create a loop and change its values

if not os.path.exists('data'):
    os.makedirs('data')                     #we are making a directory where all frames of video will be stored, frames of a video are images

while (True):                               #we are creating a loop to extract frames from video
    success, frame = vid.read()

    cv2.imshow("Output", frame)
    cv2.imwrite('./data/frame' + str(currentframe) + '.jpg', frame)
    currentframe +=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCam.release()
cv2.destroyAllWindows()                    #frames have been successfully extracted

from os import listdir                     #listdir is used select all images/items from a folder


#2
for images in os.listdir(data): //         #created a loop to read all extracted frames (images) in repository
    img1 = cv2.imread(images)
    images1=[]                             #We will append all images with arrow here

    def getContours(img):                                                                     #We have inserted contours here, in leyman terms you can sort of boundary
        contours,hierarchy = cv2.find contours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContour, cnt, -1, (255, 0,0), 3)
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))

        if (len(approx)) == 7              #If there are 7 corners on perimeter then append that image in empty image variable
            images1.append(image)


#3
for imagess in images1:                   #creating a loop for all images we have appended or filtered out
                                          #We will be creating a trackbar with 3 variables in order to detect color
    cv2.namedWindow("TrackBars")                             #These values are to be changed after running so that only arrow part comes in white
    cv2.resizeWindow("TrackBars",640,240)
    cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
    cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
    cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
    cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
    cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

    img2 = cv2.imread(imagess)                            #After creating trackbar, we are reading images and will scan for red
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackBarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackBarPos("Hue Min", "TrackBars")
    s_min = cv2.getTrackBarPos("Hue Min", "TrackBars")
    s_max = cv2.getTrackBarPos("Hue Min", "TrackBars")
    v_min = cv2.getTrackBarPos("Hue Min", "TrackBars")
    v_max = cv2.getTrackBarPos("Hue Min", "TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)                      #Finally we will our show our videoframe which has red arrow
    cv2.waitKey(1)

  #End















