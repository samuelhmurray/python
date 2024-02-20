my_family = {
    "brother": {"name": "Haskell", "age": 43},
    "sister": {"name": "Babs", "age": 38},
    "mother": {"name": "Vicy", "age": 70},
    "Father": {"name": "Chip", "age": 70},
}
for member, details in my_family.items():
    name = details["name"]
    age = details["age"]
    print(f"{name} is my {member} and is {str(age)} years old")
