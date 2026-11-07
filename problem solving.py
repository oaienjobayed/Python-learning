balance = 10000
attempts = 0
transactions = 0
total_withdrawn = 0

password = input("password: ")

while password != "1234" and attempts < 2:
    attempts = attempts + 1
    print(f"wrong password! you can try {3 - attempts - 1} more times")
    password = input("password: ")

if password != "1234":
    print("wrong password! your acc is blocked")
    exit()

print("login successful")

while True:
    print("\n1. check balance")
    print("2. withdraw money")
    print("3. cash in")
    print("4. exit")

    choice = input("your choice (1/4): ")

    if choice == "1":
        print(f"your balance is {balance}")

    elif choice == "2":
        amount = int(input("enter amount: "))
        if amount <= 0:
            print("wrong amount, give the correct amount")
        elif amount % 500 != 0:
            print("you can only withdraw multiples of 500")
        elif amount > 5000:
            print("you cannot withdraw more than 5000")
        elif amount > balance:
            print("you do not have enough money")
        else:
            balance = balance - amount
            transactions += 1
            total_withdrawn += amount
            print(f"withdraw successful! new balance is {balance}")

    elif choice == "3":
        amount = int(input("enter amount: "))
        if amount <= 0:
            print("wrong amount, give the correct amount")
        else:
            balance = balance + amount
            transactions += 1
            print(f"{amount} cash in successfully")

    elif choice == "4":
        print("Thank you!")
        print(f"total transactions: {transactions}")
        print(f"total withdrawn: {total_withdrawn} tk")
        break

    else:
        print("wrong choice, select from 1-4")










