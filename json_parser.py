import json

def email_map_from_file(fptr):
    d_map = dict()
    with open(fptr) as f:
        data = json.load(f)
        for entry in data:
            d_map[entry['email']] = entry['name']
        return d_map

d = email_map_from_file('sub_list.json')
