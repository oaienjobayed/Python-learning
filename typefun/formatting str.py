#type function
print(type(10))
print(type("hello"))
print(type(1.1))
print(type(True))
print(type([1,2]))

age=20
print(type(age))

name = "Jobayed"
print(type(name))

#formatting string
num1 = 10
num2 = 20
print (f"{num1} {num2} = {num1+num2}")

name = "oaien"
address = "chittagong"
print(f'name : {name} address : {address}') #if u want then u write extra one more line for
                                             #formating address it's up to u


name = "rahim"
age = 20
cgpa = 3.7622222
print(f'name : {name} age : {age} cgpa : {cgpa:.2f}')



name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print(f"{name}, my age is {age} years old")