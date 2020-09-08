import sys

lista = []
dic = {}

def fibo(num):
    global dic

    if num == 0:
        dic[num] = 0
    elif num == 1:
        dic[num] = 1
    else:
        if num not in dic:
            dic[num] = fibo(num-1) + fibo(num-2)
    return dic[num]

while True:
    try:
        num = int(input())
        lista.append(num)
    except:
        break

for item in lista:
    sys.setrecursionlimit(int(item)*10)
    fibo(item)

for key in lista:
    print(dic[key])