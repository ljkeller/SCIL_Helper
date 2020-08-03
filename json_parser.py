import json

def read_names(fptr):
    with open(fptr) as f:
        data = json.load(f)
        return data

d = read_names('sub_list.json')
print(d)
