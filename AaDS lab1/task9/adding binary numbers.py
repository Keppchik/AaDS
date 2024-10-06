import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open("input.txt", "r")
s1, s2 = f.readline().split()
f.close()

s3 = [0]
for i in range(len(s1)):
    s3.append(int(s1[i]) + int(s2[i]))

for i in range(1,len(s3)):
    for j in range(i, len(s3)):
        if int(s3[j]) == 2:
            s3[j-1] += 1
            s3[j] = 0

f = open("output.txt", "w")
for i in range(len(s3)):
    f.write(str(s3[i]))
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ" )
tracemalloc.stop()