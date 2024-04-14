import sqlalchemy
from sqlalchemy.orm import session ,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,Time

from common.propertiesUtil import PropertiesUtil

import pymysql
pymysql.install_as_MySQLdb()

Base=declarative_base()

class SqlSession:

    dbHost = PropertiesUtil.getConfigValue("Mysql.host")
    dbUser = PropertiesUtil.getConfigValue("Mysql.username")
    dbPassword = PropertiesUtil.getConfigValue("Mysql.password")
    dbPort = PropertiesUtil.getConfigValue("Mysql.port")
    dbName = PropertiesUtil.getConfigValue("Mysql.dbname")
#    engine=sqlalchemy.create_engine("mysql://"+dbUser+":"+dbPassword+"@"+dbHost+":"+dbPort+"/"+dbName,
#                             encoding='utf8',echo=True)
    def __init__(self):
        try:
            self.engine = sqlalchemy.create_engine(
                "mysql://" + self.dbUser + ":" + self.dbPassword + "@" + self.dbHost + ":" + self.dbPort + "/" + self.dbName,
                encoding='utf8', echo=True)
            self.Dbsession = sessionmaker(bind=self.engine)
        except Exception as e:
            print("init mysqlDB failed ---reason:"+e)
    #        print(self.dbName)

    def initDB(self):
        try:
            Base.metadata.create_all(self.engine)
            return True
        except Exception as e:
            print("init mysqlDB failed ---reason:" + e)
            return False

    def getSession(self):
        return self.Dbsession()

    def isConnectMysql(self):
        try:
            self.initDB()
        except Exception as e:
            print("init mysqlDB failed ---reason:" + e)


class Group(Base):

    __tablename__="group_info"

    group_id=Column(Integer,primary_key=True,autoincrement=True)
    group_name=Column(String(20))
    group_creater=Column(String(20))
    group_createtime=Column(Time(True))

    # def __repr__(self):
    #     return self.name

class User(Base):
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_qq=Column(Integer)
    qq_password=Column(String(40))
    user_name = Column(String(20))
    user_createtime = Column(Time(True))

    # def __repr__(self):
    #     return self.name

class UserGroupRelation(Base):

    __tablename__="user_group_relation"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(String(20))
    group_id=Column(String(20))
    user_qq = Column(String(20))
    group_name = Column(String(20))
    relation=Column(Integer) #1.用户为群主；2.用户为群内人员
    relation_createtime=Column(Time(Time))

    # def __repr__(self):
    #     return self.name

# if __name__=='__main__':
#     session=SqlSession()
#     session.initDB()
#     s=session.getSession()
    # group1=Group(group_name="同学群",group_creater="2097557614")
    # group2 = Group(group_name="test群1", group_creater="2097557614")
    # group3 = Group(group_name="test群2", group_creater="2097557616")

    # user1=User(user_qq=2097557614,qq_password=123456,user_name="jjl")
    # user2 = User(user_qq=2097557615, qq_password=123456, user_name="test1")
    # user3=User(user_qq=2097557616,qq_password=123456,user_name="test2")
    #
    # relation1=UserGroupRelation(user_id=1,group_id=1,relation=1)
    # relation2 = UserGroupRelation(user_id=2, group_id=2, relation=2)
    # relation3 = UserGroupRelation(user_id=3, group_id=3, relation=2)
    # s.add_all([relation1,relation2,relation3])
    # s.commit()
    # s.close()

