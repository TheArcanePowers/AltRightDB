# !/usr/bin/python3
import face_recognition
import glob, os
from PIL import Image
import random

os.chdir("tmp/")


for file in glob.glob("*.jpg"):
    print ("Recognising faces on file: " + file)
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) > 0:
        print (str(len(face_locations)) + " Face(s) recognised.")
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
            os.chdir("/home/arcane/Desktop/AltRightDB/Headshots/")
            img2.save(fileName + ".jpg")
            os.chdir("/home/arcane/Desktop/AltRightDB/Videos/tmp/")
            print("Saved " + fileName)
    else:
        print ("No faces recognised.")
    print(file + " deleted.")
    os.remove(file)
