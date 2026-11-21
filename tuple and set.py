#দুটো দরকারি method
t = (1, 2, 2, 3, 2)

print(t.count(2))    # 3 (২ কতবার আছে)
print(t.index(3))    # 3 (৩ কোন index-এ)

#Unpacking: tuple খুলে variable-এ রাখা
point = (10, 20)
x, y = point

print(x)    # 10
print(y)    # 20

######
#small, big = min_max([5, 2, 9])    # function দুটো মান tuple হিসেবে ফেরত দেয়

""""
কেন tuple ব্যবহার করব?
যে তথ্য বদলানো উচিত না (যেমন দিনের নাম, স্থানাঙ্ক)
list-এর চেয়ে সামান্য দ্রুত
dictionary-র key হিসেবে ব্যবহার করা যায় (list পারে না)
"""

#২. Set
#Set হলো জিনিসের সংগ্রহ, যেখানে ডুপ্লিকেট থাকে না আর ক্রম নেই (index নেই)। বন্ধনী { }।
s = {1, 2, 3, 2, 1}
print(s)        # {1, 2, 3} (ডুপ্লিকেট বাদ)

#ডুপ্লিকেট সরানো
#এটাই set-এর সবচেয়ে বেশি ব্যবহার:
numbers = [4, 9, 2, 9, 4, 7]
unique = list(set(numbers))
print(unique)     # [2, 4, 7, 9] (ক্রম আলাদা হতে পারে)

#যোগ আর মোছা
s = {1, 2, 3}

s.add(4)          # যোগ
s.add(2)          # আগে থেকে আছে, কিছু বদলায় না
print(s)          # {1, 2, 3, 4}

s.remove(1)       # মোছা (না থাকলে KeyError)
s.discard(10)     # মোছা (না থাকলে error নেই)
print(s)          # {2, 3, 4}

#আছে কিনা
s = {1, 2, 3}
print(2 in s)      # True
print(9 in s)      # False

#index নেই
s = {10, 20, 30}
print(s[0])  # TypeError! set-এ index চলে না

#Set-এর গণিত (দুই set নিয়ে কাজ)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # {1, 2, 3, 4, 5, 6} মিলন (union): সব মিলিয়ে
print(a & b)    # {3, 4} ছেদ (intersection): দুটোতেই আছে
print(a - b)    # {1, 2} শুধু a-তে আছে, b-তে নেই
print(a ^ b)    # {1, 2, 5, 6} যেকোনো একটাতে আছে, দুটোতে নয়

"""""
t = (5)          # ভুল ধারণা: এটা tuple নয়, শুধু সংখ্যা ৫
t = (5,)         # ঠিক: কমা দিলে tuple

s = {}           # ভুল ধারণা: এটা dictionary
s = set()        # ঠিক: খালি set

s = {1, 2, 3}
print(s[0])      # ভুল: set-এ index নেই
   list	 tuple	set	
বন্ধনী	[ ]  ( )	 { }
"""""

#mini project
cricket_info = ("Cricket Club", "Friday")
coding_info = ("Coding Club", "Saturday")

cricket = {"Rahim", "Karim", "Salma"}
coding = {"Salma", "Anis", "Rahim"}

name1, day1 = cricket_info
name2, day2 = coding_info

print(f"{name1} মিটিং হয় {day1}")
print(f"{name2} মিটিং হয় {day2}")

print("\nদুই ক্লাবেই আছে:", cricket & coding)
print("মোট সদস্য:", cricket | coding)
print("শুধু ক্রিকেটে:", cricket - coding)
print("শুধু কোডিংয়ে:", coding - cricket)
print("মোট কতজন:", len(cricket | coding))

new_name = input("\nনতুন সদস্যের নাম: ")
cricket.add(new_name)
print("ক্রিকেট ক্লাবের সদস্য:", cricket)
print("সংখ্যা:", len(cricket))

search = input("\nকার নাম খুঁজবেন? ")

if search in cricket and search in coding:
    print(f"{search} দুই ক্লাবেই আছে")
elif search in cricket:
    print(f"{search} শুধু ক্রিকেটে আছে")
elif search in coding:
    print(f"{search} শুধু কোডিংয়ে আছে")
else:
    print(f"{search} কোনো ক্লাবে নেই")



