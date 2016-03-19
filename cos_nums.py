import numpy as np
import pymysql
from sys import argv

# 速度：3.4min / 每1万行

script, save_file_path = argv

def fea():
    """5个term文件放在当前目录下
    """
    fea_tms = {}
    tmp_arr = np.loadtxt("d:\\syb\\yun\\jobrec\\feature_ala\\term\\dic_1.txt", 
            dtype=np.int32)
    fea_tms = dict.fromkeys(tmp_arr, 0)

    tmp_arr = np.loadtxt("d:\\syb\\yun\\jobrec\\feature_ala\\term\\dic_2.txt", 
            dtype=np.int32)
    tmp_dic = dict.fromkeys(tmp_arr, 1)
    fea_tms.update(tmp_dic)

    tmp_arr = np.loadtxt("d:\\syb\\yun\\jobrec\\feature_ala\\term\\dic_3.txt", 
            dtype=np.int32)
    tmp_dic = dict.fromkeys(tmp_arr, 2)
    fea_tms.update(tmp_dic)

    tmp_arr = np.loadtxt("d:\\syb\\yun\\jobrec\\feature_ala\\term\\dic_4.txt", 
            dtype=np.int32)
    tmp_dic = dict.fromkeys(tmp_arr, 3)
    fea_tms.update(tmp_dic)

    tmp_arr = np.loadtxt("d:\\syb\\yun\\jobrec\\feature_ala\\term\\dic_5.txt", 
            dtype=np.int32)
    tmp_dic = dict.fromkeys(tmp_arr, 4)
    fea_tms.update(tmp_dic)

    #with open("d:\\syb\\yun\\jobrec\\feature_ala\\re.txt", "r") as tmp_file:

    #    for line in tmp_file.readlines():
    #        line = line.strip()

    #        if len(line) == 0:
    #            continue
    #        else:
    #            buff = line.split(",")
    #            key = int(buff[0])
    #            value = int(buff[1])
    #            fea_tms.update({key: value})

    fea_carr = {1: 5,
            2: 5,
            3: 5,
            4: 5,
            5: 5,
            6: 5}

    fea_dpl = {1: 6,
            2: 7,
            3: 8,
            4: 9,
            5: 10,
            6: 11,
            7: 12,
            8: 13,
            9: 14,
            11: 15,
            12: 16,
            13: 17,
            14: 18,
            15: 19,
            16: 20,
            17: 21,
            18: 22,
            19: 23,
            20: 24,
            21: 25,
            22: 26,
            23: 27}

    fea_cty = {"de": 28,
            "at": 29,
            "ch": 30,
            "non_dach": 31}

    fea_reg = {1: 32,
            2: 33,
            3: 34,
            4: 35,
            5: 36,
            6: 37,
            7: 38,
            8: 39,
            9: 40,
            10: 41,
            11: 42,
            12: 43,
            13: 44,
            14: 45,
            15: 46,
            16: 47}

    fea_idy = {1: 48,
            2: 49,
            3: 50,
            4: 51,
            5: 52,
            6: 53,
            7: 54,
            8: 55,
            9: 56,
            10: 57, 
            11: 58,
            12: 59,
            13: 60,
            14: 61,
            15: 62,
            16: 63,
            17: 64,
            18: 65,
            19: 66,
            20: 67,
            21: 68,
            22: 69,
            23: 70}

    return fea_tms, fea_carr, fea_dpl, fea_cty, fea_reg, fea_idy

fea_tms, fea_carr, fea_dpl, fea_cty, fea_reg, fea_idy = fea()

