"""
"""
# 往长度是300万的表里插入数据，速度大约：2.5min / 每1万条
# 往长度是800万的表里插入数据，速度大约：3.7min / 每1万条

from sys import argv
import csv
import pymysql
from collections import namedtuple

def seek_hstor(csv_file_path, off_set):
    """
    """
    with open(csv_file_path, "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter="\t")
        headers = next(spamreader)
        Row = namedtuple("Row", headers)

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                    passwd='shi520shi', db='xing',charset='UTF8')
        cur=conn.cursor()

        line = 0
        flag = 0

        for r in spamreader:

            if line == off_set or flag == 1:
                flag = 1
                row = Row(*r)

                usr_id = int(row.user_id)
                itm_id = int(row.item_id)
                inter_type = int(row.interaction_type)
                tim = int(row.created_at)

                sql = "SELECT user_id, item_id, interaction_type, created_at FROM interactions WHERE user_id=%d AND item_id=%d AND interaction_type=%d AND created_at=%d;"

                stat = cur.execute(sql % (usr_id, itm_id, inter_type, tim))

                if stat == 0:
                    conn.commit()

                    cur.close()
                    conn.close()

                    return line
                else:
                    line += 1

            else:
                line += 1
                continue

script, csv_file_path = argv

# off_set取上次中断的行数
st_line = seek_hstor(csv_file_path, off_set=3970000)

with open(csv_file_path, "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\t")
    headers = next(spamreader)
    Row = namedtuple("Row", headers)

    # establish connect
    #conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
    #        passwd='shi520shi', db='xing3', charset='UTF8')
    #cur=conn.cursor()

    # store to db part1
    line = 0
    flag = 0

    buffer_count = 0
    buffer_list = []

    for r in spamreader:

        if line == st_line or flag == 1:
            flag = 1

            row = Row(*r)
            usr_id = int(row.user_id)
            itm_id = int(row.item_id)
            typ = int(row.interaction_type)
            tim = int(row.created_at)

            buffer_count += 1

            if buffer_count != 10000:
                buffer_list.append((usr_id, itm_id, typ, tim))
            else:
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                        passwd='shi520shi', db='xing', charset='UTF8')
                cur=conn.cursor()

                sql = "INSERT IGNORE INTO interactions (user_id, item_id, interaction_type, created_at) VALUES (%s, %s, %s, %s);"

                try:
                    cur.executemany(sql, buffer_list)
                except Exception as e:
                    print("dbms error -> line:", line)
                    continue

                conn.commit()
                cur.close()
                conn.close()

                buffer_count = 0
                buffer_list = []

            line +=1
        else:
            line += 1
            continue

        if line % 10000 == 0:
            print("line:", line)
        else:
            pass
    
    # store to db part2
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
            passwd='shi520shi', db='xing', charset='UTF8')
    cur=conn.cursor()

    sql = "INSERT INTO interactions (user_id, item_id, interaction_type, created_at) VALUES (%s, %s, %s, %s);"
    
    try:
        cur.executemany(sql, buffer_list)
    except Exception as e:
        print("dbms error -> final line")

    conn.commit()
    cur.close()
    conn.close()

    print("ok")
