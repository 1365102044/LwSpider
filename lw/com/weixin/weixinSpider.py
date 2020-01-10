
import itchat

class lwweixin:

    def __init__(self):
        # 自动登录方法，hotReload=True可以缓存，不用每次都登录,但是第一次执行时会出现一个二维码，需要手机微信扫码登录
        # itchat.auto_login(hotReload=True)
        pass
    # 搜索好友，search_friends("xxx"),其中"xxx"为好友昵称，备注或微信号不行
    def searchFriends(self):
        # "智能群管家014"为好友昵称
        userinfo = itchat.search_friends(name='对方正在输入...')
        # print('userinfo:'+userinfo)
        # print(userfinfo)，获取userinfo中的UserName参数
        userid = userinfo[0]['UserName']
        print('userid:'+userid)
        # 调用微信接口发送消息
        itchat.send("hello world!!!", userid)  # 通过用户id发送信息


if __name__ == '__main__':
    # lwweixin().searchFriends()

    itchat.auto_login(hotReload=True)
    itchat.send_msg('hello world',toUserName=None)