def sim(cur, usr_id, itm_id):
    """
    """
    usr_fea_vec = np.zeros((71,), dtype=np.int32)
    itm_fea_vec = np.zeros((71,), dtype=np.int32)

    # usr
    sql = "SELECT jobroles, career_level, discipline_id, country, region, industry_id FROM users WHERE id=%d;"
    stat = cur.execute(sql % usr_id)

    if stat == 0:
        print("mysql user feature select error")
    else:
        fea_all = cur.fetchone()
        tms = fea_all[0]
        carr = fea_all[1]
        dpl = fea_all[2]
        cty = fea_all[3]
        reg = fea_all[4]
        idy = fea_all[5]


        for tm in tms.split(","): 

            if tm == "": # 易错
                continue
            else:
                pass

            tm = int(tm)

            if tm == 0:
                continue
            else:

                if tm in fea_tms:
                    usr_fea_vec[fea_tms.get(tm)] = 1
                else:
                    pass

        if carr in fea_carr:
            usr_fea_vec[fea_carr.get(carr)] = 1
        else:
            pass

        if dpl in fea_dpl:
            usr_fea_vec[fea_dpl.get(dpl)] = 1
        else:
            pass

        if cty in fea_cty:
            usr_fea_vec[fea_cty.get(cty)] = 1
        else:
            pass
        
        if reg in fea_reg:
            usr_fea_vec[fea_reg.get(reg)] = 1
        else:
            pass

        if idy in fea_idy:
            usr_fea_vec[fea_idy.get(idy)] = 1
        else:
            pass

    # itm
    sql = "SELECT title, tags, career_level, discipline_id, country, region, industry_id FROM items WHERE id=%d;"
    stat = cur.execute(sql % itm_id)

    if stat == 0:
        print("mysql item feature select error") # may happen
    else:
        fea_all = cur.fetchone()
        tms = fea_all[0] + fea_all[1]
        carr = fea_all[2]
        dpl = fea_all[3]
        cty = fea_all[4]
        reg = fea_all[5]
        idy = fea_all[6]

        for tm in tms.split(","):

            if tm == "": # 易错
                continue
            else:
                pass

            tm = int(tm)

            if tm == 0:
                continue
            else:

                if tm in fea_tms:
                    usr_fea_vec[fea_tms.get(tm)] = 1
                else:
                    pass

        if carr in fea_carr:
            itm_fea_vec[fea_carr.get(carr)] = 1
        else:
            pass

        if dpl in fea_dpl:
            itm_fea_vec[fea_dpl.get(dpl)] = 1
        else:
            pass

        if cty in fea_cty:
            itm_fea_vec[fea_cty.get(cty)] = 1
        else:
            pass
        
        if reg in fea_reg:
            itm_fea_vec[fea_reg.get(reg)] = 1
        else:
            pass

        if idy in fea_idy:
            itm_fea_vec[fea_idy.get(idy)] = 1
        else:
            pass

    cos = np.sum(usr_fea_vec * itm_fea_vec) / np.sqrt(np.sum(usr_fea_vec) 
            * np.sum(itm_fea_vec))

    return cos

# establish connect
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="xing", charset="UTF8")
cur = conn.cursor()

# inintal tmp_arr 
print("inital tmp_arr")

sql = "SELECT DISTINCT user_id, item_id FROM interactions;"
stat = cur.execute(sql)

if stat == 0:
    print("sql execute error")
else:
    tmp_list = cur.fetchall()
    tmp_arr_2 = np.array(tmp_list)
    tmp_arr = np.zeros([len(tmp_list), 5], dtype=np.float64)
    tmp_arr[:, 0:2] = tmp_arr_2

    del tmp_arr_2
    del tmp_list

print("inital tmp_arr: ok")

# calculate feature vector
print("calculate cos, and nums")

line = 0

for ui in tmp_arr:
    usr_id = int(ui[0])
    itm_id = int(ui[1])

    sql_1 = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND item_id=%d AND interaction_type=1;"
    tmp_len = cur.execute(sql_1 % (usr_id, itm_id))
    ui[3] = tmp_len

    sql_2 = "SELECT user_id, item_id FROM interactions WHERE user_id=%d AND item_id=%d AND interaction_type=4;"
    tmp_len = cur.execute(sql_2 % (usr_id, itm_id))
    ui[4] = tmp_len

    cos = sim(cur=cur, usr_id=usr_id, itm_id=itm_id)
    ui[2] = cos

    line += 1

    if line % 1000 == 0:
        print("line: ", line)
    else:
        pass

print("calculate cos and nums: ok")

# close connect
conn.commit()
cur.close()
conn.close()

# save to io
np.savetxt(save_file_path + "/re.csv", tmp_arr, fmt="%f", delimiter="\t")
print("have saved the file to io")
