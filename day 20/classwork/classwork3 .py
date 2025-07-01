animals = ["Dog", "Elephant", "Cat", "lion", "Fox", "Tiger"]

for animal in animals:
    if len(animal) < 5 and animal == animal.capitalize():
        print(animal[:3])
    else:
        print(f"{animal} გრძელია")