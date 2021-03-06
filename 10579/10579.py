import sys

dic = {}

def fibo(num):
    global dic

    if num == 0:
        dic[num] = 0
    elif num == 1:
        dic[num] = 1
    else:
        if num not in dic: #verifico se o calculo da fibo ja foi feito
            dic[num] = fibo(num-1) + fibo(num-2)
    return dic[num]

def main():

    lista_num = [] #guarda os valores de entrada
    
    while True:
        try:
            num = int(input())
            lista_num.append(num)
        except:
            break

    for item in lista_num:
        sys.setrecursionlimit(int(item)*10)
        fibo(item)

    for key in lista_num:
        print(dic[key])

if __name__ == "__main__":
    main()