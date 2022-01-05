import os
os.system('cls')

# کلاس طراحی کنید که دو عدد صحیح را در متود سازنده دریافت کند و دارای متود های زیر باشد :
# جمع
# تفریق
# ضرب
# تقسیم
# توان

class math :
    a, b = 0, 0
    def __init__(self, a, b) -> None :
        self.a = a
        self.b = b
    def sum(self) -> int:
        return self.a + self.b
    def tafriq(self) -> int:
        return self.a - self.b
    def zarb(self) -> int:
        return self.a * self.b
    def taqsim(self) -> float :
        if self.b == 0 :
            return 0
        return self.a / self.b
    def tavan(self) -> int :
        return self.a ** self.b