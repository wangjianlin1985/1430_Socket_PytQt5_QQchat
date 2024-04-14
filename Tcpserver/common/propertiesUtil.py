
from configparser import ConfigParser

class PropertiesUtil:
    #配置文件路径
    filePath="D:\pythonProject\QQ_new\Tcpserver\configfile\dbconfig.properties"
    groupValue="mysql" #配置文件分组

    def __init__(self):
        pass

    @classmethod
    def getConfigObject(cls):
        configObj=ConfigParser()
        configObj.read(PropertiesUtil.filePath)
        return configObj


    @classmethod
    def getConfigValue(cls,key):
        obj=PropertiesUtil.getConfigObject()
        return obj.get(PropertiesUtil.groupValue,key)