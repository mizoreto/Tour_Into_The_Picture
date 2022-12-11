# CS445_Tour_Into_The_Picture

## Overview
This is the final project for CS445: Computational Photography at UIUC.

Our project, Tour Into The Picture, implements the techniques described in [Tour Into the Picture](http://graphics.cs.cmu.edu/courses/15-463/2011_fall/Papers/TIP.pdf) by Horry et al., reconstructing a 3D model from a single point perspective 2D image.


Team Member:\
Cheung Yau Shing Jonathan (ysc7)\
Yu Bu (yubu2)\
Jiayin Meng (jiayinm2)

## Approach

## Results

## Directories

## How to Use
### Get the background and foreground images
Inside the project's directory run:
```
python texture_synthesis.py -i <path to image> --x <starting point X of the mask> --y <starting point Y of the mask> --w <width of the mask> --h <height of the mask> --patch_size <patch size for inpainter>
```
You would get two files named as `background.jpg` and `foreground.jpg`.

Then run:
```
python foreground_extraction.py -i foreground.jpg
```
to get the foreground object `foreground_clean.jpg`.
