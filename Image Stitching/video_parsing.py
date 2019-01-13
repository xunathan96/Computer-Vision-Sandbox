import numpy as np
import cv2

cap = cv2.VideoCapture('kathy.mp4')

# Get Frame Size + FPS for current video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
framesize = (width, height)

# fourcc = cv2.VideoWriter_fourcc(*'H264')    #AVC1
# VideoWriter(output file name, fourcc code, fps, frame size)
out = cv2.VideoWriter('output.mp4', -1, fps, framesize)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', gray)

        # add frame to output video
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
