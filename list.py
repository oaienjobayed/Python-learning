numbers = []
even = []
odd = []

n = int(input("how many number: "))

count = 1
while count <= n:
    num = int(input(f"{count} number value: "))
    numbers.append(num)
    count += 1

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
    i = i + 1              # ঠিক: loop-এর ভেতরে, if/else-এর বাইরে (৪ space)

print(numbers)             # ঠিক: loop-এর বাইরে (০ space)
print(even)
print(odd)
print(sum(even))