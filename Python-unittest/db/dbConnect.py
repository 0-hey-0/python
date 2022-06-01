 #!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'YinJia'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from pymysql import connect,cursors
from pymysql.err import OperationalError
import configparser as cparser
from config import readConfig

# --------- 读取config.ini配置文件 ---------------


class DB():
    """
    MySQL基本操作
    """
    def __init__(self,db_name,env):
        cf = readConfig.ReadConfig()
        if env=="test":
            db_info_test = cf.get_db_test()
            host = db_info_test[0]
            port = int(db_info_test[1])
            username = db_info_test[2]
            password = db_info_test[3]
        elif env=="dev":
            db_info_dev = cf.get_db_dev()
            host = db_info_dev[0]
            port = int(db_info_dev[1])
            username = db_info_dev[2]
            password = db_info_dev[3]
        elif env=="c1":
            db_info_c1 = cf.get_db_c1()
            host = db_info_c1[0]
            port = int(db_info_c1[1])
            username = db_info_c1[2]
            password = db_info_c1[3]
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                port=port,
                                user=username,
                                password=password,
                                db=db_name,
                                charset = 'utf8mb4',
                                cursorclass = cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0],e.args[1]))
    def qurey(self,sql):
        cursor=self.conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return result

    # 清除表数据
    def clear(self,table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
             # 取消表的外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.conn.close()

# db=DB(db_name="bus-media",env="dev")
# sql="SELECT * FROM t_words_hot WHERE fd_deleted=0;"
# a=db.qurey(sql)
# print(a)