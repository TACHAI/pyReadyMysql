import pymysql,os



def core_code():
    db = pymysql.connect(host="localhost",user="root",passwd="778209",db="shxh",charset="utf8")
    cursor =db.cursor()

    sql1 ="""select  FROM tbl_zjly_yuanju WHERE online='0' ;"""
    sql2 ="""select  FROM tbl_shxh_item  li ;"""
    sql3 ="""select  FROM tbl_shxh_office   WHERE online='0' ;"""
    try:
        cursor.execute(sql1)
        res = cursor.fetchall()
        print("执行返回的结果")
        print(res)
        db.commit()
    except:
        print("sql插入错误")
    cursor.close()
    db.close()

if __name__=='__main__':
    core_code()
