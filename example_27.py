import os
os.system('cls')

# تابع بازگشتی برای تبدیل از مبنای ده به باینری

def toBinary(n) :
    if int(n/2) != 0 :
        toBinary(int(n/2))
    print(str(n%2), end='')

toBinary(20) # 10100

# 20/2
#     0
# 10/2
#     0
# 5/2
#     1
# 2/2
#     0
# 1/2
#     1
# 10100