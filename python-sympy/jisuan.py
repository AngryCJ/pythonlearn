#!/usr/bin/env python
#coding=utf8
import xlwt
import xlrd

from sympy import *

def linear(a,b,y):
    x = symbols('x')
    f = a+b*x-y
    s = solve(f,x)
    res = [x.evalf() for x in s]
    return res


def poly(C,B1,B2,y):
    x = symbols('x')
    f =C+B1*x+B2*x*x-y
    s = solve(f,x)
    res = [x.evalf() for x in s]
    return res

def Exp(y0,A1,t1,y):
    x = symbols('x')
    f=A1*pow(exp(-1/t1),x) + y0-y
    # try:
    s = solve(f,x)
    # except:
    #     print(y0,A1,t1)
    #     return []
    res = [x.evalf() for x in s]
    print(res)
    return res

result={'table1':[],'table2':[],'table3':[],'table4':[],'table5':[],'table6':[]}
with xlrd.open_workbook("参数求解.xlsx") as data:
    with open("result.txt",'w') as f:
        for i in range(1,7):
            table = data.sheet_by_index(i)
            if i == 1 or i == 4: #linear
                f.writelines('page%d\n'%i)
                for i2 in range(0,24):
                    a = table.cell(1+i2*2,2).value
                    b = table.cell(2+i2*2,2).value
                    res = linear(a,b,-20)
                    f.writelines(str(res).replace('[',' ').replace(']',' ')+'\n')
                    result['table%d'%i].append(res)
                    print('page{} linear{}'.format(i,i2))
                f.writelines('\n\n\n\n\n\n')
            elif i ==2 or i == 5: #poly
                f.writelines('page%d\n'%i)
                for i3 in range(0,24):
                    C = table.cell(1+i3*3,2).value
                    B1 = table.cell(2+i3*3,2).value
                    B2 = table.cell(3+i3*3,2).value
                    res = poly(C,B1,B2,-20)
                    f.writelines(str(res).replace('[',' ').replace(']',' ')+'\n')
                    result['table%d'%i].append(res)
                    print('page{} poly{}'.format(i,i3))
                f.writelines('\n\n\n\n\n\n')
            elif i ==3 or i==6:
                f.writelines('page%d\n'%i)
                for i4 in range(0,24):
                    y0 = table.cell(1+i4*3,2).value
                    A1 = table.cell(2+i4*3,2).value
                    t1 = table.cell(3+i4*3,2).value
                    print(y0,A1,t1)
                    res = Exp(y0,A1,t1,-20)
                    f.writelines(str(res).replace('[',' ').replace(']',' ')+'\n')
                    result['table%d'%i].append(res)
                    print('page{} Exp{}'.format(i,i4))
                f.writelines('\n\n\n\n\n\n')
    print(len(result['table1']),len(result['table2']),len(result['table3']),len(result['table4']),len(result['table5']),len(result['table6']))



# print(linear(3.1,2.2,2))
# poly(1,1,1,2)
# Exp(29253.69137,-29255.48214,-75602500,-20)