import time
import tracemalloc


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    f = open("../txtf/input.txt", "r")
    a = list(map(int, f.readline().split()))
    f.close()

    max_sub = a[0]
    sub = a[0]

    for i in range(1, len(a)):
        sub = max(a[i], sub + a[i])
        max_sub = max(max_sub, sub)

    f = open("../txtf/output.txt", "w")
    f.write(str(max_sub))
    f.close()

    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
    tracemalloc.stop()