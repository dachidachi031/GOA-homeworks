mixed_list = ["dachi", 123, True, "hello", 4.5, "world", None]

for item in mixed_list:
    if type(item) == str:
        upper_str = item.upper()
        print(upper_str[-3:])