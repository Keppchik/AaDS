import time
import tracemalloc


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()

    f = open("../txtf/input.txt", "r")
    a = list(map(int, f.readline().split()))
    f.close()


    pref = [0]*(len(a)+1)
    for i in range(1, len(a)+1):
        pref[i] = pref[i-1] + a[i-1]

    min_l = [float('inf')]*(len(a))
    min_l[0] = 0
    for i in range(1,len(a)):
        min_l[i] = min(pref[i], min_l[i-1])

    max_arr = float('-inf')
    for i in range(1, len(a)+1):
        max_arr = max(max_arr, pref[i] - min_l[i-1])



    f = open("../txtf/output.txt", "w")
    f.write(str(max_arr)+"   "+str(max_sum))
    f.close()

    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
    tracemalloc.stop()