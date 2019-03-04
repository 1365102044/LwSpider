
#注意点： 前面不能有空格

# 类、继承 多继承

# # 面向对象
# class Person:
#     # 静态变量
#     role = 'person'
#     # 构造方法
#     def __init__(self ,name ,age):
#          self.name = name
#          self.age = age
#
#     def eat(self,food):
#          print('中午吃了：' + food)
#
#     def method(self):
#         print('父类中的method方法' + __class__.__name__)
#
#     # 类方法
#     @classmethod
#     def show(cls):
#          print("点击了类方法！"+cls.role)
#
#     # 销毁时的方法
#     def __del__(self):
#         classname = self.__class__.__name__
#         print(classname + '销毁')
#
# p = Person('jack',23)
# print(p.name,p.age,sep='***')
# print(p.eat('佛跳墙'))
# print(Person.show())
# print(Person.__dict__,Person.__name__)
#
# # 设置、添加属性
# setattr(p,'lwname','32323')
#
# # 访问对象的属性
# print(getattr(p,'lwname'))
#
# #  检查是否存在一个属性
# print(str(hasattr(p,'age')))
# print('是否有lwname属性：'+ str(hasattr(p,'lwname')))
#
# # 删除属性
# delattr(p,'age')
# print('是否有age属性:' + str(hasattr(p,'age')))
#
# print('\n'+'*' * 20 + '\n')
#
# class father:
#     lwname = 'lw'
#     def __init__(self):
#         print('父类的init方法')
#     def method(self):
#         print('父类中的method方法' + __class__.__name__)
#     def setattr(self,attr):
#         father.lwname = attr
#     def getattr(self,attr):
#         print('父类的属性:'+father.lwname)
#
# class son(father,Person):
#     lwage = 23
#     def __init__(self):
#         print('子类的init方法')
#     # def method(self):
#         print('子类中的method方法'+__class__.__name__)
#
# f = father()
# s = son()
# s.method()
# s.setattr('lwname')
# s.getattr('lwname')
# s.method()



# ********************** 闭包 装饰器*********2018年12月06日20:09:52 *******************************

# # 闭包: 外层函数内部定义一个内层函数，并把内层函数当做返回值返回；内层函数里是用了外层函数的变量,那么这个外层函数就是闭包
# def out_func(arg1):
#     def inner_func(arg2):
#         return arg1 + arg2
#     return inner_func
#
# out_f = out_func(1)
# print(out_f(12))
#
#
# # 装饰器
# def func1():
#     print('函数****func1')
# def func2():
#     print('函数****func2')
# def func3():
#     print('函数****func3')
#
# func1()
# func2()
# func3()
#
# # 使用装饰器添加权限检查功能，符合开闭原则（原代码的扩展，不修改原代码）
# def check(funcname):
#     def inner_func():
#         print("权限检查********")
#         funcname()
#     return  inner_func
#
# @check
# def func4():
#     print('函数****func4')
#
# func4()
#
#
#
# def check2(funcname):
#     def inner_func(*para):
#         for ele in para:
#             print('*'*20+ele)
#         funcname()
#     return  inner_func
#
# def check3(funcname):
#     def inner_func(*para):
#         for ele in para:
#             print(ele + '*'*20)
#         funcname()
#     return inner_func
#
# # 使用多个修饰器时，只有最后一个起作用
# @check3
# @check2
# def func5(*para):
#     print('*' * 20 + 'func5' )
#
# func5('3','5','6')
#
#
# # 解除修饰器
#
# import wraps
#
# func5.__wrapped__(3,5)



# ********************** 线程*********2018年12月06日20:09:52 *******************************

'''
Python3中多线程的模块有_thread和threading。
推荐使用threading。
_thread 提供了低级别的、原始的线程以及一个简单的锁，threading 模块包含了 _thread 模块中的所有方法
'''

import threading

class MyThread(threading.Thread):
    def __init__(self,name,count):
        threading.Thread.__init__(self)
        self.name = name
        self.cout = count
    def run(self):
        for ele in range(1,10):
            print('*'*20 + str(ele) + '*'*20 + self.name + '+++' + str(self.cout))

thread1 =  MyThread('thread1',3)
thread2 =  MyThread('thread2',2)
thread3 =  MyThread('thread3',3)
thread1.start()
thread2.start()
thread3.start()
