import lab2.utils as utils

def max_subarr(arr):
    max_sub = a[0]
    sub = a[0]

    for i in range(1, len(a)):
        sub = max(a[i], sub + a[i])
        max_sub = max(max_sub, sub)

    return max_sub

if __name__ == "__main__":
    time_start = utils.start_tracking()

    data = utils.read_from_file("../txtf/input.txt")
    a = data
    result = max_subarr(a)

    utils.write_in_file("../txtf/output.txt", [result])
    utils.print_time_memory(time_start)