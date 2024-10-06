import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open("input.txt", "r")
a = list(map(int,f.readline().split()))
f.close()

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[j], a[i] = a[i], a[j]

f = open("output.txt", "w")
for i in range(len(a)):
    f.write(str(a[i]) + " ")
f.close()


print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ" )
tracemalloc.stop()