import os
os.system('cls')

# کلاسی برای دایره بنویسید که متود های زیر را داشته باشد :
# محاسبه مساحت
# محاسبه محیط

class circle :
    r = 0
    def __init__(self, r) -> None :
        self.r = r
    def perimeter(self) -> float :
        return 2 * 3.14 * self.r
    def area(self) -> float :
        return 3.14 * self.r * self.r

my_object = circle(4)
print(my_object.perimeter())
print(my_object.area())