
name="liming"
import logging
# class Foo(object):
#     def __init__(self,func):
#         self._func = func
#
#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')
#
# @Foo
# def bar():
#     print ('bar')
#
# bar()
#
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#     return decorator
#
# @use_logging(level="warn")
# def foo(name):
#     print("i am %s" % name)
#
# # foo=use_logging(level="warn")(foo)
# foo('aa')


####Yong3.zhou
# level=["OFF"]
# def decorator(func):
#     def wrapper(*args, **kwargs):
#             if level[0] == "OFF":
#                 return func(*args)
#             else:
#                 pass
#     return wrapper
#
# @decorator
# def aa():
#     print("aa")
#     return('OFF')
#
# @decorator
# def bb():
#     print("bb")
#     return('ON')
#
# @decorator
# def cc():
#     print("cc")
#     return('ON')
#
# # try:
# #     level[0]=aa()
# #     level[0]=bb()
# #     level[0]=cc()
# # except:
# #     print("error")
####Yong3.zhou


def aa():
    print("aa")
    return('OFF')

def bb():
    print("bb")
    return('ON')

def cc():
    print("cc")
    return('ON')
def fun():
    try:
        aa()
        return
        bb()
    except:
        print("error")

fun()