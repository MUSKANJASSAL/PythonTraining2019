import cv2

print(cv2.__version__)

img = cv2.imread("ibises.jpg", 0)
# 1 means Read as Coloured Image, 0 as Black/White

print("==========Image==========")
print(img)

print("==========Type of Image==========")
print(type(img))  # ;)

print("==========Image Shape==========")
print(img.shape)   # Resolution

print("==========Image 0th Index==========")
print(img[0])

print("==========Image Shape 0th Index==========")
print(img[0].shape)

print("==========Image Length 0th Index==========")
print(len(img[0]))