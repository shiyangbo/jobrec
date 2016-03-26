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

#print("to put mat in tmp_arr")
#tuType = np.dtype(np.float64, np.int32, np.int32)
#tmp_arr = np.loadtxt(file_path + "/cos_nums.txt", dtype=tuType, usecols=(0, 1, 2))
#print("put mat in tmp_arr: ok")

tmp_1_dit = {} # for type_1
tmp_4_dit = {}

# record true useful info to 1_dit and 4_dit
# true useful info is: (uni_cos, usr_click_nums, same_cos_nums) csv-format
line = 0
with open(file_path + "/cos_nums.txt", "r") as tmp_file:

    for row in tmp_file.readlines():
        tmp_list = row.split("\t")
        cos = tmp_list[0]
        nums_1 = int(float(tmp_list[1]))
        nums_4 = int(float(tmp_list[2]))

        if cos in tmp_1_dit:
            tmp_1_dit[cos][0] = tmp_1_dit.get(cos)[0] + nums_1
            tmp_1_dit[cos][1] = tmp_1_dit.get(cos)[1] + 1
        else:
            tmp_1_dit.update({cos: [nums_1, 1]})

        if cos in tmp_4_dit:
            tmp_4_dit[cos][0] = tmp_4_dit.get(cos)[0] + nums_4
            tmp_4_dit[cos][1] = tmp_4_dit.get(cos)[1] + 1
        else:
            tmp_4_dit.update({cos: [nums_4, 1]})

        line += 1

        if line % 1000 == 0:
            print("line:", line)
        else:
            pass
#line = 0
#for tpl in tmp_arr:
#    cos = tpl[0]
#    nums_1 = int(tpl[1])
#    nums_4 = int(tpl[2])
#
#    if cos in tmp_1_dit:
#        tmp_1_dit[cos][0] = tmp_1_dit.get(cos)[0] + nums_1
#        tmp_1_dit[cos][1] = tmp_1_dit.get(cos)[1] + 1
#    else:
#        tmp_1_dit.update({cos: [nums_1, 1]})
#
#    if cos in tmp_4_dit:
#        tmp_4_dit[cos][0] = tmp_4_dit.get(cos)[0] + nums_4
#        tmp_4_dit[cos][1] = tmp_4_dit.get(cos)[1] + 1
#    else:
#        tmp_4_dit.update({cos: [nums_4, 1]})
#
#    line += 1
#    
#    if line % 1000 == 0:
#        print("line:", line)
#    else:
#        pass

# save 1 dit
with open(file_path + "/cos_nums_1.csv", "w", newline="") as tmp_file:
    spamwriter = csv.writer(tmp_file, delimiter=",")
    spamwriter.writerow(["cos", "usr_click_nums", "same_cos_nums"])

    for k in tmp_1_dit:
        usr_click_nums = tmp_1_dit.get(k)[0]
        same_cos_nums = tmp_1_dit.get(k)[1]
        spamwriter.writerow([k, usr_click_nums, same_cos_nums])

# save 4 dit
with open(file_path + "/cos_nums_4.csv", "w", newline="") as tmp_file:
    spamwriter = csv.writer(tmp_file, delimiter=",")
    spamwriter.writerow(["cos", "usr_click_nums", "same_cos_nums"])

    for k in tmp_4_dit:
        usr_click_nums = tmp_4_dit.get(k)[0]
        same_cos_nums = tmp_4_dit.get(k)[1]
        spamwriter.writerow([k, usr_click_nums, same_cos_nums])

