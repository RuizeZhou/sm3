#coding:utf-8
def left(x,times):#循环左移
    return x[times:]+x[:times]


def XOR2(a,b):#二进制的异或，返回二进制数
    return '{1:0{0}b}'.format(len(a), int(a, 2) ^ int(b, 2))
def AND2(a, b):
    return '{1:0{0}b}'.format(len(a), int(a, 2) & int(b, 2))
def OR2(a, b):
    return '{1:0{0}b}'.format(len(a), int(a, 2) | int(b, 2))
def NOT2(a):
    result = ''
    for ch in a:
        if ch == '1':
            result = result + '0'
        else:
            result = result + '1'
    return result


def P1(x):
    return XOR2(XOR2(x,left(x,15)),left(x,23))
def P0(x):
    return XOR2(XOR2(x,left(x,9)),left(x,17))

def FF(x,y,z,j):
    if(j>=0)&(j<=15):
        return XOR2(XOR2(x,y),z)
    else:

        return OR2( OR2(AND2(x,y), AND2(x,z)) , AND2(y,z))

def GG(x,y,z,j):
    if(j>=0)&(j<=15):
        return XOR2(XOR2(x,y),z)
    else:
        return OR2(AND2(x,y),AND2(NOT2(x),z))
