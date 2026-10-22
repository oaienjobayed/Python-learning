# marks = 87
#
# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("A-")
# elif marks >= 50:
#     print("B")
# elif marks >= 40:
#     print("C")
# else:
#     print("fail")


# marks = int(input("Enter your marks: "))
#
# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("A-")
# elif marks >= 50:
#     print("B")
# elif marks >= 40:
#     print("C")
# else:
#     print("fail")

#explore new problem
total = float (input ("how much ur total bill ?"))

if total >= 1000:
    discount = total * 0.10
    print(f"congress! u got 10% discount {discount}")
    total = total - discount
else:
    print("sorry! u do not have any discount")

print(f"you give me {total}")

#another problem
age = int (input ("how old are you?"))
has_ticket = input ("do u have a ticket? (y/n)")

if age >= 18 and has_ticket == "y":
    print("you are eligible")
elif has_ticket != "y":
    print("buy a ticket first")
else:
    print("sorry! ur age is under 18")
