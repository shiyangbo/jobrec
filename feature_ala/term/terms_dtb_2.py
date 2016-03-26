import numpy as np
from sys import argv

# 交集是：2596
# 并集是：5004

script, file_path = argv

usr_list = np.loadtxt(file_path + "/usr_top3800.txt", dtype=np.int32,
        usecols=(0, 1))
itm_list = np.loadtxt(file_path + "/itm_top3800.txt", dtype=np.int32,
        usecols=(0, 1))

usr_set = set(usr_list[:, 0])
itm_set = set(itm_list[:, 0])

inter_set = usr_set & itm_set
union_set = usr_set | itm_set

result = list(inter_set) # save inter_set as a list
result.sort()

np.savetxt(file_path + "/re.txt", np.array(result), fmt="%d", delimiter="\t")
