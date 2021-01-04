# !/usr/bin/python3
import cv2
import math
import face_recognition
import glob, os
from PIL import Image
import random
from imutils import paths
import argparse


OriginalCWD = os.getcwd()

print("-=-=-=-=MAIN=-=-=-=-")

os.chdir("Events")
eventname = input("What is the event?: ").replace(" ", "")

try:
    os.makedirs(eventname)
    print("Creating folder...")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
    print("Folder already exists, working inside that")
    
os.chdir(eventname)
os.mkdir("tmp")

print("-=-=Generating frames=-=-")

os.chdir(OriginalCWD)

videoFile = "input.mp4"
imagesFolder = OriginalCWD + "/Events/"+eventname+"/tmp"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()


print ("-=-=Recognising Faces=-=-")
os.chdir(OriginalCWD + "/Events/"+eventname)
os.mkdir("faces")
os.chdir(OriginalCWD + "/Events/"+eventname+"/tmp")
NofFaces = 0


for file in glob.glob("image_*.jpg"):
    #print ("Recognising faces on file: " + file)
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) > 0:
        #print (str(len(face_locations)) + " Face(s) recognised.")
        NofFaces = NofFaces + (int(len(face_locations))
        img = Image.open(file)
        for face in face_locations:
            #get top left and bottom right
            topRH, topRW, btLH, btLW = face
            #so u see more than just the face, eg hair etc
            btLW = btLW - 200
            topRH = topRH - 200
            topRW = topRW + 200
            btLH = btLH + 200
            Dimensions = tuple((btLW,topRH,topRW,btLH))
            img2 = img.crop(Dimensions)

            word_file = "/usr/share/dict/words"
            WORDS = open(word_file).read().splitlines()
            fileName = str(random.choice(WORDS) + random.choice(WORDS))
            fileName = fileName.replace("'s", "")
            os.chdir(OriginalCWD + "/Events/"+eventname+"/faces")
            img2.save(fileName + ".jpg")
            os.chdir(OriginalCWD + "/Events/"+eventname+"/tmp")
            #print("Saved " + fileName)
    else:
        #print ("No faces recognised.")
    #print(file + " deleted.")
    os.remove(file)
os.chdir(OriginalCWD + "/Events/"+eventname)
os.rmdir("tmp")
os.chdir(OriginalCWD + "/Events/"+eventname+"/faces")

print("-=-=Cleaning=-=-")

Nremoved = 0
#total = 0

for file in glob.glob("*.jpg"):
    #total = total + 1
    im = Image.open(file)
    x, y = im.size
    if x < 150 and y < 150:
        #print(file + " is too small")
        os.remove(file)
        Nremoved = Nremoved + 1

print (str(Nremoved) + "  small pictures removed.")
#print (str(total) + " pictures analysed for size in total.")

#############################################

Nremoved = 0
#total = 0

for file in glob.glob("*.jpg"):
    #total = total + 1
    #cv2.Laplacian(file, cv2.CV_64F).var()
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < 70:
        os.remove(file)
        Nremoved = Nremoved + 1

print (str(Nremoved) + "  blurry pictures removed.")
#print (str(total) + " pictures analysed for blur in total.")

print("-=-=Checking for dupes=-=- (warning takes long af)")
deletedCounter = 0
os.mkdir(OriginalCWD + "/Events/"+eventname+"/known_faces")

for file in glob.glob("*.jpg"):
    image = face_recognition.load_image_file(file)
    ###check if first run
    if len(os.listdir(OriginalCWD + "/Events/"+eventname+"/known_faces") ) == 0:
        print("First run")
        try face_locations = face_recognition.face_locations(image):
            os.rename(file, "/known_faces/"+file)
        except:
            print("Face not recognised")
            os.remove(file)
            break   
    try recognising face:
        if face = any known faces:
            delete face
            continue
        else:
            move face into known faces
    exception:
        delete face
        deletedCounter = deletedCounter + 1

print(deletedCounter + " unrecognised faces")
change working directory
finalCounter = 0

for file:
    finalCounter = finalCounter + 1

print (finalCounter + " Unique faces.")
    
