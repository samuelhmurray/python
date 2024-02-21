class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Alf", 10)
dog2 = Dog("sam", 1)

print(dog2.name)
