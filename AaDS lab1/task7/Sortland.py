import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open("input.txt", "r")
n = int(f.readline())
a = list(map(float,f.readline().split()))
f.close()

b = a.copy()

for i in range(n):
    for j in range(n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

s = ["-1", "-1", "-1"]
for i in range(n):
    if b[i] == a[0]:
        s[0] = str(i+1)
    elif b[i] == a[n//2]:
        s[1] = str(i+1)
    elif b[i] == a[-1]:
        s[2] = str(i+1)
f = open("output.txt", "w")
for i in range(3):
    f.write(s[i]+" ")
f.close()


print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ" )
tracemalloc.stop()