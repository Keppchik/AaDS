import time
import tracemalloc

count = 0

def merge(A, p, q, r):
    global count

    L = A[p:q]
    R = A[q:r]
    R.append(float('inf'))
    L.append(float('inf'))

    i, j = 0, 0
    for k in range(p, r):
        if L[i] <= R[j] :
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += len(L) - i - 1


def merge_sort(A, p, r):
    if p < r - 1:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)
    return A

if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    f = open("../txtf/input.txt", "r")
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    f.close()

    merge_sort(a, 0, len(a))

    f = open("../txtf/output.txt", "w")
    f.write(str(count))
    f.close()

    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
    tracemalloc.stop()