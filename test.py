import random
import numpy as np
import pymysql
from sys import argv

script, file_path, debug_path_05p, debug_path_010p, debug_path_020p, debug_path_15p, debug_path_110p, debug_path_120p = argv

tar_usr = np.loadtxt(file_path, dtype=np.int32)
dt = np.dtype("a800")
test_Mat_0_5p = np.zeros([1, 2], dtype=dt)
test_Mat_0_10p = np.zeros([1, 2], dtype=dt)
test_Mat_0_20p = np.zeros([1, 2], dtype=dt)
test_Mat_1_5p = np.zeros([1, 2], dtype=dt)
test_Mat_1_10p = np.zeros([1, 2], dtype=dt)
test_Mat_1_20p = np.zeros([1, 2], dtype=dt)

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="xing3", charset="UTF8")
cur = conn.cursor()

# 先单版本，然后加上缓存加快速度
for i in range(tar_usr.shape[0]):

    usr_id = tar_usr[i]

    sql_1 = "SELECT count(user_id) FROM interactions_new WHERE user_id=165 AND created_at<>4;" 
    stat = cur.execute(sql_1 % usr_id)

    if stat == 0:
        pass
    else:
        len_ety = cur.fetchone()
        #entries = cur.fetchone()
        entries = cur.fetchall()
        tmp_Mat = np.array(entries).reshape(-1, 4) # notice

        # 时间排序取5%， 10%， 20%

        ind = np.argsort(-tmp_Mat[:, 3]) # notice that -1

        # 5%
        if tmp_Mat.shape[0] < 20:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_Mat_sec = tmp_Mat_sec[0, :].reshape(-1, 4) # notice

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat_sec[0, 1])

            test_Mat_0_5p = np.row_stack((test_Mat_0_5p, [str_usr, str_jobs]))
        else:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_len = int(tmp_Mat_sec.shape[0] * 0.05)

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                str_jobs += str(tmp_Mat_sec[j, 1])

                if j != tmp_len - 1:
                    str_jobs += ","
                else:
                    pass

            test_Mat_0_5p = np.row_stack((test_Mat_0_5p, [str_usr, str_jobs]))

        # 10%
        if tmp_Mat.shape[0] < 10:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_Mat_sec = tmp_Mat_sec[0, :].reshape(-1, 4) # notice

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat_sec[0, 1])

            test_Mat_0_10p = np.row_stack((test_Mat_0_10p, [str_usr, str_jobs]))
        else:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_len = int(tmp_Mat_sec.shape[0] * 0.1)

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                str_jobs += str(tmp_Mat_sec[j, 1])

                if j != tmp_len - 1:
                    str_jobs += ","
                else:
                    pass

            test_Mat_0_10p = np.row_stack((test_Mat_0_10p, [str_usr, str_jobs]))

        # 20%
        if tmp_Mat.shape[0] < 5:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_Mat_sec = tmp_Mat_sec[0, :].reshape(-1, 4) # notice

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat_sec[0, 1])

            test_Mat_0_20p = np.row_stack((test_Mat_0_20p, [str_usr, str_jobs]))
        else:
            tmp_Mat_sec = tmp_Mat[ind]
            tmp_len = int(tmp_Mat_sec.shape[0] * 0.2)

            str_usr = str(tmp_Mat_sec[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                str_jobs += str(tmp_Mat_sec[j, 1])

                if j != tmp_len - 1:
                    str_jobs += ","
                else:
                    pass

            test_Mat_0_20p = np.row_stack((test_Mat_0_20p, [str_usr, str_jobs]))

        # 随机取5%， 10%， 30%

        # 5%
        if tmp_Mat.shape[0] < 20:
            rnd = random.sample(range(tmp_Mat.shape[0]), 1)

            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat[rnd[0], 1])

            test_Mat_1_5p = np.row_stack((test_Mat_1_5p, [str_usr, str_jobs]))
        else:
            tmp_len = int(tmp_Mat.shape[0] * 0.05)
            rnd = random.sample(range(tmp_Mat.shape[0]), tmp_len)
            
            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                 str_jobs += str(tmp_Mat[rnd[j], 1])
            
                 if j != tmp_len -1:
                     str_jobs += ","
                 else:
                     pass

            test_Mat_1_5p = np.row_stack((test_Mat_1_5p, [str_usr, str_jobs]))

        # 10%
        if tmp_Mat.shape[0] < 10:
            rnd = random.sample(range(tmp_Mat.shape[0]), 1)

            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat[rnd[0], 1])

            test_Mat_1_10p = np.row_stack((test_Mat_1_10p, [str_usr, str_jobs]))
        else:
            tmp_len = int(tmp_Mat.shape[0] * 0.1)
            rnd = random.sample(range(tmp_Mat.shape[0]), tmp_len)

            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                str_jobs += str(tmp_Mat[rnd[j], 1])

                if j != tmp_len -1:
                    str_jobs += ","
                else:
                    pass

            test_Mat_1_10p = np.row_stack((test_Mat_1_10p, [str_usr, str_jobs]))

        # 20%
        if tmp_Mat.shape[0] < 5:
            rnd = random.sample(range(tmp_Mat.shape[0]), 1)

            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            str_jobs += str(tmp_Mat[rnd[0], 1])

            test_Mat_1_20p = np.row_stack((test_Mat_1_20p, [str_usr, str_jobs]))
        else:
            tmp_len = int(tmp_Mat.shape[0] * 0.2)
            rnd = random.sample(range(tmp_Mat.shape[0]), tmp_len)

            str_usr = str(tmp_Mat[0, 0])
            str_jobs = ""

            for j in range(tmp_len):
                str_jobs += str(tmp_Mat[rnd[j], 1])

                if j != tmp_len -1:
                    str_jobs += ","
                else:
                    pass

            test_Mat_1_20p = np.row_stack((test_Mat_1_20p, [str_usr, str_jobs]))


    if i % 1000 == 0:
        print("test:", i)
        file_name = "/" + str(i) + "_test.txt"

        np.savetxt(debug_path_05p + file_name, test_Mat_0_5p, 
                fmt="%s", delimiter="\t")
        np.savetxt(debug_path_010p + file_name, test_Mat_0_10p, 
                fmt="%s", delimiter="\t")
        np.savetxt(debug_path_020p + file_name, test_Mat_0_20p, 
                fmt="%s", delimiter="\t")
        np.savetxt(debug_path_15p + file_name, test_Mat_1_5p, 
                fmt="%s", delimiter="\t")
        np.savetxt(debug_path_110p + file_name, test_Mat_1_10p, 
                fmt="%s", delimiter="\t")
        np.savetxt(debug_path_120p + file_name, test_Mat_1_20p, 
                fmt="%s", delimiter="\t")
    else:
        pass

cur.close()
conn.close()
