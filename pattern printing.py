n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

###উল্টো ত্রিভুজ
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

###সংখ্যার ত্রিভুজ
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

###প্রতি সারিতে সেই সারির নম্বর বারবার:
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

###পিরামিড (space লাগে)
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

""""
pattern ভাবার কৌশল (সবচেয়ে জরুরি)

নতুন pattern দেখলে এই তিনটা প্রশ্ন করুন:

কয়টা সারি? → বাইরের loop
প্রতি সারিতে কী কী, কয়টা? → ভেতরের loop। সারি নম্বরের সাথে সম্পর্ক খুঁজুন (i টা? n - i টা? সবসময় n টা?)
কিছু আগে ছাপতে হবে কি? (যেমন space)
মনে রাখার ছক
pattern	সারি	ভেতরের loop
বর্গ	range(n)	range(n)
ত্রিভুজ	range(1, n+1)	range(i)
উল্টো ত্রিভুজ	range(n, 0, -1)	range(i)
পিরামিড	range(1, n+1)	আগে space (n-i), তারপর তারা (i)

"""