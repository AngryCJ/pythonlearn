#!/usr/bin/env python
#coding=utf8

import urllib.parse
import urllib.request
import re
import os
import time



class pachong():
    def __init__(self,url,num,pattern):
        self.url = url
        self.num = num
        self.pattern = pattern
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"}

    def ReadWeb(self,url):
        request = urllib.request.Request(url=url,headers=self.header)
        return urllib.request.urlopen(request).read().decode()

    def regedit(self,str):
        compil=re.compile(self.pattern,re.S)
        return re.findall(compil,str)

    def __call__(self, *args, **kwargs):
        pages = []
        print("Spider Start....\n")
        for i in range(self.num):
            try:
                page = self.regedit(self.ReadWeb(self.url%(str(i+1))))
                pages.append(page)
                print("spider on ------>--------> page {}".format(str(i+1)))
            except:
                print("爬page{}出现错误....".format(str(i+1)))
            time.sleep(0.5)
            print(page)
        # print(len(pages))
        print("\nSpider End....")
        return pages

class txtsave():
    def __init__(self,path,list):
        self.path = path
        self.num1 = 0
        self.num2 = 1
        self.list = list

    def __call__(self, *args, **kwargs):
        print("开始保存数据....")
        x = 0
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        for i1 in range(len(self.list)):
            for i2 in range(len(self.list[i1])):
                file_path = (self.path + '/' +'teachers.txt')
                d = urllib.parse.quote(self.list[i1][i2][2])
                imgurl = 'http://www.maiziedu.com/'+d
                try:
                    urllib.request.urlretrieve(imgurl,self.path + '/'+'%s.jpg'% self.list[i1][i2][0])
                except:
                    print(imgurl,self.list[i1][i2][1])
                with open(file_path,'a',encoding='utf-8') as f:
                    a = '老师姓名： '+self.list[i1][i2][0]+'\n'+'编号： '+self.list[i1][i2][1]+'\n'+'导师简介：'+self.list[i1][i2][3]+'\n\n'
                    f.writelines(a)
                    x+=1
        print("保存数据完成....")
        print(x)

if __name__ == '__main__':
    pattern = '<a title="(.*?)" href="/u/(\d*?)/"><img alt=".*?" src="(.*?)"></a>.*?<p class="color66"><span class="color99">简介：</span>(.*?)</p>'
    spider = pachong("http://www.maiziedu.com/course/teachers/?page=%s",27,pattern)
    webinfo = spider()
    txt = txtsave('MZteachers',webinfo)
    txt()