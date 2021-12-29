import os
os.system('cls')

# تابعی بازگشتی بنویسید که یک عدد دریافت کرده و تعداد ارقام آنرا برگرداند

def digits(n, sum=0) -> int :
    if int(n/10) == 0 :
        return sum + 1
    else :
        return digits(int(n/10), sum+1)

n = int(input('> '))
print(digits(n))