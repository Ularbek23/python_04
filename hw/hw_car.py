def cars(name, mark, **kwargs):
    slovar = {
        "name": name,
        "mark": mark,
    }
    slovar.update(kwargs)
    return slovar




print(cars("subaru", "outback", color="blue", engine="V8"))