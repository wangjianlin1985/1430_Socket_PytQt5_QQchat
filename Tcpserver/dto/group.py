
from sqlalchemy import Integer,Column,String,Time

from sqlalchemyUtil import Base
from sqlalchemy.ext.declarative import declarative_base

class Group(Base):

    __tablename__="group_info"

    group_id=Column(Integer,primary_key=True,autoincrement=True)
    group_name=Column(String(20))
    group_creater=Column(String(20))
    group_createtime=Column(Time(True))

    def __repr__(self):
        return self.name



