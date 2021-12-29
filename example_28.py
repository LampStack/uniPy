import os
os.system('cls')

# برنامه ای بنویسید که لیستی از کاربر دریافت کرده و اعضای تکراری را با استفاده از متود پاپ حذف نماید

n = int(input('count of list :'))
my_list = []
for i in range(n) :
    my_list.append(int(input('> enter data :')))

# [1, 4, 3, 4, 5]
#     i     j

for i in range(len(my_list)) :
    j = i + 1
    while j < len(my_list):
        if my_list[i] == my_list[j]:
            my_list.pop(j)
        else :
            j += 1

print(my_list)