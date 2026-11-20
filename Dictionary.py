#কেন দরকার?
#list দিয়ে একজন ছাত্রের তথ্য:
student = ["Rahim", 20, 3.75]
print(student[0])    # Rahim (0 মানে কী? মনে রাখতে হয়)

#dictionary দিয়ে:
student = {"name": "Rahim", "age": 20, "cgpa": 3.75}
print(student["name"])    # Rahim (নাম দেখেই বোঝা যায়)

# যোগ করা আর বদলানো
student = {"name": "Rahim", "age": 20}

student["city"] = "Chattogram"   # নতুন key যোগ
student["age"] = 21              # পুরনো key-র মান বদল

print(student)
# {'name': 'Rahim', 'age': 21, 'city': 'Chattogram'}

#মোছা
student = {"name": "Rahim", "age": 20, "city": "Ctg"}

del student["city"]            # key ধরে মোছা
age = student.pop("age")       # মুছে মানটা ফেরত দেয়
print(student)                 # {'name': 'Rahim'}

#for দিয়ে পড়া
student = {"name": "Rahim", "age": 20, "city": "Ctg"}

for key in student:
    print(key, "→", student[key])

#দরকারি function
marks = {"bangla": 70, "english": 80, "math": 90}

print(len(marks))               # 3 (কয়টা জোড়া)
print(sum(marks.values()))      # 240
print(max(marks.values()))      # 90
print(sum(marks.values()) / len(marks))   # 80.0

#উদাহরণ: শব্দ গোনা
#প্রতিটা অক্ষর কতবার এসেছে:
word = "banana"
count = {}

for letter in word:
   if letter in count:
     count[letter] += 1
   else:
     count[letter] = 1
print(count)

##project idea
contacts = {}

while True:
    print("1.Addition 2.Finding 3.see all 4.exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("addition complete")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("not founded")

    elif choice == "3":
        if len(contacts) == 0:
            print("no contacts found")
        else:
            for name, phone in contacts.items(): #সব দেখুন
                print(f"{name}: {phone}")

    elif choice == "4":
        print("exit! thank you")
        break

    else:
        print("invalid choice")


