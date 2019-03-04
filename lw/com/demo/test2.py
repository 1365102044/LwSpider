import requests
from lxml import html
# url='https://movie.douban.com/' #需要爬数据的网址
# page=requests.Session().get(url)
# tree=html.fromstring(page.text)
# print(page.text)

# result=tree.xpath('//td[@class="title"]//a/text()')
# result2=tree.xpath('//li[@class="title"]//a/text()')
# print(result)
# print(result2)

# str1 = "23234546"
# print('2' in str1)
#
# str2 =  input()
# print(str2)
#
# str3 = input()
# eval(str3)

# for s in range(1,3):
#     print(s)
#
#
# # 输出到文件中 open('文件路径','写入模式')
# f = open("test.text","a+")
# print('3232324545',file=f)
#
#
# '''
# 完整函数：print(values, sep, end, file, flush)
# values：需要输出的值，有多个值使用,进行分隔
# sep：分隔符，默认使用空格进行分隔
# end：输出完毕后添加的字符，默认是\n
# file：默认是显示器，也可以指定文件
# flush：刷新缓冲区，进行立刻输出,默认false
# '''
# num = 32
# print('%10d'% num)
# print('%10d' % num)
#
# print('{1}:{0}'.format (100,200))


# 时间
import time


# str3 = time.time()
# str4 = time.localtime()
# str5 = time.asctime()
# str6 = time.strftime('%Y-%m-%d %H:%M:%S')
# time.sleep(1)
# print(str3,str4.tm_year,str5,str6,sep='****')


# ************************ 函数 *******2018年12月06日20:09:52 *******************************

# def sum(a, b):
#     return a + b
#
#
# print(sum(2, 5))
# print(sum(a=3, b=4))
#
#
# # 不定参数  (*参数)
# def sum2(*param):
#     s: int = 0;
#     for v in param:
#         s += v
#     return s
#
#
# print(sum2(2, 4, 5, ))
#
#
# # 加了两个星号 ** 的参数会以字典的形式导入。
# def printInfo(**dict):
#     print(dict)
#
#
# printInfo(lwname='jack', age=4)
#
#
# def prinSum(a, b, *, c):
#     return a + b + c
#
#
# print(prinSum(2, 4, c=5),end='***')

# # 匿名函数 格式：lambda [arg1 ,arg2,.....argn]:expression
# sum3 = lambda a, b: a + b
# print(sum3(2, 4))


# # 把局部变量的作用域变成全局作用域 global
# num = 1
# def func1():
#     global  num
#     print(num)
#     num = num + 1
#     print(num)
# func1()
#
#
# # 把变量的作用域从内层函数变成外层函数 nonlocal
# def func2():
#     a1 = 1
#     print(a1,id(a1))
#     def innerfunc():
#         nonlocal a1
#         a1 = 100
#         print(a1,id(a1))
#     innerfunc()
# func2()
#
#
# # 注意：这种会报错，会认为引用未定义的局部变量
#
# a2 = 1
# def fun3():
#     a = a + 1


# ************************ 文件操作 *******2018年12月06日20:09:52 *******************************

# file_w = open('test.text','w')
# file_w.write('123456')
# file_w.write('1234567')
#
# # writelines 可以写入多段文本
# list1 = []
# list1.append('\none\n')
# list1.append('two\n')
# file_w.writelines(list1)
# # 写入的文本，需要刷新，才能后面才能读取，否则，下面读取不到，等到执行完毕，才刷新
# file_w.flush()
#
# # 读取文件 read 后不能读取
# file_r = open('test.text','r',encoding='utf-8')

# str_r = file_r.read()
# print(str_r)

# str_r1 = file_r.readline()
# print(str_r1)
#
# str_r2 = file_r.readlines()
# print(str_r2)
# file_r.close()

# # 使用with 不用收到的关闭文件
# with open('test.text','r',encoding='utf-8') as file_r1:
#     lines = file_r.readlines()
#     for c in lines:
#         print(c.rstrip())


# # 异常处理
# try:
#     res =  print(5 / 0)
# except:
#     print('***********exc')
# else:
#     print(res)
# finally:
#     print('最后要走的代码')


# *******************************2018年12月06日20:09:52 *******************************

# # 表达式
# m = True
# print('hello') if m else print('world')
#
# # 列表推导式.
# '''
# 效率高于for循环 variable = [out_exp_res   for   out_exp   in   input_list   if   condition]
# out_exp_res: 列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
# condition：　　根据条件过滤哪些值可以。
# '''
# str1 =  '112323qweaweq'
# res = [letter for letter in str1 if str1.count(letter) == 1]
# if len(res) > 0:
#     print(res[0])
# else:
#     print('未找到只出现一次的字符')
#
#
# str2 = 'adfasdfgDdwAdsWE'
# res2 = [letter.upper() for letter in str2]
# print(res2)
#
#
# # 元组表达式
# '''
# 其实没有的得到元组的原因就是元组推导不会立即计算出所有的表达式的值，它只是一个表达式，会在你调用的时候计算出表达式的值。
# '''
# tuple1 = (letter for letter in range(1,10))
# print(tuple1)
#
# tupl_res = [letter for letter in tuple1]
# print(tupl_res)
#
# # 字典推导式
# # 交互 key:value  -> valye:key
# dict = {"k1":'v1','k2':'v2','k3':'v3'}
# dict_res = {v:k for k,v in dict.items()}
# print(dict_res)


# *******************************2018年12月06日20:09:52 *******************************

# num1 = 2
# num3 = 2
# num4 = 25845
# num5 = 25845
# s1 = '323'
# s2 = '323'
# t1 = ['2','3']
# t2 = ['2','3']
#
# print(num1 is num3) # True
# print(num4 is num5) # True
# print(s1 is s2)     # True
# print(t1 is t2)     # False  元组
# print(id(t1),id(t2)) # id() 获取内存地址
#
#
# # 元组中存放了可变对象，可变对象是可变的，因为元组中存放的是对象的地址，即使可变对象变了，地址依然不变
#
# t3 = ('1','2',[4,5])
# print(id(t3))
# t3[2].append(6)
# print(t3,id(t3))


# **********************copy deepcopy*********2018年12月06日20:09:52 *******************************

# import copy
#
# def lwp(*s):
#     print(*s,sep='*****')
#
#
# a1 = [[1,3],[2,6],[4,5]]
# a2 = a1
# a2[0].append(2)
# a2.append(32)
# lwp(a1,a2)
# print(id(a1),id(a2))
# print(id(a1[0]),id(a2[0]))
#
# a3 = copy.copy(a1)
# a3[1].append(200)
# lwp('a3:', a1,a3)
# lwp(id(a1),id(a3))
# lwp(id(a1[1]),id(a3[1]))
#
#
# a4 = copy.deepcopy(a1)
# a4[2].append(20)
# lwp(a1,a4)
# lwp(id(a1),id(a4))
# lwp(id(a1[2]),id(a4[2]))


# **********************迭代器*********2018年12月06日20:09:52 *******************************

# shuzu1 = [1, 3, 4, 5, 7]
# ite = iter(shuzu1)  # 创建迭代器对象
# # for ele in ite:
# #     print(ele, sep='***')
#
# flag = True
# while flag:
#     try:
#         print(next(ite))
#     except:
#         flag = False


# lwvar = '323'
# def lwsum(self):
#     print('++++++++++++')
#
# class lwclass():
#     def __init__(self):
#         pass
#     def lwadd(self):
#         print('******add')
#
# if __name__ == '__main__':
#     print(lwvar+'**********')

c = {}
d = {'23':'323'}
c.pop(d)
