  #type 1
names = ["ab", "cd", "ef"]
for name in names:
    print(name)

    #type 2
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

   #type 3
numbers =[11, 22, 33, 44, 55]
total = 0

for num in numbers:
    total = total + num
    print(total)

    #type 4
names = ["ab", "cd", "ef"]
search = "ab"

found = False
for name in names:
    if search == name:
        found = True

    if found:
        print(f"{search} is found.")
    else:
        print(f"{search} is not found.")

