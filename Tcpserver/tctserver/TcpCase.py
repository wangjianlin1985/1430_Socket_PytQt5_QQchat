
from socket import *

class TcpCase:
    tcp_address = '127.0.0.1';
    tcp_lport = 6337;
    buffsize = 1024;
#实现socket
    s = socket(AF_INET, SOCK_STREAM);
    s.bind((tcp_address, tcp_lport));
    s.listen(10);

    @classmethod
    def getTcpSocket(self):
        print("TcpSocket start:"+str(self.s))
        return self.s;

#返回tcpCase单例
tcpSocket=TcpCase.getTcpSocket();
