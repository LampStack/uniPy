import os
os.system('cls')

# برنامه ای بنویسید که نام و نمره تعداد دانشجو را دریافت کرده
# نام و نمره شاگرد اول کلاس را چاپ نماید

count = int(input('> '))
myDict = dict()
for i in range(count) :
    name, glare = input('> ').split()
    myDict[name] = float(glare)

max_name = ''
max_glare = 0

for name, glare in myDict.items() :
    if glare > max_glare :
        max_name = name
        max_glare = glare

print(max_name, str(max_glare))