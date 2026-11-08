fruits = ["আম", "জাম"]

fruits.append("কলা")        # শেষে যোগ করা
print(fruits)               # ['আম', 'জাম', 'কলা']

fruits.insert(1, "পেয়ারা")  # ১ নম্বর জায়গায় বসানো
print(fruits)               # ['আম', 'পেয়ারা', 'জাম', 'কলা']

fruits.remove("জাম")        # নাম ধরে মুছা
print(fruits)               # ['আম', 'পেয়ারা', 'কলা']

fruits.pop()                # শেষেরটা মুছে ফেলে
print(fruits)               # ['আম', 'পেয়ারা']

###############
marks = [78, 85, 62, 90]

print(len(marks))     # 4  (কয়টা জিনিস)
print(max(marks))     # 90
print(min(marks))     # 62
print(sum(marks))     # 315
print(sum(marks) / len(marks))   # 78.75 (গড়)
print(sorted(marks))  # [62, 78, 85, 90]

##############################
marks = []
n = int(input("how many subjet: "))

count = 1
while count <= n:
    m = int(input(f"{count} subject number"))
    marks.append(m)
    count = count + 1

print(marks)
print(max(marks))
print(min(marks))
print(f"{sum(marks)/len(marks)}")