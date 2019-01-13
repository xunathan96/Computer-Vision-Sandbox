# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# images_file is path to file that contains all images to stitch
# output_file is a path to where the stitched image is saved
images_file = "input_images"
output_file = "output_images/out.png"

args = {}
args["images"] = images_file
args["output"] = output_file

print("[INFO] loading images...")
# grab the paths to the input images and initialize our images list

images_list = list(paths.list_images(args["images"]))
imagePaths = sorted(images_list)
images = []

# load each image using openCV, and add them to images list
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)

# initialize OpenCV's image sticher object and then perform the image
# stitching
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

# Stitching Successful
if status == 0:
	# write the output stitched image to disk
	cv2.imwrite(args["output"], stitched)

# Stitching Failed -- Likely not enough keypoints detected
else:
	print("[INFO] image stitching failed ({})".format(status))
