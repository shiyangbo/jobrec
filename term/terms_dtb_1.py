import pymysql
import numpy as np
from sys import argv

# 用户terms：11964
# 物品terms：96522
# 交集：10671

def usr_t(cur):
    """
    """
    sql = "SELECT jobroles FROM users;"
    cur.execute(sql)
    tmp_list = cur.fetchall()

    usr_terms = {}

    for ety in tmp_list:
        #str = ety[0].strip().split(",")
        tmp_str = ety[0].split(",")

        if len(tmp_str) == 1:
            #n += 1
            continue
        else:

            for term in tmp_str:

                if term in usr_terms:
                    usr_terms[term] = usr_terms.get(term) + 1
                else:
                    usr_terms.update({term: 1})

    return usr_terms

def itm_t(cur):
    """
    """
    sql = "SELECT title, tags FROM items;"
    cur.execute(sql)
    tmp_list = cur.fetchall()

    itm_terms = {}

    for ety in tmp_list:
        tmp_str = ety[0].split(",") 
        tmp_str.extend(ety[1].split(","))

        if len(tmp_str) == 0:
            continue
        elif len(tmp_str) == 1:
            continue
        else:

            for term in tmp_str:

                if term == "":
                    continue
                else:

                    if term in itm_terms:
                        itm_terms[term] = itm_terms.get(term) + 1
                    else:
                        itm_terms.update({term: 1})

    return itm_terms

script, file_path = argv

# establish connect
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="shi520shi",
        db="xing", charset="UTF8")
cur = conn.cursor()

# terms distribute
usr_terms = usr_t(cur)
conn.commit()

itm_terms = itm_t(cur)
conn.commit()

inter = dict.fromkeys([k for k in usr_terms if k in itm_terms])

usr_list = []
itm_list = []

for k in inter:
    usr_list.append([int(k), int(usr_terms.get(k))])
    itm_list.append([int(k), int(itm_terms.get(k))])

usr_list.sort(key = lambda x : x[1], reverse=True)
itm_list.sort(key = lambda x : x[1], reverse=True)
np.savetxt(file_path + "/u.txt", np.array(usr_list), fmt="%s", delimiter="\t")
np.savetxt(file_path + "/i.txt", np.array(itm_list), fmt="%s", delimiter="\t")

# close connect
cur.close()
conn.close()


