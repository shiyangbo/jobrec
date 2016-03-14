import csv
import numpy as np
import pymysql
from sys import argv

def sel_ti(cur, usr_id, len_ety, per):
    """
    """

    if len_ety < int(1 / per):
        sql = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND created_at<>4 ORDER BY created_at DESC LIMIT 1;"
        cur.execute(sql % usr_id)
        tmp_tpl = cur.fetchall()

        return tmp_tpl
    else:
        tmp_len = int(len_ety * per)
        sql = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND created_at<>4 ORDER BY created_at DESC LIMIT %d;"
        cur.execute(sql % (usr_id, tmp_len))
        tmp_tpl = cur.fetchall()

        return tmp_tpl


def sel_usr(cur, user_id, len_ety, per):
    """
    """

    if len_ety < int(1 / per):
        sql = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND interaction_type<>4 ORDER BY RAND() LIMIT 1;"
        cur.execute(sql % usr_id)
        tmp_tpl = cur.fetchall()

        return tmp_tpl
    else:
        tmp_len = int(len_ety * per)
        sql = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND interaction_type<>4 ORDER BY RAND() LIMIT %d;"
        cur.execute(sql % (usr_id, tmp_len))
        tmp_tpl = cur.fetchall()

        return tmp_tpl

script, tar_file_path, file_par_path = argv

tar_usr = np.loadtxt(tar_file_path, dtype=np.int32)

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="123456", db="xing", charset="UTF8")
cur = conn.cursor()

with open(file_par_path + "/usr_thir.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter="\t")
    spamwriter.writerow(["user_id", "items"])

    for i in range(tar_usr.shape[0]):
        usr_id = tar_usr[i]
    
        sql_1 = "SELECT count(user_id) FROM interactions WHERE user_id=%d AND created_at<>4;" 
        stat = cur.execute(sql_1 % usr_id)
    
        if stat == 0:
                pass
        else:
            len_ety = cur.fetchone()[0]
    
            #tmp_tpl = sel_ti(cur, usr_id, len_ety, per=0.05)
            #tmp_tpl = sel_ti(cur, usr_id, len_ety, per=0.1)
            #tmp_tpl = sel_ti(cur, usr_id, len_ety, per=0.2)
    
            #tmp_tpl = sel_usr(cur, usr_id, len_ety, per=0.05)
            #tmp_tpl = sel_usr(cur, usr_id, len_ety, per=0.1)
            tmp_tpl = sel_usr(cur, usr_id, len_ety, per=0.2)

            # 
            if len(tmp_tpl) == 0:
                continue
            else:
                pass

            usr_id = tmp_tpl[0][0]
            usr_its = ",".join(str(ety[1]) for ety in tmp_tpl)
            spamwriter.writerow([usr_id, usr_its])

        if i % 1000 == 0:
            print(i)
        else:
            pass

conn.commit()

cur.close()
conn.close()
