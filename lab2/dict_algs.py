def check_childrens(el):
    for child in el["children"]:
        if child["age"] > 18:
            return True
    return False


if __name__ == "__main__":
    # Дано
    ivan = {
        "name": "darja",
        "age": 34,
        "children": [{
            "name": "vasja",
            "age": 12,
        }, {
            "name": "petja",
            "age": 10,
        }],
    }

    darja = {
        "name": "darja",
        "age": 41,
        "children": [{
            "name": "kirill",
            "age": 21,
        }, {
            "name": "pavel",
            "age": 15,
        }],
    }
    emps = [ivan, darja]

    for i in emps:
        if check_childrens(i):
            print(i["name"])
