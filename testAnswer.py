# -*- coding:utf-8 -*


import pymysql,time,os,requests,json,csv



def core_code():
    print(str()+"连接到mysql...")
    db = pymysql.connect(host="40.73.102.21",user="root",passwd="Passw0rdVmw@re!",db="shxh",charset="utf8")
    cursor =db.cursor()

    path = os.getcwd();
    successFile = open(path + '\\' + 'successFile.csv', 'a', encoding='utf-8');
    errorFile = open(path + '\\' + 'errorFileTemp.csv', 'a', encoding='utf-8');

    with open(path + '\\' + 'errorFile.csv', 'r', encoding='utf-8')as f:
        fd = csv.reader(f)
        for index,  rows in enumerate(fd):
            line = rows
            ques=line[0]
            question=line[1]
            sql ="select answer FROM tbl_zjly_yuanju WHERE `type`='0' and status='2' and question = '{}';".format(question)
            print("sql"+sql)
            try:
                cursor.execute(sql)
                res = cursor.fetchone()
                print(res)
                an = str(res[0]).replace("\n", "PPP")
                successFile.write('\n' + ques + "," + question+","+an);
                db.commit()
            except:
                errorFile.write('\n' + ques + "," + question);
    cursor.close()
    db.close()

if __name__ == '__main__':
    start_time = time.clock()
    core_code()
    end_time = time.clock()
    print("一次连接花费的时间%f" % (end_time - start_time))