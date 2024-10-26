f = open('../txtf/input.txt')
a, b = map(int,f.readline().split())
f.close()
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    f = open('../txtf/output.txt', 'w')
    s = str(a+b)
    f.write(s)
    f.close()
else:
    print("ERROR")