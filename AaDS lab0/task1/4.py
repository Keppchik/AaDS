f = open('../task1/input.txt')
a, b = map(int,f.readline().split())
f.close()
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    f = open('../task1/output.txt', 'w')
    s = str(a+b*b)
    f.write(s)
    f.close()
else:
    print("ERROR")