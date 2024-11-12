import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_script_dir, '..', 'txtf')

input_path = os.path.abspath(relative_path + "/input.txt")
output_path = os.path.abspath(relative_path + "/output.txt")

f = open(input_path, 'r')
a, b = map(int,f.readline().split())
f.close()
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    f = open(output_path, 'w')
    s = str(a+b*b)
    f.write(s)
    f.close()
else:
    print("ERROR")