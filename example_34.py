import os
os.system('cls')

# کلاسی دلخواه بنویسید که ابتدا لیستی از اعداد را دریافت کند و متود های زیر را داشته باشد :
# محاسبه میانگین تمام اعداد
# حذف اعضای تکراری

class user :
    my_users = list()
    def __init__(self) -> None:
        while True :
            x = int(input('> '))
            if x == -1 : # با دریافت عدد منفی یک خاتمه یابد
                break
            self.my_users.append(x)
    def avg(self) :
        sum = 0
        for num in self.my_users :
            sum += num
        return sum/len(self.my_users)
    def remove(self) :
        self.my_users = list(set(self.my_users))
        return True
    

my_object = user()

print(my_object.my_users)
my_object.remove()
print(my_object.my_users)

print(my_object.avg())