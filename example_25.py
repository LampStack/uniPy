import os
os.system('cls')

# برنامه ای بنویسید که یک فایل متنی را خوانده و خطی که بیشترین کلمه را دارد چاپ نماید

with open('file.txt', 'r') as file :
    my_file = file.read()

myLen = list()
for line in my_file.split('\n') :
    myLen.append(len(line.split()))

max = 1
index = 0

for i in range(len(myLen)) :
    if myLen[i] > max :
        max = myLen[i]
        index = i

print(my_file.split('\n')[index])
