# !/usr/bin/python3
import subprocess
import os, glob

cmd = "face_recognition --tolerance 0.520 /known_faces "
Fcmd= "date"

os.chdir("Charlottesville/")

faces = []

for filename in glob.glob("*.jpg"):
    command = str(cmd + filename)
    try:
    #print ("Checking " + filename)
    #print (command)
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
