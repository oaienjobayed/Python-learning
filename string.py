word = "Python"

print(word[0])     # P
print(word[3])     # h
print(word[-1])    # n (একদম শেষের অক্ষর)
print(len(word))   # 6 (কয়টা অক্ষর)

#Slicing: অংশ কেটে নেওয়া
word = "Python"

print(word[0:2])   # Py
print(word[2:5])   # tho
print(word[:3])    # Pyt  (শুরু থেকে ২ পর্যন্ত)
print(word[3:])    # hon  (৩ থেকে শেষ পর্যন্ত)
print(word[::-1])  # nohtyP (উল্টে দেওয়া)

#string-এর একটা অক্ষর সরাসরি বদলানো যায় না। নতুন string বানাতে হয়:
word = "Python"
new_word = "J" + word[1:]
print(new_word)    # Jython

#বড়-ছোট হাতের অক্ষর
s = "Hello World"

print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.capitalize())   # Hello world (প্রথম অক্ষর বড়)
print(s.title())        # Hello World (প্রতি শব্দের প্রথম অক্ষর বড়)

#বাড়তি space মোছা
s = "   hello   "
print(s.strip())    # hello (দুই পাশের space গেল)
print(s.lstrip())   # শুধু বাঁ পাশের
print(s.rstrip())   # শুধু ডান পাশের

#খোঁজা
s = "I love Python"

print(s.find("love"))      # 2  (কত নম্বর index-এ শুরু)
print(s.find("Java"))      # -1 (পাওয়া যায়নি)
print(s.count("o"))        # 2  (কতবার আছে)
print(s.startswith("I"))   # True
print(s.endswith("n"))     # True

#বদলানো
s = "I love Python"
print(s.replace("Python", "Java"))   # I love Java
print(s)                             # I love Python (মূলটা বদলায়নি)

#স্বরবর্ণ গোনার উদাহরণ:
word = "education"
count = 0

for letter in word:
    if letter in "aeiou":
        count += 1

print("স্বরবর্ণ:", count)    # 5

#মান বসানো (f-string, আপনি জানেন)
name = "Rahim"
age = 20
print(f"নাম: {name}, বয়স: {age}")
print(f"নাম বড় হাতে: {name.upper()}")   # {} এর ভেতরে method চলে