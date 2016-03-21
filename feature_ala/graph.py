import numpy as np
from sys import argv

script, file_path = argv

cos_arr = np.linspace(0, 1, 21)

tplType = np.dtype(np.float64, np.int32)

result = np.zeros((len(cos_arr), 2), dtype=tplType)
result[:, 0] = cos_arr

#num_arr = np.loadtxt(file_path + "/cos_nums_1.csv", dtype=tplType, usecols=(0, 1))
num_arr = np.loadtxt(file_path + "/cos_nums_4.csv", dtype=tplType, usecols=(0, 1))

ind = 0

for cos in cos_arr:
    thresh = 0.05

    if cos < 1e-6:

        for ety in num_arr:

            if ety[0] >= cos and ety[0] < cos + thresh:
                result[ind, 1] += ety[1]
            else:
                pass

    elif cos - 1 > 1e-6 or 1 - cos > 1e-6:

        for ety in num_arr:

            if ety[0] >= cos - thresh and ety[0] <= cos:
                result[ind, 1] += ety[1]
            else:
                pass

    else:

        for ety in num_arr:

            if ety[0] >= cos - thresh and ety[0] < cos + thresh:
                result[ind, 1] += ety[1]
            else:
                pass

    ind += 1

#np.savetxt(file_path + "/r1.txt", result, fmt="%s", delimiter="\t")
np.savetxt(file_path + "/r2.txt", result, fmt="%s", delimiter="\t")
