
"""定义Frame窗口基类"""

import sys
import wx


class MyFrame(wx.Frame):
    session = {}

    def __init__(self,title,size):
        super().__init__(parent=None, id=None, title=title, pos=None, size=size,
                        style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX,
                       name=None)
        # style是定义窗口风格，具体看官网。https://docs.wxpython.org/wx.Frame.html#wx-frame
        # 上面的DEFAULT就是包含了下面所有的风格的：
        # wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER |
        # wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        # 上面的例子是去掉了其中的一个。官网的例子是这样的：
        # style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)  去掉了2个来固定窗口大小
        # 设置窗口居中
        self.Center()
        # 设置Frame窗口内容面板
        self.contentpanel = wx.Panel(parent=self)
        # 图标文件
        ico = wx.Icon ( "resources/bats.ico", wx.BITMAP_TYPE_ICO )
        # 设置图标
        self.SetIcon ( ico )
        # 设定窗口大小，这里设置了相同的最大和最小值，也就是固定了窗口大小。
        # 因为上面的窗口风格了保留了wx.RESIZE_BORDER，所以这里用另外一个放来来保证大小不可调整
        # 这样做有一点不好，就是鼠标放在窗口边缘，会变成调整窗口大小的样子，但是拉不动窗口
        self.SetSizeHints ( size, size )
        # 绑定关闭按钮的点击事件
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        # 退出系统
        self.Destroy ()
        sys.exit ()

