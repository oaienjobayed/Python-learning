#ছোট প্রজেক্ট: ক্যালকুলেটর
def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    if b == 0:
        return "Divide by 0 not possible"
    return a/b

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

print(add(x,y))
print(subtract(x,y))
print(multiply(x,y))
print(divide(x,y))

#list নিয়ে function
def total(numbers):
    t = 0
    for n in numbers:
        t = t + n
    return t

def average(numbers):
    return total(numbers) / len(numbers)

marks = [70, 80, 90]
print(average(marks))
print(total(marks))

#একাধিক মান ফেরত
def min_max(numbers):
    return min(numbers), max(numbers)
small, big = min_max([3, 5, 1])
print(small, big)

#Keyword argument
def info(name, age):
    print(f"{name}, {age} বছর")

info(age=20, name="Rahim") # Rahim 20 বছর

#Default value
def greet (name, msg = "Hello"):
    print(f"{msg}, {name}")

greet("Rahim")
greet("Rahim", "Welcome")

#শর্তসহ function
def get_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "F"

print(get_grade(85))    # A+
print(get_grade(65))    # B

#even
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False


#return: ফলাফল ফেরত দেওয়া
#print শুধু পর্দায় দেখায়। return ফলাফল ফেরত দেয়, যাতে পরে ব্যবহার করা যায়।
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)    # 5 ছাপে, কিন্তু x এ থাকে None (কিছু নেই)
y = add_return(2, 3)   # কিছু ছাপে না, y এ থাকে 5