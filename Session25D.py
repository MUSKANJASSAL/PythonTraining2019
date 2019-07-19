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

video.release()
cv2.destroyAllWindows()

"""
CV2: “[ WARN:0] terminating async callback” when attempting to take a picture

It's probably showing a warning because you're not releasing the handle to the webcam.
Try adding this to the end of the code

camera.release()
cv2.destroyAllWindows()
"""