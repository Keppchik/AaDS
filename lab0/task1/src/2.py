a, b = map(int,input("Введите 2 числа через пробел: ").split())
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    print(a+b*b)
else:
    print("ERROR")