import time
t_start = time.perf_counter()

f = open('input.txt')
k = int(f.readline())
f.close()
if 0 < k <= 10**7:
    a, b = 0, 1
    for i in range(k-1):
        a, b = b, (a+b)%10
    f = open('output.txt', 'w')
    f.write(str(b))
    f.close()
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
elif k == 0:
    f = open('output.txt', 'w')
    f.write("0")
    f.close()
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
else:
    print("ERROR")


