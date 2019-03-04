import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle


window =  tk.Tk()
window.geometry('450x300')
window.title('Welcome to lw Python')

# welcome image
image_file = tk.PhotoImage(file='welcome.gif')
canvas = tk.Canvas(window,height=200,width=500)
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')


# user information
tk.Label(window,text='User Name:').place(x=50,y=150)
tk.Label(window,text='PassWord:').place(x=50,y=190)

user_name_var = tk.StringVar()
user_name_var.set('exmaple@python.com')
entry_user_name = tk.Entry(window,textvariable=user_name_var)
entry_user_name.place(x=160,y=150)

user_pw_var = tk.StringVar()
entry_password = tk.Entry(window,textvariable=user_pw_var,show='*')
entry_password.place(x=160,y=190)


# 登录
def login():

    user_name = user_name_var.get ()
    user_pw = user_pw_var.get ()

    infor_list = []
    with open('account_infor.text','r') as file:
        infor = file.readlines()
        for ele in infor:
            infor_list.append(eval(ele))
    print('所有账号信息：'+infor_list)

    for ele in infor_list:
        if user_name in ele.keys():
            if ele[user_name] == user_pw:
                tk.messagebox.showinfo(title='恭喜！',message='登录成功')
                return True
            else:
                tk.messagebox.showerror ( title='登录失败', message='输入的密码错误' )
                return False
    tk.messagebox.showerror ( title='登录失败', message='该账号未注册' )
    return False

# 注册时检查输入的账号是否存在
def checkAccountExist(us,pw):
    infor_list = []
    with open ( 'account_infor.text', 'r' ) as file:
        infor = file.readlines ()
        for ele in infor:
            infor_list.append ( eval ( ele ) )
    for ele in infor_list:
        if us in ele.keys():
            tk.messagebox.showerror(title='注册',message='该账号已注册')
            return True
        else:
            return False


# 注册流程
def sign_up():

    # 提交注册信息
    def sign_up_commit():

        user_name = sign_up_username_var.get ()
        user_pw1 = sign_up_pw_var.get ()
        user_pw2 = sign_up_pw_var2.get ()

        if not user_name:
            tk.messagebox.showerror(title='注册',message='User Name不能为空')
            return
        elif not user_pw1:
            tk.messagebox.showerror (title='注册', message='PassWord不能为空')
            return
        elif not user_pw2 or user_pw2 != user_pw1:
            tk.messagebox.showerror (title='注册', message='两次输入的密码不一致')
            return

        # 检查账号是否已经注册
        if checkAccountExist(user_name,user_pw1):
            return

        # 把账号和密码写入文件
        infor = '{"%s":"%s"}\n' % (user_name,user_pw1)
        with open('account_infor.text','a+') as file:
            file.write(infor)

        # 销毁窗体
        window_sign_up.destroy()

    # 注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x250')
    window_sign_up.title('sign up window')

    # 注册lable
    sign_up_userName = tk.Label(window_sign_up,text='User Name:').place(x=20,y=30)
    sign_up_pw = tk.Label (window_sign_up, text='PassWord:' ).place ( x=20, y=70 )
    sign_up_pw2 = tk.Label (window_sign_up, text='confirm PW:' ).place ( x=20, y=110 )

    # 注册提交按钮
    sign_up_commit = tk.Button(window_sign_up,text='commit',command=sign_up_commit).place(x=130,y=160)

    # 注册输入框
    sign_up_username_var = tk.StringVar()
    sign_up_username_var.set('exmaple@python.com')
    tk.Entry(window_sign_up,textvariable=sign_up_username_var).place(x=150,y=30)
    sign_up_pw_var = tk.StringVar()
    tk.Entry ( window_sign_up, textvariable=sign_up_pw_var ).place ( x=150, y=70 )
    sign_up_pw_var2 = tk.StringVar ()
    tk.Entry ( window_sign_up, textvariable=sign_up_pw_var2 ).place ( x=150, y=110 )

# 登录界面按钮
tk.Button(window,text='login',command=login).place(x=170,y=230)
tk.Button(window,text='sign up',command=sign_up).place(x=270,y=230)

window.mainloop()