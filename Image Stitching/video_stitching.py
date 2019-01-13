import numpy as np
import cv2
from frame_stitching import stitch_frames

cap1 = cv2.VideoCapture('school - left.mp4')
cap2 = cv2.VideoCapture('school - right.mp4')

'''
# Get Frame Size + FPS for current videos
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
framesize = (width, height)

# fourcc = cv2.VideoWriter_fourcc(*'H264')    #AVC1
# VideoWriter(output file name, fourcc code, fps, frame size)
out = cv2.VideoWriter('output.mp4', -1, fps, framesize)
'''

framesize = (1920, 1080)
fps = 30
out = cv2.VideoWriter('output.mp4', -1, fps, framesize)

while(cap1.isOpened() and cap2.isOpened()):
    ret_1, frame_1 = cap1.read()
    ret_2, frame_2 = cap2.read()

    if ret_1==True and ret_2==True:

        frame = stitch_frames(frame_1, frame_2)
        (height, width) = frame.shape[:2]

        if width > framesize[0] or height > framesize[1]:
            print("[INFO] stitched image too large: ({}, {})".format(height, width))
            frame = np.zeros((3,3,3), np.uint8)
            height = 3
            width = 3

        # add padding to stitched images so that video size is constant
        pad_top = 0
        pad_bottom = framesize[1] - height
        pad_left = 0
        pad_right = framesize[0] - width
        frame = cv2.copyMakeBorder(frame, pad_top, pad_bottom, pad_left, pad_right,
                                    cv2.BORDER_CONSTANT, 0)

        # add frame to output video
        out.write(frame)

    else:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
