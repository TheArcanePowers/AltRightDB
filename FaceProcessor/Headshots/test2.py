# !/usr/bin/python3
import face_recognition
import os, glob

folder = "Charlottesville/"
os.chdir(folder)

# Load the jpg files into numpy arrays
dict = {}
for file in glob.glob("*.jpg"):
    filename = file.replace(".jpg","")
    dict[filename + "_image"] = face_recognition.load_image_file(file)

#biden_image = face_recognition.load_image_file("biden.jpg")
#obama_image = face_recognition.load_image_file("obama.jpg")
#unknown_image = face_recognition.load_image_file("obama2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    for file in glob.glob("*.jpg"):
        filename = file.replace(".jpg","")
        dict[filename + "_face_encoding"] = face_recognition.face_encodings(file)[0]

except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = []
for file in glob.glob("*.jpg"):
    filename = file.replace(".jpg","")
    known_faces.append(filename + "_face_encoding")

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
for file in glob.glob("*.jpg"):
    unknown_image = face_recognition.load_image_file(file)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print(results)

#print("Is the unknown face a picture of Biden? {}".format(results[0]))
#print("Is the unknown face a picture of Obama? {}".format(results[1]))
#print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
