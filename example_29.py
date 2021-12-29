import os
os.system('cls')

# برنامه ای بنویسید که یک عدد از کاربر دریافت کرده و آنرا در یک لیست مرتب شده درج نماید
# تابع insert

my_list = [1, 5, 7, 8, 9, 15, 25]
n = int(input('> '))

for i in range(len(my_list)):
    if my_list[i] >= n :
        my_list.insert(i, n)
        break

print(my_list)