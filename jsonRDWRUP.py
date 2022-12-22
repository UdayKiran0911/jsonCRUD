import json
import os

a = { 
"3": {"name": "Mesone","age": 21,"address": { "street": "1 Main Street", "city": "Los Angeles", "zipcode": 90001},"married": False},
}

x = { 
"1": {"name": "Jsone","age": 21,"address": { "street": "1 Main Street", "city": "Los Angeles", "zipcode": 90001},"married": False},
"2":{"name": "Kimberly","age": 36,"address": { "street": "2 subway road", "city": "Delhi", "zipcode": 500001},"married": True},
"3":{"name": "Lily","age": 16,"address": { "street": "7th Avenu, street 9", "city": "Hyderabad", "zipcode": 500011},"married": False},
}

z = { 
"7": {"name": "Jsone","age": 21,"address": { "street": "1 Main Street", "city": "Los Angeles", "zipcode": 90001},"married": False},
"8":{"name": "Kimberly","age": 36,"address": { "street": "2 subway road", "city": "Delhi", "zipcode": 500001},"married": True},
"9":{"name": "Lily","age": 16,"address": { "street": "7th Avenu, street 9", "city": "Hyderabad", "zipcode": 500011},"married": False},
}

y = { 
"4": {"name": "Mesone","age": 21,"address": { "street": "1 Main Street", "city": "Los Angeles", "zipcode": 90001},"married": False},
}

filepath = "C:\\Users\\UyBodala\\OneDrive - SkillSoft Corporation\MyDocuments\\Python Supporting Scripts\\jsonfile.json"

# Check if the file is empty, if the file size is not 0, the function will return False, if 0 will return True
def isfileemtpy(filepath):
    if os.stat(filepath).st_size > 0:
        return False
    else:
        return True

# Check if the key exist or not, if key is found the function will return True, else will return False
def iskeyexist(data, keyval):
    if keyval in data.keys():
        return True
    else:
        return False

# the function will write the dictionary into a json file.
# it will also check for the emptiness of the file, if the file is not empty, it will check if the key already exist,
# if it does not exist only then it will be added.
def jsonwriter(jsd, filepath):
    with open(filepath,"a+") as f:
        if not isfileemtpy(filepath):
            jfile = jsonreader(filepath)
            for datakey in jsd.keys():
                if not iskeyexist(jfile, datakey):
                    jfile.update(jsd)
                    f.truncate(0)
                    f.write(json.dumps(jfile, indent=2, sort_keys=True))
            else:
                print(f"Key {datakey} Already Exist")
        else:
            f.write(json.dumps(jsd, indent=2, sort_keys=True))

# the function will update the existing values for existing keys
# if the key is not found or the file is empty,
# it will raise "Key Not Found" and "File is Empty" message respectively and accordingly.
def jsonupdate(d_list, filepath):
    with open(filepath,"r+") as f:
        if not isfileemtpy(filepath):            
            jfile = json.load(f)
            if iskeyexist(jfile, d_list[0]):
                jfile[d_list[0]][d_list[1]] = d_list[2]
                f.seek(0)
                f.write(json.dumps(jfile, indent=2, sort_keys=True))
                f.truncate()
            else:
                print(f"Key {d_list[0]} Not Found")
        else:
            print("File is Empty")

# the function is for deleting the values based on key, if the key is not found or the file is empty,
# it will raise "Key Not Found" and "File is Empty" message respectively and accordingly.
def jsondelete(id, filepath):
    if not isfileemtpy(filepath):
        with open(filepath,"a+") as f:
            f.seek(0)
            jfile = json.load(f)
            if iskeyexist(jfile, id):
                del jfile[id]
                f.truncate(0)
                f.write(json.dumps(jfile, indent=2, sort_keys=True))
            else:
                print(f"Key {id} Not Found")
    else:
        print("File is Empty")

# the function is for reading the json file, it will check for file emptiness, if empty will raise "File is Empty" message
def jsonreader(filepath):
    with open(filepath,"r+") as f:
        if not isfileemtpy(filepath):                
            f.seek(0)
            return json.load(f)
        else:
            print("File is Empty")
            
# Examples
jsonupdate(["3", "name", "Albatros"], filepath)
jsonwriter(x, filepath)
jsonwriter(y, filepath)
jsonwriter(a, filepath)
jsonupdate(["3", "name", "Albatros"], filepath)
jsondelete("3", filepath)
jsondelete("2", filepath)
jsondelete("6", filepath)
jsondelete("1", filepath)
jsonwriter(z, filepath)
jsonupdate(["1", "name", "Albatros"], filepath)
jsonupdate(["7", "name", "Albatros"], filepath)
jsonupdate(["9", "married", True], filepath)
jsonreader(filepath)
