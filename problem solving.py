name = input("Enter your name: ")
age = int(input("Enter your age: "))
amount = float(input("Enter your amount: "))
member = input("do u have membership id? (y/n) ").lower()

if age <= 0:
    print("Wrong age")

elif amount <= 0:
    print("Wrong amount")

else:
    if member == "y" and amount >= 2000:
        discount = amount * 0.15
        print(f"congrats! u have received 15% Discount {discount}")

    elif member == "y":
        discount = amount * 0.05
        print(f"congrats! u have received 5% Discount {discount}")

    elif member == "n" and amount >= 2000:
        discount = amount * 0.10
        print(f"congrats! u have received 10% Discount {discount}")

    else:
        discount = 0
        print("sorry! u do not have any discount")

    if age >= 60:
        extra = amount * 0.05
        discount = discount + extra
        print(f"senior citizen extra 5% Discount {extra}")

    total = amount - discount
    print(f"the payment is successful, you have to pay {total}")




