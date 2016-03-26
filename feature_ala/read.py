import numpy as np
import csv
from sys import argv

script, file_path = argv

#with open(file_path + "/re.csv", "r") as tmp_file:
#    tmp_list = []
#
#    n = 0
#    for line in tmp_file.readlines():
#        tmp_str = line.strip().split("\t")
#
#        cos = float(tmp_str[2])
#        nums_1 = int(float(tmp_str[3]))
#        nums_4 = int(float(tmp_str[4]))
#
#        tmp_list.append((cos, nums_1, nums_4))
#
#        n += 1
#
#        print(n)
#
#tuType = np.dtype(np.float64, np.int32, np.int32)
#tmp_arr = np.array(tmp_list, dtype=tuType)
#np.savetxt(file_path + "/cos_nums.txt", tmp_arr, fmt="%s", delimiter="\t")

tuType = np.dtype(np.float64, np.int32, np.int32)
tmp_arr = np.loadtxt(file_path + "/cos_nums.txt", dtype=tuType, usecols=(0, 1, 2))

tmp_1_dit = {} # for type_1
tmp_4_dit = {}

line = 0

for tpl in tmp_arr:
    cos = tpl[0]
    nums_1 = int(tpl[1])
    nums_4 = int(tpl[2])

    if cos in tmp_1_dit:
        tmp_1_dit[cos] = tmp_1_dit.get(cos) + nums_1
    else:
        tmp_1_dit.update({cos: nums_1})

    if cos in tmp_4_dit:
        tmp_4_dit[cos] = tmp_4_dit.get(cos) + nums_4
    else:
        tmp_4_dit.update({cos: nums_4})

    line += 1
    
    if line % 1000 == 0:
        print("line:", line)
    else:
        pass

# save 1 dit
with open(file_path + "/cos_nums_1.csv", "w", newline="") as tmp_file:
    spamwriter = csv.writer(tmp_file, delimiter="\t")
    spamwriter.writerow(["cos", "nums"])

    for k in tmp_1_dit:
        spamwriter.writerow([k, tmp_1_dit.get(k)])

# save 4 dit
with open(file_path + "/cos_nums_4.csv", "w", newline="") as tmp_file:
    spamwriter = csv.writer(tmp_file, delimiter="\t")
    spamwriter.writerow(["cos", "nums"])

    for k in tmp_4_dit:
        spamwriter.writerow([k, tmp_4_dit.get(k)])

