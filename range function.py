#১. range(stop)
for i in range (4):
    print (i)

#২. range(start, stop)
for i in range (1,6):
    print (i)

#৩. range(start, stop, step)
for i in range (0, 10, 2):
    print (i)

#উল্টো গুনতে
for i in range (10, 0, -1):
    print (i)

"""
## while
i = 1
while i <= 5:
    print(i)
    i += 1
"""
# for + range (একই কাজ)
for i in range(1, 6):
    print(i)

"""
#আগে:
numbers = []
n=4
count = 1
while count <= n:
    num = int(input(f"{count} নম্বর সংখ্যা: "))
    numbers.append(num)
    count += 1
"""
#এখন:
n = 4
numbers = []
for count in range(1, n + 1):
    num = int(input(f"{count} নম্বর সংখ্যা: "))
    numbers.append(num)


"""""
##easy way te solved
found = False

for i in range(len(names)):
    if names[i] == search:
        print(f"{search} পাওয়া গেছে, {i + 1} নম্বরে")
        found = True

if found == False:
    print(f"{search} পাওয়া যায়নি")
"""""