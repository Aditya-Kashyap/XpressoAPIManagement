import json

# if file.endswith('.json'):
from flask import jsonify


def load_json(json_file):
    """
    Load the JSON
    Returns:

    """
    with open(json_file, 'r') as f:
        json_dict = json.load(f)
        print(json_dict)
        return json_dict


# dict_obj = json.load("json_dijsct.json")
# print(dict)

def load_remove_json(json_file, key_name: str):
    """
    Load the JSON
    Args:
        json_file:
        key_name (object):

    Returns:

    """
    with open(json_file, 'r') as f:
        print(type(f))
        json_dict = json.load(f)
        print(type(json_dict))
        print(f'Original JSON:{json_dict}')
        updated_json = remove_attribute_json(json_dict, key_name)
        # print(f'Updated JSON:{quarks}')
    return updated_json


# dict_obj = json.load("json_dijsct.json")
# print(dict)

def remove_attribute_json(json_dict, name: str):
    """

    Args:
        json_dict:
        name: str->name of the attribute

    Returns:

    """
    print(type(json_dict))
    for i, q in enumerate(json_dict):
        if q['name'] == name:
            del json_dict[i]
    print(f'Updated JSON:{json_dict}')
    print(type(json_dict))
    return json_dict
    # return jsonify({'quarks': json_dict})


if __name__ == '__main__':
    # json_output = load_json("quarks.json")
    attribute_name = 'up'
    json_output = load_remove_json("quarks.json", attribute_name)
