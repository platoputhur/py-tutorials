class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print("My name is " + self.name + " and I am " + str(self.age) + " years old. I live at " + self.address)


mike = Person(
    name="Mike", age=24, address="Avenue Street, KL, IN"
)
print(mike.name)
# mike.introduce()

sakura = Person(
    name="Sakura", age=42, address="Avenue Street, KO, KP"
)
print(sakura.name)