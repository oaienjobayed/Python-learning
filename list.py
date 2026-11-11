names = []
n = int(input("how many people name you want to add?"))

count = 1
while count <= n:
    name=input(f"{count} number name: ")
    names.append(name)
    count = count + 1

search = input("Find your name: ")

found = False
i = 0
while i<len(names):
    if names[i] == search:
        print(f"{search} is exit. in {i+1} no place")
        found = True
    i = i + 1

if found == False:
    print(f"{search} is not found.")