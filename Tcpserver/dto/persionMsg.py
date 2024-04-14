from sqlalchemy import Integer,Column,String,Time

from sqlalchemyUtil import Base



class User(Base):
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_qq=Column(Integer)
    qq_password = Column(String(40))
    user_name = Column(String(20))
    user_createtime = Column(Time(True))

    def __repr__(self):
        return self.name
