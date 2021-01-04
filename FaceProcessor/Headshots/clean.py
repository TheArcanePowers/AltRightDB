# !/usr/bin/python3
import glob, os
from PIL import Image

Nremoved = 0
total = 0

for file in glob.glob("*.jpg"):
	total = total + 1
	im = Image.open(file)
	x, y = im.size
	if x < 150 and y < 150:
		#print(file + " is too small")
		os.remove(file)
		Nremoved = Nremoved + 1

print (str(Nremoved) + "  small pictures removed.")
print (str(total) + " pictures analysed for size in total.")

#############################################

# import the necessary packages
from imutils import paths
import argparse
import cv2
import shutil

Nremoved = 0
total = 0

for file in glob.glob("*.jpg"):
	total = total + 1
	#cv2.Laplacian(file, cv2.CV_64F).var()
	image = cv2.imread(file)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = cv2.Laplacian(gray, cv2.CV_64F).var()
	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	if fm < 80:
		shutil.move(file, "Blurry/")
		Nremoved = Nremoved + 1

print (str(Nremoved) + "  blurry pictures moved.")
print (str(total) + " pictures analysed for blur in total.")
