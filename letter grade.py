# ### letter grade
# marks = 85
#
# if marks >= 80:
#     grade = "A+"
#     gpa = 5.0
# elif marks >= 70:
#       grade = "A"
#       gpa = 4.0
# else:
#     grade = "B"
#     gpa = 3.0
#
# print(f"grade is {grade}, GPA is {gpa}")
#
# ###while loop
#
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
#
# n = 2
# i = 1
# while i <= 5:
#     print(f"{n} x {i} = {n * i}")
#     i += 1
#
#
# ###break use
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     print(f"The number is {num}")
#     print("End")

###sum of n number
# n = int(input("Enter a number: "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 1
# print(total)

###password varification

password = input("পাসওয়ার্ড: ")
attempts = 1

while password != "1234" and attempts < 3:
    print("wrong password, u can try 2 time only")
    password = input("পাসওয়ার্ড: ")
    attempts = attempts + 1

if password == "1234":
    print("লগইন সফল ✅")
else:
    print("wrong password, আপনার 3 বার চেষ্টা শেষ")
