#coding:utf-8
#22/05/15  Ruize Zhou
import utils
IV='7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e'

class sm3:
    def __init__(self , words):#先不考虑接收服务器的数据。    #客户端的元素words:List
        afterfill=self.Fill(words)
        self.end=self.Iteration(afterfill)


    def Fill(self,msg):
        if msg.isalpha():
            msg_bin=''.join([bin(ord(c)).replace('0b', '0') for c in msg]) #字母ASCII：65-122，2^6=64 2^7=128，7位可表示，添一位
        # else:#十六进制
        #     msg_bin=''.join( [ bin(int(msg[i:i+2],10)).replace('0b', '00')   for i in range(len(msg)//16)])
        else:
            raise ValueError("plz input msg with alpha")
        length=bin(len(msg_bin))[2:]


        #+1
        msg_bin+='1'

        #+0
        # len0=   #这里可以直接计算一下。。也可以循环填入
        while len(msg_bin)%512 !=448:
            msg_bin+='0'

        #+len(msg)
        msg_bin=msg_bin+'0'*(64-len(length))+length
        return msg_bin


    #消息拓展
    def expand(self,msg_bin):
        W={}
        for i in range(16):
            W[i]=msg_bin[i*32:(i+1)*32]
        for j in range(16,68):
            y2=utils.XOR2(W[j-16],W[j-9])
            y3=utils.XOR2(y2,utils.left(W[j-3],15))
            y4=utils.P1(y3)
            y5=utils.XOR2(y4,utils.left(W[j-13],7))
            y6=utils.XOR2(y5,W[j-6])
            W[j]=y6

            # y1=P1(XOR2(XOR2(W[j-16],W[j-9]),left(W[j-3],15)))
            # W[j]=XOR2(XOR2(y1,left(W[j-13],7)),W[j-6])

        for k in range(64):
            W[k+68]=utils.XOR2(W[k],W[k+4])


        return W



    def Iteration(self,m):#输入二进制字符串
        V={}
        V[0]=IV
        n=len(m)//512
        B={}
        for i in range(n):
            B[i]=m[i*512 : (i+1)*512]
            W=self.expand(B[i])

            V[i+1]=self.compress(V[i],W)
        return V[n]

    def compress(self,V,W):
        A = bin(int(V[0:8],16))[2:].zfill(32)#不足32要填充0
        B = bin(int(V[8:16],16))[2:].zfill(32)
        C = bin(int(V[16:24],16))[2:].zfill(32)
        D = bin(int(V[24:32],16))[2:].zfill(32)
        E = bin(int(V[32:40],16))[2:].zfill(32)
        F = bin(int(V[40:48],16))[2:].zfill(32)
        G = bin(int(V[48:56],16))[2:].zfill(32)
        H = bin(int(V[56:64],16))[2:].zfill(32)

        for j in range(64):
            if j<=15:
                Tj =bin(int('79cc4519',16))[2:].zfill(32)
            else:
                Tj =bin(int('7a879d8a',16))[2:].zfill(32)

            tmp=(int(utils.left(A,12),2)+int(E,2)+int(utils.left(Tj,j%32),2))%(2**32)
            SS1=utils.left(bin(tmp)[2:].zfill(32),7)

            SS2=utils.XOR2(SS1,utils.left(A,12))

            tmp=(int(utils.FF(A,B,C,j),2)+int(D,2)+int(SS2,2)+int(W[j+68],2))%(2**32)
            TT1=bin(tmp)[2:].zfill(32)


            tmp=(int(utils.GG(E,F,G,j),2)+int(H,2)+int(SS1,2)+int(W[j],2))%(2**32)
            TT2=bin(tmp)[2:].zfill(32)


            D=C
            C=utils.left(B,9)
            B=A
            A=TT1
            H=G
            G=utils.left(F,19)
            F=E
            E=utils.P0(TT2)


        tmp=A+B+C+D+E+F+G+H
        V=bin(int(V,16))[2:]
        return hex(int(utils.XOR2(tmp,V), 2))[2:]

    @property
    def label(self):
      return self.end





if __name__=='__main__':
    message='abc'
    # message='abcd'*16

    print(sm3(message).label)

