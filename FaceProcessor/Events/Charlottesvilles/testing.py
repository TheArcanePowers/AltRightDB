# !/usr/bin/python3
import face_recognition
import subprocess
import os, glob


cmd = "face_recognition --tolerance 0.520 /known_faces "
deletedCounter = 0

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

print (finalCounter + " Unique faces.")


for filename in glob.glob("*.jpg"):
    command = str(cmd + filename)
    try:
        print ("Checking " + filename)
        print (command)
        returned_output = subprocess.check_output(command, shell=True)
    except Exception:
        returned_output = str(Exception.output)
    #finished = str(returned_output.split('\n'))
    #for line in finished:
    #    print (line)
    ## CLEAN THE THING
    returned_output = returned_output.decode("utf-8")
    if "no_persons_found" in returned_output:
        print ("No faces detected in " + filename)
        print ("Moving to manual check folder.")
        os.rename(filename+".jpg","MCheck/" + filename)
        continue
    if "unknown_person" in returned_output:
        print (filename + " is a unique face.")
    else:
        print (filename + "is a copy!")
        os.rename(filename, "Delete/" + filename)
