开发软件： Pycharm + Python3.6    数据库：mysql8.0

  本软件基于python gui图形库pyqt5编写的仿qq，采用mysql数据库存储，socket通信（tcp协议）实现，支持多账号登录，注册，单人私聊，群聊，添加好友分组等功能。
  
（1）客户端界面目录文件：pyqt5-qq,服务端目录文件：Tcpserver
（2）服务端目录结构:

common：存放公共的工具类代码文件目录，主要是配置文件解析工具类，数据库操作工具类，本软件主要使用的是sqlalchemy orm数据库框架。
configfile:存放配置文件目录
dto:存放数据库表模型类代码文件

（3）客户端目录结构:
image,res:存放资源文件
其他文件：界面及逻辑实现源码
