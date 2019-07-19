import cv2

img = cv2.imread("ibises.jpg", 0)

shape = img.shape
print(shape)
# resizedImg = cv2.resize(img, (shape[0]//2, shape[1]//2))
resizedImg = cv2.resize(img, (400,400))

cv2.imshow("Title", resizedImg)

cv2.imwrite("MyIbises.jpg", resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()