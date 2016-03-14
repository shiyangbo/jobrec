"""
"""

import pymysql
import numpy as np
from sys import argv

script, file_path = argv

# establish connect
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="xing", charset="UTF8")
cur = conn.cursor()

day_list = []

sql = "SELECT COUNT(DISTINCT user_id) FROM interactions WHERE created_at >= UNIX_TIMESTAMP('%s') AND created_at <= UNIX_TIMESTAMP('%s');"

# july, 19-31
print("july")
for day in range(31):

    if day < 18:
        pass
    else:
        stat = cur.execute(sql % ("2015-8-" + str(day+1) + " 00:00:00", 
                "2015-8-" + str(day+1) + " 23:59:59"))

        if stat == 0:
            pass
        else:
            usr_num = cur.fetchone()[0]
            ety = ("2015-8-" + str(day + 1), usr_num)
            day_list.append(ety)

# aug, 1-30
print("aug")
for day in range(30):
    stat = cur.execute(sql % ("2015-9-" + str(day+1) + " 00:00:00", "2015-9-" +
            str(day+1) + " 23:59:59"))

    if stat == 0:
        pass
    else:
        usr_num = cur.fetchone()[0]
        ety = ("2015-9-" + str(day + 1), usr_num)
        day_list.append(ety)

# oct, 1-31
print("oct")
for day in range(31):
    stat = cur.execute(sql % ("2015-10-" + str(day+1) + " 00:00:00", "2015-10-" +
            str(day+1) + " 23:59:59"))
    if stat == 0:
        pass
    else:
        usr_num = cur.fetchone()[0]
        ety = ("2015-10-" + str(day + 1), usr_num)
        day_list.append(ety)

# nov, 1-9
print("nov")
for day in range(9):
    stat = cur.execute(sql % ("2015-11-" + str(day+1) + " 00:00:00", "2015-11-" +
            str(day+1) + " 23:00:00"))
    if stat == 0:
        pass
    else:
        usr_num = cur.fetchone()[0]
        ety = ("2015-11-" + str(day + 1), usr_num)
        day_list.append(ety)

conn.commit()

tmp_array = np.array(day_list)
np.savetxt(file_path + "/re.csv", tmp_array, fmt="%s", delimiter="\t")

# close connect
cur.close()
conn.close()
