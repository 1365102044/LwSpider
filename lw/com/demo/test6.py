
import threading
import time

# a = [3,4,5,6]
# print(len(a))
# for i in range(0,len(a)):
#     print ( str(a[i]) +'********'+str(i))
#     if i == len(a):
#         print(a[i])


# lists = [a for a in range(0,10) if a%2 is 0 a**3, i for i in range(0,10) if i%2 !=0 is i**5]


# for i in range(0,3):
#     print(i)

# for index, var in enumerate(['2','4','6','7']):
#     print(index)
#     print(var+'******')

#coding=utf-8



import threading
from time import ctime,sleep
import asyncio

# ************* 多线程 ****************

# def music(func):
#     for i in range(500):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         # sleep(1)
#
# def move(func):
#     for i in range(500):
#         print ("I was at the %s! %s" %(func,ctime()))
#         # sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#
#     print ("all over %s" %ctime())




# ************* 多线程 ****************


async def func():
    await asyncio.sleep(1)
    # time.sleep(1)
    print('*******'+ctime())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    funclist = [func() for i in range(500)]
    loop.run_until_complete(asyncio.gather(*funclist))