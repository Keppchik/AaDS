import time
import psutil
t_start = time.perf_counter()

f = open("input.txt", "r")
n = int(f.readline())
a = list(map(int, f.readline().split()))
f.close()

for i in range(1, n):
    j = i
    temp = a[i]
    while j > 0 and a[j-1] < temp:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1
    a[j] = temp

f = open("output.txt", "w")
for i in range(n):
    f.write(str(a[i])+" ")
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Память:", psutil.Process().memory_info().rss / 1024 ** 2, "МБ")