person: dict = {
    "name": "Mark",
    "age": 56,
}
person["weight"] = 78.0
person["age"] = 45
print(list(person.keys()))
print(tuple(person.values()))
