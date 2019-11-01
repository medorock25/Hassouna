phone_book = {1: ["ahmed","879869"], 2: ["ali","9698"] , 3: ["mai","8768768"]}

inp= input("Search by name: ")

for k,v in phone_book.items():
    if v in phone_book.items():
        print(k,v)
    else:
        print("No matches found")