import json

def email_map_from_file(fptr):
    d_map = dict()
    with open(fptr) as f:
        data = json.load(f)
        for entry in data:
            if entry['name'].lower() in d_map:
                d_map[entry['name'].lower()].append(entry['email'].lower())
            else:
                d_map[entry['name'].lower()] = [entry['email'].lower()]
        return d_map

d = email_map_from_file('sub_list.json')
