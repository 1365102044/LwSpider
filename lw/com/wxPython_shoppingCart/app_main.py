
import wx

from .ui.login_frame import LoginFrame


class APP(wx.Frame):

    def OnInit(self):
        """创建窗口对象"""
        frame = LoginFrame ()
        # frame = ListFrame()  # 单独调试商品界面的时候，省的每次都要登录一下
        frame.Show ()
        return True


if __name__ == '__main__':
    app = APP () # 实例化
    app.MainLoop ()  # 进入主事件循环

