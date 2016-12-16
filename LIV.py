#!/usr/bin/env python
#coding=utf8
import xlrd
def readexcel(num):
    with xlrd.open_workbook('%s 2016-11-1原始数据.xls'%(str(num).zfill(2))) as data:
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
            # print(sheet)
            # print(len(sheet[0]),len(sheet[1]),len(sheet[2]),len(sheet[3]),len(sheet[4]))
    return sheet



if __name__=="__main__":
    a = readexcel(31)
    print(a)
    print(len(a[0]),len(a[1]),len(a[2]),len(a[3]),len(a[4]))