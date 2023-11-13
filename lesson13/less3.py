def convert(dict):
    spis = []
    for key in dict:
        spis.append(dict[key])
    return spis
print(convert({"adress": "Isanova 103", "floors": 7, "has_parking": True}))