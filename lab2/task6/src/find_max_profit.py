import lab2.utils as utils

def maxsubarray(arr):
    pref = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        pref[i] = pref[i - 1] + a[i - 1]

    min_l = [float('inf')] * (len(a))
    min_l[0] = 0
    for i in range(1, len(a)):
        min_l[i] = min(pref[i], min_l[i - 1])

    max_arr = float('-inf')
    for i in range(1, len(a) + 1):
        max_arr = max(max_arr, pref[i] - min_l[i - 1])

    return max_arr

if __name__ == "__main__":
    time_start = utils.start_tracking()

    data = utils.read_from_file("../txtf/input.txt")
    a = data
    result = maxsubarray(a)

    utils.write_in_file("../txtf/output.txt", [result])
    utils.print_time_memory(time_start)