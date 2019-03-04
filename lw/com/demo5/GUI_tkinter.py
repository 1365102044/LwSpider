
import tkinter
import tkinter as mytk

import tkinter.messagebox


window = mytk.Tk()
window.title('my tk!')
window.geometry('300x500')



# **************************** 1.输入框 和text输入框 ***********************************
#
# e = tkinter.Entry ( window, show=None )
# e.pack ()
#
# def insert_point1():
#     va = e.get ()
#     t.insert('insert',va)
# def insert_end1():
#     va = e.get ()
#     t.insert ( 'end', va )
#     # t.insert('1.2',va) # 插入到第一行第二列
#
# b1 = tkinter.Button ( window, text='insert point', command=insert_point1)
# b1.pack ()
#
# b2 = tkinter.Button ( window, text='insert end', command=insert_end1 )
# b2.pack ()
#
# t = tkinter.Text(window,height=2)
# t.pack()



# **************************** 2.菜单/列表选择 ***********************************
# var2 = mytk.StringVar()
# la2 = mytk.Label(window,bg='Yellow',textvariable=var2,width=20,height=2)
# la2.pack()
#
# def print_select2():
#     value = lb2.get(lb2.curselection())
#     var2.set(value)
#
# b2 = mytk.Button(window,text='select item',command=print_select2,height=2)
# b2.pack()
#
# var22 = mytk.StringVar()
# var22.set((23,43,55,65,67,87))
# lb2 = mytk.Listbox(window,listvariable=var22)
# lb2.pack()
#
# tem_items = [22,44,55,66,77]
# for ele in tem_items:
#     lb2.insert('end',ele)


# **************************** 3.单选框 ***********************************
# var3 = mytk.StringVar()
# la3 = mytk.Label(window,text='empty',height=2,width=10,bg='Yellow')
# la3.pack()
#
# def select3():
#     la3.config(text='you select '+var3.get())
#
# rb31 = mytk.Radiobutton(window,text='Option A',variable=var3,value='A',command=select3)
# rb32 = mytk.Radiobutton(window,text='Option B',variable=var3,value='B',command=select3)
# rb33 = mytk.Radiobutton(window,text='Option C',variable=var3,value='C',command=select3)
# rb31.pack()
# rb32.pack()
# rb33.pack()


# **************************** 4.scale尺度 ***********************************

# la4 = mytk.Label(window,text='empty',bg='yellow',height=2)
# la4.pack()
#
# def selet_scale4(v):
#     la4.config(text='you select '+v)
# sc4 = mytk.Scale(window,label='title',from_=2,to=10,orient=mytk.HORIZONTAL,
#                 length=170,showvalue=1,tickinterval=2,resolution=0.01,command=selet_scale4)
# sc4.pack()
#
#
#
# # **************************** 5.多选框 ***********************************
#
#
# la5 = mytk.Label(window,text='empty',bg='yellow',height=2)
# la5.pack()
#
# def select5():
#     if var51.get() == 1 and var52.get() == 1:
#         la5.config(text='I love both')
#     elif (var51.get() == 0) and (var52.get() == 0):
#         la5.config ( text='I do not love either' )
#     elif (var51.get() == 1) and (var52.get() == 0):
#         la5.config ( text='I love only Python' )
#     else:
#         la5.config ( text='I love only OC' )
#
# var51 = mytk.IntVar()
# var52 = mytk.IntVar()
# ck51 = mytk.Checkbutton(window,text='Python',variable=var51,onvalue=1,offvalue=0,command=select5)
# ck52 = mytk.Checkbutton(window,text='OC',variable=var52,onvalue=1,offvalue=0,command=select5)
# ck51.pack()
# ck52.pack()



# **************************** 6.画布canvas ***********************************

