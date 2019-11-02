cool = {'floor': [0,1,2,3,4,5]}
position = cool.values()
target = int(input("Enter a number: "))


for position in cool.values():
    while position != target:
        print("going to {}".format(target))
        if position == target:
            print("stay")

