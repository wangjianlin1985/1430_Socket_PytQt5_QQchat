
from TcpCase import tcpSocket
import socket
from threading import Thread

from QQTcpServerLogin import QQTcpLogin
from common.sqlalchemyUtil import SqlSession,UserGroupRelation



class TcpServer:
    socketList = {}
    onlineSocket={}
    sqlSession = SqlSession().getSession()
    def startTcpServer(self):
        print("TcpServer is starting")
        while True:
            cSocket,ipAdress=tcpSocket.accept()
            print("--recv socket connect request:" + str(cSocket) + " ip:" + str(ipAdress))
            self.socketList[ipAdress]=cSocket
            try:
                Thread(target=self.socketThread,args=(cSocket,ipAdress)).start()
            except Exception as e:
                print("--clietn socket:"+str(cSocket)+" ip:"+str(ipAdress)+" is unusal/unconnet!")
                print("Exception:"+str(e))

            print("--all socket connect:"+str(self.socketList))
        self.socketClose()

    def socketThread(self,clientsock,clientaddress):
        while True:
            recvMsg=clientsock.recv(1024).decode('utf-8').split(" ")
            msgIdentifcation=recvMsg[0]
            #print(msgIdentifcation+" :"+str(type(recvMsg)))
            if not recvMsg:
                self.socketList.pop(clientaddress)
                print("qq已下线！")
            elif msgIdentifcation=='login':
                login=QQTcpLogin()
                res=login.loginCheck(recvMsg[1],recvMsg[2])
                if res=="true":
                    self.onlineSocket[recvMsg[1]]=clientsock
                    print(recvMsg[1]+" is login success")
                clientsock.send(res.encode())
            elif msgIdentifcation=='personal':
                print("private msg:"+str(recvMsg))
                self.privateMessage(recvMsg[2],recvMsg[1]+":"+recvMsg[3],clientsock)
            elif msgIdentifcation == 'groupchat':
                print("group msg:" + str(recvMsg))
                self.groupMessage(recvMsg[1],recvMsg[2]+":"+recvMsg[3])
            elif msgIdentifcation=='register':
                login = QQTcpLogin()
                resgisterRes = login.register(recvMsg[1],recvMsg[2])
                clientsock.send(resgisterRes.encode())

            else:
                print("收到信息:"+str(recvMsg)+" 此信息无法识别！")

    def socketClose(self):
        return tcpSocket.close()

    def privateMessage(self,accepter,sendMsgs,cSocket):
        try:
            print(str(self.onlineSocket.get(accepter))+accepter)
            if self.onlineSocket.get(accepter):
                self.onlineSocket[accepter].send(sendMsgs.encode())
                cSocket.send(sendMsgs.encode())
            else:
                msg=accepter+" 不在线！"
                cSocket.send(msg.encode())
        except Exception as e:
            print("private chating exception" +e)

    def groupMessage(self,group,sendMsgs):
        try:
            group_qqs=self.sqlSession.query(UserGroupRelation).filter(UserGroupRelation.group_name==group).all()
            for relatoin in group_qqs:
                if self.onlineSocket.__contains__(relatoin.user_qq):
                    self.onlineSocket[relatoin.user_qq].send(sendMsgs.encode())
                else:
                    print(group+" member " +relatoin.user_qq+ " isn't online!")
#            print(group_qqs)
        except Exception as e:
            print("Group chating exception" +str(e))



if __name__=='__main__':

    if SqlSession().initDB():
        TcpServer().startTcpServer()
        #TcpServer().groupMessage("","","")
    else:
        print("TcpServer start failed! The reason is mysql no runing ")

