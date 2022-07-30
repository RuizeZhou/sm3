# 项目说明

**1.小组成员**：周睿泽。git账户名称：RuizeZhou

**2,所作项目名称：**

本项目名称为：Project: do your best to optimize SM3 implementation (software)

简介：实现国密sm3，编程语言为python。

完成人：周睿泽

**3.清单：**

完成的项目：

√Project: implement the naïve birthday attack of reduced SM3 

√Project: implement the Rho method of reduced SM3

√Project: implement length extension attack for SM3, SHA256, etc.

√Project: do your best to optimize SM3 implementation (software)

√Project: Impl Merkle Tree following RFC6962

√Project: report on the application of this deduce technique in Ethereum with ECDSA

√Project: Implement sm2 with RFC6979

√Project: verify the above pitfalls with proof-of-concept code

√Project: Implement a PGP scheme with SM2

未完成的项目：

Project: Try to Implement this scheme

Project: Implement the above ECMH scheme

Project: implement sm2 2P sign with real network communication

Project: implement sm2 2P decrypt with real network communication

Project: PoC impl of the scheme, or do implement analysis by Google

Project: forge a signature to pretend that you are Satoshi

Project: send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself

Project: forge a signature to pretend that you are Satoshi

Project: research report on MPT

Project: Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.

有问题的项目及问题：\

**4.本项目具体内容：**  具体内容如下

## sm3

### A.具体的项目代码说明

sm3哈希算法主要分为几个部分。首先要进行填充。然后通过迭代来循环进行哈希操作。

Iteration具体包括消息拓展函数和压缩函数，根据国密说明文件中的步骤编写代码即可得到：

```
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
        for k in range(64):
            W[k+68]=utils.XOR2(W[k],W[k+4])
        return W        
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
```

最后一轮输出256比特的杂凑值y=ABCDEFGH





### B.运行指导

​	导入同目录下的utils包，直接运行即可测试样例。

### C.代码运行全过程截图(无截图无说明的代码不给分)
以输入消息'abc'为例，输出哈希值如下：

![image-20220731045722378](https://cdn.jsdelivr.net/gh/RuizeZhou/images/image-20220731045722378.png)

### D.每个人的具体贡献说明及贡献排序(复制的代码需要标出引用)

​	本人负责全部。


