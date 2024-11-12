import time
import tracemalloc
import os

t_start = time.perf_counter()
tracemalloc.start()

current_script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_script_dir, '..', 'txtf')

input_path = os.path.abspath(relative_path + "/input.txt")
output_path = os.path.abspath(relative_path + "/output.txt")

f = open(input_path, 'r')
k = int(f.readline())
f.close()
if 0 < k <= 45:
    a, b = 0, 1
    for i in range(k-1):
        a, b = b, a+b
    f = open(output_path, 'w')
    f.write(str(b))
    f.close()
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print(f'Память: {tracemalloc.get_traced_memory()[1] / (1024 ** 2)} МБ')
elif k == 0:
    f = open(output_path, 'w')
    f.write("0")
    f.close()
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
    print(f'Память: {tracemalloc.get_traced_memory()[1] / (1024 ** 2)} МБ')
else:
    print("ERROR")
tracemalloc.stop()
