age = int(input("old: "))
class_type = int(input("class (1/2): "))

if age <= 0:
    print("wrong old")
else:
    if class_type == 1:
        fare = 500
    elif class_type == 2:
        fare = 1200
    else:
        fare = None
        print("wrong class")

    if fare is not None:
        if age < 12:
            fare = fare / 2
        elif age >= 60:
            fare = fare * 0.80
        print(f"ur fear: {fare:.2f} tk")



#new problem
name = "oaien"
has_money = input("how much money do you have? (yes/no) ")

if has_money == "yes":
    items = "fish and tomato"
    print(f"{name} will buy {items}")
else:
    print(f"{name} can not buy fish and tomato")

#another problem
operator = input("select ur sim? (gp/robi) ")
amount = int(input("enter ur recharge amount: "))

if operator == "gp" or operator == "robi":
    if amount < 10:
        print("minimum recharge 10 tk")
    elif amount <= 500:
        print("your recharge amount is successful!")
        if operator == "gp" and amount >= 100:
            bonus = amount * 0.05
            print(f"you get {bonus} tk bonus")
    else:
        print("maximum recharge 500 tk")
else:
    print("invalid sim operator")


