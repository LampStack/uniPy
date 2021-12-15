import os
os.system('cls')

# برنامه ای بنویسید که لیست دانشجویان و نمراتشان را دریافت کرده
# نام و نمره سه نفر برتر را نمایش دهد

def my_sort(L1, L2):
    for temp in range(len(L1)-1) :
        for i in range(len(L1)-1) :
            if L2[i] < L2[i+1] :
                L1[i], L1[i+1] = L1[i+1], L1[i]
                L2[i], L2[i+1] = L2[i+1], L2[i]

count = int(input('> '))
myDict = dict()
for i in range(count) :
    name, glare = input('> ').split()
    myDict[name] = float(glare)
L1 = list(myDict.keys()) #names
L2 = list(myDict.values()) #Glare
my_sort(L1, L2)

for i in range(3) :
    print(L1[i], str(L2[i]))