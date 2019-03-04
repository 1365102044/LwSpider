# import keyword
#
# a = 1
# print(a)
# print('中国')
# print('hello world')
#
# # 关键字
# print(keyword.kwlist)  # da
#
# #单行注释
#
# '''
# 多行注释
# '''
#
# # 多行语句
# total = 'item1' + \
#         'item2' + \
#         'item3'
# print(total)
#
# str = '''
#     dad
#     ddgdg
# '''
# print(str)
# str = '22'
# print(str)
# print(str == total)
#
# # 缩进表示区域块
# if str:
#     print(222)
# else:
#     print(3333)
#
# # r 表示忽略转义符 原句输出
# print('hello\nworld')
# print(r'hello world')
#
#
# # print 默认换行 使用 end=' ' 让其不换行
# a = 'a'
# b = 'b'
# print(a, end=' ')
# print(b, end=' ')
#
# print('\n' + '*' * 20 +'\n')
#
# # 通过 type() 函数得到类型
# num = 100
# fs = 1+2j
# fl = 1.33
# print(type(num),type(fs),type(fl))
#
# # 类型判断 isinstance()
# if isinstance(num,int):
#     print(int)
#
# print('\n' + '*' * 20 +'\n')
#
# '''
# isinstance 和 type 的区别在于：
#     type()不会认为子类是一种父类类型。
#     isinstance()会认为子类是一种父类类型。
# '''
# # eg:
# class A:
#     pass
# class B(A):
#     pass
#
# print(isinstance(A(),A))
# print(type(A()) == A)
# print(isinstance(B(),A))
# print(type(B()) == A)
#
#
# print('\n' +'String'+ '*' * 20 +'\n')
#
# # 字符串截取 变量[头下标:尾下标]
# jiequStr = 'qwertyuiop'
#
# print(jiequStr[0])
# print(jiequStr[2:])
# print(jiequStr[0:-1])
# print(jiequStr[-1:3:-1])
# print(jiequStr[-1:3:1])
#
# # 报错，不能赋值
# # jiequStr[0] = 'w'
# # print(jiequStr)
#
#
# print('\n' + 'List'+'*' * 20 +'\n')
#
# # List  append()、pop() 可以被修改
# list = ['jack','rose',201,2+9j,3.04]
# print(list[:])
# print(list[0:3])
# print(list[0:-1])
#
# print('\n' + 'Tuple'+'*' * 20 +'\n')
#
# # Tuple  不可以被修改
# tuple = ('jack','rose',201,2+9j,3.04)
# print(tuple[:])
# print(tuple[0:3])
# print(tuple[0:-1])
#
#
# print('\n' + 'Set'+'*' * 20 +'\n')
#
# # Set 集合   parame = {value01,value02,...}  或者  set(value)
# #创建一个空的集合
# lwset = set()
# lwset4 = set('3')
# lwset3 = { }
# print(type(lwset),type(lwset3))
# lwset.add(3)
# lwset1 = {3,4,5,5}
# print(lwset)
# print(lwset1)
# print(lwset4)
#
#
# # zhstr = "3465"
# # lwlist = list(zhstr)
# # print(list(zhstr))
# # print(type(list(zhstr)))
# # print(tuple(zhstr))
# # print(type(tuple(zhstr)))
# # print(dict(zhstr))
# # print(type(dict(zhstr)))
#
#
# print('\n' + '随机数'+'*' * 20 +'\n')
# # 随机数
# import random
# # 0-1
# print(random.random())
# # random.choice(sqe)
# print(random.choice((2,3,4,5,7,8)))
# # random.randrange(start,stop,step)  #左闭右开
# print(random.randrange(100))
# print(random.randrange(1,100,2))
#
#
# str5 = 'twut2weqe'
# print(str5.find('w',0,len(str5)))
#
#
#

# from lw.com.demo.test2 import *
#
# print(lwvar)
# a = lwclass()
# a.lwadd()
#
# # lwsum()
#
# from lw.com.demo2.test2_1 import testClass
#
# class2_1 = testClass()
# class2_1.lwadd()


a = '2354'

index = a.find('5')
if index != -1:
    a = a[0:index]
    print(a)