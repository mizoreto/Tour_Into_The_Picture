import argparse
import cv2
import numpy as np
from inpainter import Inpainter

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path input image on which we'll perform inpainting")
ap.add_argument("--x", type=str, required=True,
	help="startingPoint_x of mask which corresponds to foreground areas")
ap.add_argument("--y", type=str, required=True,
	help="startingPoint_y of mask which corresponds to foreground areas")
ap.add_argument("--w", type=str, required=True,
	help="width of mask which corresponds to foreground areas")
ap.add_argument("--h", type=str, required=True,
	help="height of mask which corresponds to foreground areas")
ap.add_argument("--patch_size", type=str, required=True,
	help="patch size")

ap.add_argument("-a", "--method", type=str, default="telea",
	choices=["telea", "ns"],
	help="inpainting algorithm to use")
ap.add_argument("-r", "--radius", type=int, default=3,
	help="inpainting radius")
args = vars(ap.parse_args())

# initialize the inpainting algorithm to be the Telea et al. method
flags = cv2.INPAINT_TELEA
# check to see if we should be using the Navier-Stokes (i.e., Bertalmio
# et al.) method for inpainting
if args["method"] == "ns":
	flags = cv2.INPAINT_NS

image = cv2.imread(args["image"])
mask = np.zeros(image.shape[:2],np.uint8)
x = int(args["x"])
y = int(args["y"])
w = int(args["w"])
h = int(args["h"])
patch_size = int(args["patch_size"])
mask[x:x+w, y:y+h] = 1

# perform inpainting
output = Inpainter(
        image,
        mask,
        patch_size,
        False
    ).inpaint()
foreground = image[x:x+w, y:y+h]
file_back = "background.jpg"
file_fore = "foreground.jpg"
cv2.imwrite(file_back, output)
cv2.imwrite(file_fore, foreground)
