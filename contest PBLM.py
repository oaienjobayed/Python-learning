numbers = []
n = int(input("How many number : "))

if n < 1 or n > 20:
    print("Invalid n")
    exit()

for count in range(1, n + 1):
    num = int(input(f"{count} number: "))
    numbers.append(num)

print("List:", numbers)

# বড় আর ছোট
print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# যোগফল আর গড়
total = sum(numbers)
average = total / n
print(f"Sum: {total}, Average: {average:.2f}")

# জোড়-বিজোড় আর ধনাত্মক-ঋণাত্মক গোনা
even = 0
odd = 0
positive = 0
negative = 0
zero = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

print(f"Even: {even}, Odd: {odd}")
print(f"Positive: {positive}, Negative: {negative}, Zero: {zero}")





