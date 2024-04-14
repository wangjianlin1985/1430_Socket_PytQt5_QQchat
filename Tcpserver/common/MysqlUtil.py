import pymysql
from common.propertiesUtil import PropertiesUtil
'''创建数据库'''

class DBUtil:

    dbconn=None
    cursor = None

    def __init__(self):
        self.dbHost=PropertiesUtil.getConfigValue("Mysql.host")
        self.dbUser=PropertiesUtil.getConfigValue("Mysql.username")
        self.dbPassword = PropertiesUtil.getConfigValue("Mysql.password")
        self.dbPort = PropertiesUtil.getConfigValue("Mysql.port")
        self.dbName = PropertiesUtil.getConfigValue("Mysql.dbname")
        self.dbCharsets = PropertiesUtil.getConfigValue("Mysql.charsets")
        print("mysql config:"+str(PropertiesUtil))

    def initMysql(self):
        try:
            self.dbconn=pymysql.Connect(
                host=self.dbHost,
                port=int(self.dbPort),
                user=self.dbUser,
                passwd=self.dbPassword,
                db=self.dbName,
                charset=self.dbCharsets
            )
            self.cursor=self.dbconn.cursor()
            print("init mysql success" + self.dbconn)
        except Exception as e:
            print("init mysql failed" , e)



    def close(self):
        if self.dbconn==None:
            print("conn already close!")
        else:
            self.cursor.close()
            self.dbconn.close()
            print("conn close success!")


    def insert(self):
        pass

    def select(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass


mysql=DBUtil()
mysql.initMysql()
mysql.close()
    #print(mysql_host)
'''
#打开数据库连接，不需要指定数据库，因为需要创建数据库
conn = pymysql.connect('localhost',user = "root",passwd = "123456")
#获取游标
cursor=conn.cursor()
#创建pythonBD数据库
cursor.execute('CREATE DATABASE IF NOT EXISTS pythonDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
cursor.close()#先关闭游标
conn.close()#再关闭数据库连接
print('创建pythonBD数据库成功')
'''
DBUtil()