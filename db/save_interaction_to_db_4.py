# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:01:31 2016

@author: liwj0
"""

import csv
import pymysql
from collections import namedtuple
from sys import argv

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

# off_set设为(line-10000), line为上次中断显示的最后行数
st_line = seek_hstor(csv_file_path, off_set=3970000)

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='shi520shi',
        db='xing',charset='UTF8')
cur=conn.cursor()

with open(csv_file_path,'r') as f:
    spamreader = csv.reader(f,delimiter='\t')
    headers = next(spamreader)
    Row = namedtuple('Row',headers)

    n = 0
    flag = 0

    for r in spamreader:
        row = Row(*r)
        
        if n == st_line or flag == 1:
            flag = 1

            sql = "INSERT IGNORE INTO `interactions` (user_id,item_id,interaction_type,created_at) VALUES ('%d', '%d', '%d','%d')" %\
            (int(row.user_id),int(row.item_id),int(row.interaction_type),int(row.created_at))
                
            cur.execute(sql)

            n += 1
        else:
            n += 1
            continue

        if n % 10000 == 0:
            conn.commit()
            print("line:", n)
        else:
            pass

conn.commit()
      
cur.close()
conn.close()    

print("ok")
