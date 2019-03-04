
import wx


class Exmple1(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,parent=None,id=-1,title='初识 wxPython',size=(600,600))
        parnel = wx.Panel(self,-1)
        self.Center()

        button = wx.Button(parnel,label='button',pos=(50,50))
        satictText = wx.StaticText(parnel,-1,'this is staticText',pos=(50,80))
        textCtrl = wx.TextCtrl(parnel,-1,'this textCtrl',pos=(50,100))
        password = wx.TextCtrl(parnel,-1,'this is password',style=wx.TE_PASSWORD,pos=(50,130))
        mutilTextCtrl = wx.TextCtrl(parnel,-1,'this is mutiSlTextCtrl',style=wx.TE_MULTILINE,pos=(50,170))

        checkBox1 = wx.CheckBox(parnel,-1,'我是复选框1',pos=(200,50))
        checkBox2 = wx.CheckBox (parnel, -1, '我是复选框2', pos=(200, 70))

        radio1 = wx.RadioButton(parnel,-1,'我是单选框1',pos=(200,100),style=wx.RB_GROUP)
        radio2 = wx.RadioButton(parnel,-1,'我是单选框2',pos=(200, 120) )
        radio3 = wx.RadioButton(parnel,-1,'我是单选框3',pos=(200, 140) )

        radlist = ['python','rn','oc','swift','html']
        wx.RadioBox(parnel,-1,'一组单选按钮',pos=(300,50),size=wx.DefaultSize,choices=radlist,
                    style=wx.RA_SPECIFY_ROWS)

        boxlist = ['python','rn','oc','swift','html']
        listbox = wx.ListBox(parnel,-1,pos=(450,50),size=(100,100),choices=boxlist,
                             style=wx.RA_SPECIFY_ROWS)

        imag = wx.Image('welcome.gif',wx.BITMAP_TYPE_ANY).Scale(400,200)
        sb = wx.StaticBitmap(parnel,-1,wx.BitmapFromImage(imag),pos=(50,300))


class Exmple2(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,parent=None,id=-1,title='测试2',size=(600,600))
        panel = wx.Panel(self,-1)
        # panel.SetBackgroundColour('Blue')
        self.Center()

        sizer = wx.GridBagSizer ( 4, 4 )

        s_text = wx.StaticText(panel,label='Rename to')
        sizer.Add(s_text,pos=(0,0),flag=wx.LEFT|wx.BOTTOM|wx.TOP,border=10)

        tc = wx.TextCtrl(panel)
        sizer.Add(tc,pos=(1,0),span=(1,5),flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=5)


class Exmple3(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,id=-1,size=(500,500))

        panel = wx.Panel(self,-1)
        self.Center()

        panel.Bind(wx.EVT_MOTION,self.OnMove)
        wx.StaticText ( panel, -1, "Pos:", pos=(10, 12) )
        self.tx = wx.TextCtrl(panel,pos=(60,12),size=(100,20))

    def OnMove(self,event):
        pos = event.GetPosition()
        self.tx.SetValue('%s,%s'%(pos.x,pos.y))


if __name__ == '__main__':
    app = wx.App()
    F = Exmple3()
    F.Show()
    app.MainLoop()
