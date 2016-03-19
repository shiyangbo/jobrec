import pymysql

# establish connect
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="xing", charset="UTF8")
cur = conn.cursor()

sql_1 = "SELECT user_id, item_id FROM interactions WHERE user_id=2882142 AND item_id=88 AND interaction_type=1;"
tmp_len = cur.execute(sql_1)
print(tmp_len)

# close connect
conn.commit()
cur.close()
conn.close()

