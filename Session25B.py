import cv2

img = cv2.imread("ibises.jpg", 1)
cv2.imshow("Title", img)

# We are not waiting for any time interval
# User will press any key on keyboard and we will quit the program
cv2.waitKey(0)

# Quit after 3 seconds
# cv2.waitKey(3000)

cv2.destroyAllWindows()

# Assignment: Rotate Numpy Array 180, 90(clockwise) degrees and show it as an image