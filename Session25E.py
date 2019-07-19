import cv2
import time
#import cv2, time
video = cv2.VideoCapture(0)

check, frame = video.read()
# It will return tuple check at 0 index and frame at index 1

print("==Check==")
print(check)
print("==Frame==")
print(frame)

# Sleep main thread for 3 seconds
time.sleep(3)

cv2.imshow("VideoCapture", frame)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()