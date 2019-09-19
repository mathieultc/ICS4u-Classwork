
import json

'''

#writing to a dictionary to a file

some_dict = {
    "name":"John",
    "color":"blue",
    "over 18": False

}

#Write json string to a file in one line instead of multiplelines
with open ("data.json","w") as f:
    json.dump(some_dict,f)
'''
'''
# Loading a dictionary from a file as a dictionary type data
with open("data.json","r") as f:
    data = json.load(f)

print(data)
print(type(data))

data["name"] = "alex"

with open("data.json","w") as f:
    json.dump(data,f)
'''
#nested dictionries
data = {
    "students":[
        {"name":"john"},
        {"name": "alex"}
    ],
    "classroom" :[
        {"course_code":"ICS4U"}
    ]

}

with open("markbook.json","w") as f:
    json.dump(data,f)
