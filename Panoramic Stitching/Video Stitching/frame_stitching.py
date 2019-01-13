# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

def stitch_frames(left_frame, right_frame):

    images = [left_frame, right_frame]

    # initialize OpenCV's image sticher object and then perform the image stitching
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    if status == 0:
        # Stitching Successful
        print("[INFO] image stitching Successful ({})".format(status))
        return stitched
    else:
        # Stitching Failed -- Likely not enough keypoints detected
        print("[INFO] image stitching failed ({})".format(status))
        # Return a black 3x3 image
        blank_frame = np.zeros((3,3,3), np.uint8)
        return blank_frame
