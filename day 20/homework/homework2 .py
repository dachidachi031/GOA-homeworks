name = "DACHI"

has_upper = False

for letter in name:
    if letter.isupper():
        has_upper = True
        break

if has_upper:
    print(name.lower())
else:
    print(name.capitalize())