import json

def load_crop_data():
    with open("data/crops.json", "r") as file:
        return json.load(file)

def get_crop(name):
    data = load_crop_data()

    if name.lower() not in data:
        return None

    crop = data[name.lower()]
    return crop