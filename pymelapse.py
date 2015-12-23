import cv2
import time

writer = cv2.VideoWriter('output.avi', -1, 30, (640,480))
capture = cv2.VideoCapture(0)
capture_timer = 2.0 # seconds
frames = []

start_time = time.time()
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret==True:

        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= capture_timer:
            writer.write(frame)
            start_time = current_time

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
capture.release()
writer.release()
cv2.destroyAllWindows()
