import utils
import os

count = 0

def merge_count(A, p, q, r):
    global count

    L = A[p:q]
    R = A[q:r]
    R.append(float('inf'))
    L.append(float('inf'))

    i, j = 0, 0
    for k in range(p, r):
        if L[i] <= R[j]:
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

def main(isTest = False, a = None, n = None):
    global count
    time_start = utils.start_tracking()
    input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


    if not isTest:
        data = utils.read_from_file(input_path)
        n = data[0]
        a = data[1:]

    merge_sort(a, 0, n)

    utils.write_in_file(output_path, [count])
    if not isTest:
        utils.print_time_memory(time_start)
    return count

if __name__ == "__main__":
    main()