# def move():
#     canvas.move ( rect, 0, 2 )
#
# canvas = mytk.Canvas(window,width=300,height=100,bg='blue')
# canvas.pack()
#
# image_file = mytk.PhotoImage(file='ins.gif')
# image = canvas.create_image(10,10,anchor='nw',image=image_file)  #anchor 图片的锚定点,以这个点对应坐标系中的00点
#
# x0, y0, x1, y1= 50, 50, 80, 80
# line = canvas.create_line(x0, y0, x1, y1)
#
# oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形
#
# btn6 = mytk.Button(window,text='move',command=move,height=2).pack()





# **************************** 7.Menubar菜单 ***********************************

# l7 = mytk.Label(window, text='', bg='yellow')
# l7.pack()
# counter = 0
# def do_job():
#     global counter
#     l7.config(text='do '+ str(counter))
#     counter+=1
#
#
# ##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
# menubar = mytk.Menu(window)
#
# ##定义一个空菜单单元
# filemenu = mytk.Menu(menubar, tearoff=0)
#
# ##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
# menubar.add_cascade(label='File', menu=filemenu)
#
# ##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
# ##如果点击这些单元, 就会触发`do_job`的功能
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
# filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单
#
# filemenu.add_separator()##这里就是一条分割线
#
# ##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
# filemenu.add_command(label='Exit', command=window.quit)
#
#
# editmenu = mytk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Cut', command=do_job)
# editmenu.add_command(label='Copy', command=do_job)
# editmenu.add_command(label='Paste', command=do_job)
#
# submenu = mytk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
# filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
# submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`
#
# window.config(menu=menubar)




# **************************** 8.Frame***********************************


# ###定义一个`label`显示`on the window`
# mytk.Label(window, text='on the window').pack()
#
# ###在`window`上创建一个`frame`
# frm = mytk.Frame(window)
# frm.pack()
#
# ###在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
#
# frm_l = mytk.Frame(frm)
# frm_r = mytk.Frame(frm)
#
# ###这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
# frm_l.pack(side='left')
# frm_r.pack(side='right')
#
# ###这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
# mytk.Label(frm_l, text='on the frm_l1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
# mytk.Label(frm_l, text='on the frm_l2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
# mytk.Label(frm_r, text='on the frm_r1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`


# **************************** 9.messagebox***********************************

# def hit_me():
#     #mytk.messagebox.showinfo(title='Hi', message='hahahaha')   # return 'ok'
#     #mytk.messagebox.showwarning(title='Hi', message='nononono')   # return 'ok'
#     # mytk.messagebox.showerror(title='Hi', message='No!! never')   # return 'ok'
#     # print(mytk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'
#     #print(mytk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
#     # print(mytk.messagebox.asktrycancel(title='Hi', message='hahahaha'))   # return True, False
#     # print(mytk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
#     print(mytk.messagebox.askyesnocancel(title="Hi", message="haha"))     # return, True, False, None
#
# mytk.Button(window, text='hit me', command=hit_me).pack()



# **************************** 10.pack grid place 放置位置***********************************

'''pack(), 他会按照上下左右的方式排列.'''
#canvas = mytk.Canvas(window, height=150, width=500)
#canvas.grid(row=1, column=1)
#image_file = mytk.PhotoImage(file='welcome.gif')
#image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#mytk.Label(window, text='1').pack(side='top')
#mytk.Label(window, text='1').pack(side='bottom')
#mytk.Label(window, text='1').pack(side='left')
#mytk.Label(window, text='1').pack(side='right')


'''
    grid 是方格, 所以所有的内容会被放在这些规律的方格中
    代码就是创建一个四行三列的表格，其实grid就是用表格的形式定位的。
    这里的参数 row为行，colum为列，padx就是单元格左右间距，pady就是单元格上下间距
'''
for i in range(4):
    for j in range(3):
        mytk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)


'''
    再接下来就是place(), 这个比较容易理解，就是给精确的坐标来定位，
    如此处给的（20,10），就是将这个部件放在坐标为（x，y）的这个位置 
    后面的参数anchor=nw就是前面所讲的锚定点是西北角。
'''
mytk.Label(window, text=1).place(x=20, y=10, anchor='nw')



window.mainloop()


