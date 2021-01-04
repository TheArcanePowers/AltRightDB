# !/usr/bin/python3
from PIL import Image
import face_recognition
import glob, os

#folder = input("folder name (with trailing slash): ")
folder = "Charlottesville/"
os.chdir(folder)

for file in glob.glob("*.jpg"):
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(file)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) > 0:
        pass
    else:
        print("No faces detected in " + file)
        os.remove(file)

global file

#for file in glob.glob("*.jpg"):
    print ("(main) scanning " + file)
    picture_of_me = face_recognition.load_image_file(file)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    for pic in glob.glob("*.jpg"):
        print ("scanning " + pic)
        if pic == file:
            pass
        unknown_picture = face_recognition.load_image_file(pic)
        if len(unknown_picture) > 0:
            print (unknown_picture)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)


            if results[0] == True:
                print("It's a picture of me!")
                #os.remove(pic)
            else:
                print("It's not a picture of me!")
