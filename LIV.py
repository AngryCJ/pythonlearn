#!/usr/bin/env python
#coding=utf8
import xlrd
from functools import reduce
def readexcel(num):
    try:
        with xlrd.open_workbook('/media/chongjie/项目/python/LearnPython/%s 2016-11-1原始数据.xls'%(str(num).zfill(2))) as data:
                table = data.sheet_by_index(0)
                sheet = []
                for n in range(5):
                    shuju = []
                    for i in range(800):
                        try:
                            data = table.cell(i,n).value
                        except:
                            break
                        else:
                            if data !='':
                                shuju.append(data)
                            else:
                                pass
                    sheet.append(shuju)
                # print(len(sheet[0]),len(sheet[1]),len(sheet[2]),len(sheet[3]),len(sheet[4]))
                num1 = len(sheet[1])
                num2 = len(sheet[2])
                num3 = len(sheet[3])
                num4 = len(sheet[4])

                # datax = []
                # datax.append(sheet[0][0:num1])
                # datax.append(sheet[0][num1:num1+num2])
                # datax.append(sheet[0][num1+num2:num1+num2+num3])
                # datax.append(sheet[0][num1+num2+num3:num1+num2+num3+num4])
                # print(datax)

                diyizu = [sheet[0][0:num1],sheet[1]]
                dierzu = [sheet[0][num1:num1+num2],sheet[2]]
                disanzu = [sheet[0][num1+num2:num1+num2+num3],sheet[3]]
                disizu = [sheet[0][num1+num2+num3:num1+num2+num3+num4],sheet[4]]

                excel=[diyizu,dierzu,disanzu,disizu]

        return excel
    except:
        print("文件不存在")
        exit()
def LSM(x,y,m,n):
    """
    最小二乘法算法
    :param x: 横纵坐标
    :param y: 纵轴坐标
    :param m: 返回的结果变量组数，若需返回4次方程，m为5
    :param n:采样点数
    :return:返回各次方的系数，最大次方的系数在最后面
    """
    B=[0.0]*n
    T=[0.0]*n
    S=[0.0]*n
    COF=[0.0]*m

    if n!=len(x) or n!=len(y):return ''
    if m>n:m=n
    for i in range(m):
        COF[i]=0
    Z=0
    B[0]=1
    D1=n
    P=0
    C=0

    for i in range(n):
        P = P + x[i] - Z
        C = C + y[i]

    C = C / D1
    P = P / D1
    COF[0] = C * B[0]

    if m > 1:
        T[1] = 1
        T[0] = -1*P
        D2 = 0
        C = 0
        G = 0
        for i in range(n):
            Q = x[i] - Z - P
            D2 = D2 + Q * Q
            C = y[i] * Q + C
            G = (x[i] - Z) * Q * Q + G
        C = C / D2
        P = G / D2
        Q = D2 / D1
        D1 = D2
        COF[1] = C * T[1]
        COF[0] = C * T[0] + COF[0]

    for j in range (2 ,m):
        S[j] = T[j - 1]
        S[j - 1]= -P * T[j - 1] + T[j - 2]
        if j >= 3:
            for k in range(j - 2,0,-1):
                S[k] = -1*P * T[k] + T[k - 1] - Q * B[k]
        S[0] = -1*P * T[0] - Q * B[0]
        D2 = 0
        C = 0
        G = 0
        for i in range(n):
            Q = S[j]
            for k in range(j - 1, -1,-1):
                Q = Q * (x[i] - Z) + S[k]
            D2 = D2 + Q * Q
            C = y[i] * Q + C
            G = (x[i] - Z) * Q * Q + G
        C = C / D2
        P = G / D2
        Q = D2 / D1
        D1 = D2
        COF[j] = C * S[j]
        T[j] = S[j]
        for k in range(j - 1,-1,-1):
            COF[k] = C * S[k] + COF[k]
            B[k] = T[k]
            T[k] = S[k]
    return COF


class  LIV():
    def __init__(self,dataxy):
        self.datax1 = dataxy[0]
        self.datay1 = dataxy[1]
        self.final = []
        self.finalx = []
        self.finaly = []


    def smooth(self,datax,datay,num=2):
        self.num = num
        datax2 = [(reduce(lambda x,y:x+y,datax[a:a+self.num]))/self.num for a in range(len(datax)-self.num+1)]
        datay2 = [(reduce(lambda x,y:x+y,datay[a:a+self.num]))/self.num for a in range(len(datay)-self.num+1)]
        return [datax2,datay2]

    def diff(self,datax,datay):
        datax3 = [(datax[a]+datax[a+1])/2 for a in range(len(datax)-1)]
        datay3 = [(datay[a+1]-datay[a]) for a in range(len(datax)-1)]
        return [datax3,datay3]

    def chuli(self):
        final1 = self.smooth(self.datax1,self.datay1)
        final2 = self.diff(final1[0],final1[1])
        final3 = self.smooth(final2[0],final2[1])
        final4 = self.diff(final3[0],final3[1])
        self.finalx = final4[0]
        self.finaly = final4[1]
        # print(final4)
        return final4


    def __call__(self, *args, **kwargs):
        self.chuli()
        max1 = max(self.finaly)
        maxindex = self.finaly.index(max1)
        xishu = [self.finalx[maxindex-1:maxindex+2],self.finaly[maxindex-1:maxindex+2]]
        # print(maxindex,len(self.finalx),len(self.finaly))
        try:
            EOF = LSM(xishu[0],xishu[1],3,len(xishu[0]))
        except:
            print("数据有误")
            exit()
        yuzhi = -1*EOF[1]/(2*EOF[2])

        if max(self.finaly)>5:
            for i in range(20):
                del self.finalx[maxindex]
                del self.finaly[maxindex]
                max2 = max(self.finaly)
                if max2>5: continue
                maxindex = self.finaly.index(max2)
                xishu1 = [self.finalx[maxindex-1:maxindex+2],self.finaly[maxindex-1:maxindex+2]]
                # print(maxindex,len(self.finalx),len(self.finaly))
                try:
                    EOF1 = LSM(xishu1[0],xishu1[1],3,len(xishu1[0]))
                except:
                    print("数据有误")
                yuzhi1 = -1*EOF1[1]/(2*EOF1[2])
                return [yuzhi,max1,yuzhi1,max2]

        return [yuzhi,max1]

if __name__=="__main__":
    a = readexcel(7)
    # print(a[2])
    # result = LIV(a[2])
    # result()
    result = [LIV(a[i])() for i in range(4)]
    # print(result.finalx,result.finaly)
    print(result)

