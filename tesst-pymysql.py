import pymysql;
from pymysql.cursors import DictCursor,SSCursor,SSDictCursor
print('1232')
sql_instance = None

def getConnection():
    if sql_instance is None:
        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='manhand', password='manhand',
                    db='testDB', charset='utf8mb4')
        return conn
    else:
        return sql_instance
    
if __name__ == '__main__':
    conn = getConnection()
    cur = conn.cursor(cursor=DictCursor)
    # 防sql注入
    # 不要使用字符串拼接sql语句，使用参数化
    # 
    val = "1345 or '1'='1'"
    sql_str = "select id,val from tb_test1 where id=%s" % (val)
    sql_str = "select id,val from tb_test1 where id=" + val
    
    cur.execute(sql_str)
    print(cur.fetchall())
    conn.commit()
    
    # cur.execute()
    # cur.fetchall()
    # conn.commit()
    # conn.rollback()
    
    conn.close()
    print(conn)
    
    import os
