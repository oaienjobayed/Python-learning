age = int(input("বয়স: "))
class_type = int(input("শ্রেণি (1/2): "))

if age <= 0:
    print("ভুল বয়স")
else:
    if class_type == 1:
        fare = 500
    elif class_type == 2:
        fare = 1200
    else:
        fare = None
        print("ভুল শ্রেণি")

    if fare is not None:
        if age < 12:
            fare = fare / 2
        elif age >= 60:
            fare = fare * 0.80
        print(f"আপনার ভাড়া: {fare:.2f} টাকা")