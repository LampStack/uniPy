import os
os.system('cls')

# برنامه ای بنویسید که هرچه در ترمینال تایپ شد به انتهای فایل متنی اضافه کند

while True :
    line = input('> ')
    if line == 'q' : break
    with open('file.txt', 'a') as file :
        file.write(line + '\n')