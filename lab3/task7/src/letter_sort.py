import lab3.utils as utils

def letter_sort(arr, n, m, k):
    indexes = [i+1 for i in range(n)]
    for i in range(m-1, m-1-k, -1):
        count = [0] * 26
        for j in range(n):
            count[ord(arr[j][i])-97] += 1
        for j in range(1, 26):
            count[j] += count[j-1]

        output = [0]*n
        output_indexes = [0]*n
        for j in range(n-1, -1, -1):
            letter = ord(arr[j][i])-97
            output[count[letter] - 1] = arr[j]
            output_indexes[count[letter] - 1] = indexes[j]
            count[letter] -= 1
        for j in range(n):
            arr[j] = output[j]
            indexes[j] = output_indexes[j]

    return indexes


if __name__ == "__main__":
    time_start = utils.start_tracking()

    data = utils.read_from_file("../txtf/input.txt", type=str)
    n = int(data[0])
    m = int(data[2])
    k = int(data[4])
    arr = data[5:].replace("\n", " ").split()

    result = letter_sort(arr.copy(), n, m, k)

    utils.write_in_file("../txtf/output.txt", result)
    utils.print_time_memory(time_start)