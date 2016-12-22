#!/usr/bin/python
#coding=utf8
'''1.Py常用三种设计模式：观察者模式，单例模式，工厂模式介绍
   2.创建 元类 type 介绍
   3. hasattr setattar getattar 介绍
'''

class dingyuezhe():
    '''
    观察者模式-->订阅者，观察者
    '''
    def __init__(self,name):
        self.name = name
    def update(self,message):
        print(str(self.name)+" : "+message)

class poster():
    '''
    观察者模式--> 被观察者，消息发送者
    '''
    def __init__(self,name):
        self.poster = name
        self.list = []
    def adduser(self,user):
        if user.name not in self.list:
            self.list.append(user)
        else:
            print("已经在列表内，无需重复添加")
    def delusr(self,user):
        if user.name in self.list:
            self.list.remove(user)
        else:
            print("不在列表内，无法删除")
    def report(self,message):
        for yonghu in self.list:
            yonghu.update("from china repost  " +message)


class singlemode():
    '''
    单例模式
    '''
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'sig'):
            cls.sig = super().__new__(cls,*args,**kwargs)
        return cls.sig


class monkey():

    '''
    工厂模式类1
    '''
    def run(self):
        print( " mokey run")

class pig():
    '''
    工厂模式类2
    '''
    def run(self):
        print( " pig run")

class duck():
    '''
    工厂模式类3
    '''
    def run(self):
        print( " duck run")

def run(obj):
    '''
    工厂模式共同接口
    :param obj:  类名
    :return:
    '''
    obj.run()


class  mymeta(type):
    '''
    元类 示例

    '''
    def __init__(self,name,base,dict):
       print("init process")
    def __new__(cls, name,base,dict):
       dict['cry']=lambda self:print("I'm cry")
       res = type.__new__(cls, name,base,dict)
       res.company = "acclink"
       return res

class metaexp(metaclass=mymeta):
    '''
    元类 示例
    '''
    pass






if __name__  == "__main__":
    #######################################观察者模式##############################
    youju = poster('china')
    user1 = dingyuezhe('zhangsan')
    user2 = dingyuezhe('lisi')
    user3 = dingyuezhe('wangwu')

    youju.adduser(user1)
    youju.adduser(user2)
    youju.adduser(user3)

    youju.report("今天放假了")

#####################################单例模式########################################

    ba = singlemode()
    bb = singlemode()
    print(id(ba))
    print(id(bb))

########################################工厂模式######################################
    monkey1 = monkey()
    pig1 = pig()
    duck1 = duck()

    run(monkey1)
    run(pig1)
    run(duck1)

######################################元类实例########################################
    metac = metaexp()
    metac.cry()
    print(metac.company)

#######################################hasattar getattar  setattar###################
#可以获得类的变量或者方法名，重新更改方法或者变量都可以