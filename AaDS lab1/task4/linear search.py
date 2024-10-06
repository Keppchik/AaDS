import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open("input.txt", "r")
a = list(f.readline().split())
v = f.readline()
f.close()

k = []
for i in range(len(a)):
    if a[i] == v:
        k.append(i)

f = open("output.txt", "w")
if len(k) == 0:
    f.write("-1")
elif len(k) == 1:
    f.write(str(k[0]))
else:
    f.write(str(len(k))+"\n")
    for i in range(len(k)-1):
        f.write(str(k[i])+',')
    f.write(str(k[len(k)-1]))
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ" )
tracemalloc.stop()