import time
import tracemalloc

def bin_search(a, value, p, r):
    if p < r:
        q = (p + r) // 2
        if value < a[q]:
            return bin_search(a, value, p, q)
        elif value > a[q]:
            return bin_search(a, value, q + 1, r)
        else:
            return q
    return -1


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    f = open("../txtf/input.txt", "r")
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    k = int(f.readline())
    b = list(map(int, f.readline().split()))
    f.close()


    f = open("../txtf/output.txt", "w")
    for number in b:
        f.write(str(bin_search(a, number, 0, n)) + " ")
    f.close()

    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
    tracemalloc.stop()