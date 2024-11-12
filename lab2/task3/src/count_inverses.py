import lab2.utils as utils

count = 0

def merge_count(A, p, q, r):
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
        merge_count(A, p, q, r)
    return A

if __name__ == "__main__":
    time_start = utils.start_tracking()

    data = utils.read_from_file("../txtf/input.txt")
    n = data[0]
    a = data[1:]

    merge_sort(a, 0, n)

    utils.write_in_file("../txtf/output.txt", [count])
    utils.print_time_memory(time_start)