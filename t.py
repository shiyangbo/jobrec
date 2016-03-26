#import pymysql
#
## establish connect
#conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
#        passwd="shi520shi", db="xing", charset="UTF8")
#cur = conn.cursor()
#
#sql_1 = "SELECT user_id, item_id FROM interactions WHERE user_id=2882142 AND item_id=88 AND interaction_type=1;"
#tmp_len = cur.execute(sql_1)
#print(tmp_len)
#
## close connect
#conn.commit()
#cur.close()
#conn.close()

#import scipy.spatial as sysp
#a = [0, 0, 1, 2, 0]
#b = [1, 2, 1, 1, 1]
#cos = sysp.distance.cosine(a, b)
#print(cos)

from sys import argv

script, file_path = argv

with open(file_path + "/re.csv", "r") as tmp_file:
    tmp_list = []

    n = 0
    for line in tmp_file.readlines():
        tmp_str = line.strip().split("\t")
        cos = float(tmp_str[2])
        nums_1 = int(float(tmp_str[3]))
        nums_4 = int(float(tmp_str[4]))
        tmp_list.append((cos, nums_1, nums_4))

        n += 1

        print(n)

print(len(tmp_list))
