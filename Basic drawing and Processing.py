import cv2 as cv

img = cv.imread('PHOTOS/ex1.jpg')
cv.imshow('IMAGE', img)

#1. Rectangle
cv.rectangle(img, (0,0),(img.shape[1]//2, img.shape[0]//2),(0,255,0), thickness=-1)
cv.imshow('Rectangle', img)

#2. Circle
cv.circle(img,(150,150),60,(0,0,255), thickness = 3)
cv.imshow('Circle', img)

#3. Line
cv.line(img, (0,0),(250,250), (255,0,0), thickness=2)
cv.imshow('Line', img)

#4. Writing some text
cv.putText(img, 'Hi!, Welcome to OpenCV', (0,300), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255), thickness=2)
cv.imshow('Text', img)

#4.Resize and crop
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA) 

resized_image = rescaleFrame(img, scale=0.7)
cv.imshow('Image', resized_image)

cv.imwrite('output/resized_img.jpg', resized_image)

cv.waitKey(0)