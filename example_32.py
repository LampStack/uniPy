import os
os.system('cls')

# کلاسی برای یک مستطیل بنویسید که متود های زیر را داشته باشد :
# محاسبه محیط
# محاسبه مساحت
# تشخیص مربع بودن

class rectangle :
    a, b = 0, 0
    def __init__(self) -> None :
        pass
    def set_args(self, a, b) -> None :
        self.a = a
        self.b = b
    def perimeter(self) -> int :
        return 2 * (self.a + self.b)
    def area(self) -> int :
        return self.a * self.b
    def isSquare(self) -> bool :
        if self.a == self.b :
            return True
        return False


my_object = rectangle()
my_object.set_args(2, 3)
print(my_object.perimeter())
print(my_object.area())
print(my_object.isSquare())