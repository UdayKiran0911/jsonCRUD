import json
import os

filepath = "<File Absolute(Full) Location>"

def isfileemtpy(filepath):
    if os.stat(filepath).st_size > 0:
        return False
    else:
        return True

def iskeyexist(data, keyval):
    if keyval in data.keys():
        return True
    else:
        return False

def jsonwriter(jsd):
    with open(filepath,"a+") as f:
        if not isfileemtpy(filepath):
            jfile = jsonreader(filepath)
            jfile.update(jsd)
            f.truncate(0)
            f.write(json.dumps(jfile, indent=2, sort_keys=True))
        else:
            f.write(json.dumps(jsd, indent=2, sort_keys=True))

# Updaete takes a list as argument with three values ["id", "key", "value"]
def jsonupdate(d_list):
    with open(filepath,"r+") as f:
        if not isfileemtpy(filepath):            
            jfile = json.load(f)
            if iskeyexist(jfile, d_list[0]):
                jfile[d_list[0]][d_list[1]] = d_list[2]
                f.seek(0)
                f.write(json.dumps(jfile, indent=2, sort_keys=True))
                f.truncate()
            else:
                print("Key Not Found")
        else:
            print("File is Empty")

def jsonreader(filepath):
    with open(filepath,"r+") as f:
        if not isfileemtpy(filepath):                
            f.seek(0)
            return json.load(f)
        else:
            print("File is Empty")
