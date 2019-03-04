
import requests
import urllib.request
from lxml import etree
import ssl
import sys
from aip import AipOcr

from lw.com.tools.LWOcrTool import *

# 模拟登陆
class autoLogin(object):

    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                          'Version/12.0 Safari/605.1.15'}

    # 验证码
    captcha_id = ''

    # 验证码标识
    captcha_solution = ''

    # 模拟登陆一：（使用账号、密码，验证码方式）

    login_cookie = {'Cookies': 'as="https://www.douban.com/note/701372777/"; '
                               '__utma=30149280.610191550.1541328297.1544584394.1545786747.8; __utmb=30149280.23.10.1545786747; '
                               '__utmc=30149280; __utmv=30149280.18918; __utmz=30149280.1545786747.8.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); regpop=1; __utmt=1; push_doumail_num=0; push_noty_num=0; douban-fav-remind=1; douban-profile-remind=1; ap_v=0,6.0; ue="1365102044@qq.com"; ps=y; _vwo_uuid_v2=DB436AE86A9503AD9443F043F0D7AA9B1|cbaa53721cc437661a0acc8f246cecc6; gr_user_id=29755e01-58c7-4af0-bd7b-2259069a3c3c; viewed="27061630_6920082_25870206_25829244"; ll="108288"; bid=uGBYkiH4zSc'}
    login_url_new = 'https://accounts.douban.com/login'

    def getLoginParam(self):
        login_param = {'form_email': 'liu1365102044@163.com',
                       'form_password': '1111aaaa',
                       'redir': 'https://www.douban.com/',
                       'source': 'main',
                       'captcha-solution': self.captcha_solution,
                       'captcha-id': self.captcha_id,
                       'login': '登录'}
        return login_param

    # 开始登陆
    def loginDouBan(self):
        print(self.getLoginParam())
        res = requests.post ( self.login_url_new, data=self.getLoginParam(), headers=self.header,
                              cookies=self.login_cookie ).text
        # print ( res )
        xpath_source = etree.HTML(res)
        error =  xpath_source.xpath('//p[@class="error"]')
        if len(error) > 0:
            print ( '*' * 20 + 'error:' + error[0].text + '*' * 20 )

        respose = res.respose()
        print(respose)

    # 把验证码图片保存本地
    def saveImage(self,imgUrl):
        # urllib 当URL为HTTPS时 需要SSL
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(imgUrl,'验证码.jpg')

    # 获取登录页的验证码信息
    def getLoginPageInfor(self):
        res = requests.post ( self.login_url_new, data=self.getLoginParam(), headers=self.header,
                              cookies=self.login_cookie ).text
        print ( res )
        xpath_source = etree.HTML ( res )
        # code_image_url_list = xpath_source.xpath ( '//img[@id="captcha_image"]' )
        # if len ( code_image_url_list ) > 0:
        #     code_image_url = code_image_url_list[0].attrib['src']
        #     self.saveImage ( code_image_url )

        code_eque_list = xpath_source.xpath ( '//input[@name="captcha-id"]' )
        if len ( code_eque_list ) > 0:
            self.captcha_id = code_eque_list[0].attrib['value']
            print ('captcha_id:' + self.captcha_id )

            # 根据验证码ID 拼接验证码图片地址
            code_image_url = 'https://www.douban.com/misc/captcha?id={}&amp;size=s'.format (self.captcha_id)
            self.saveImage ( code_image_url )
            print ( '验证码图片地址:' + code_image_url )

            # 识别到的验证码
            self.captcha_solution =  LWocrTool(isDelete=True).lw_ocr(code_image_url)
            print('识别到的验证码:'+self.captcha_solution)


            # 输入 从获取验证码图片上得到的 验证码
            # self.captcha_solution = input('请输入验证码：')

            # 获取到验证码信息 去登录
            self.loginDouBan()


    # 模拟登陆二：（使用登陆后的cookie方式）
    startUrl = 'https://www.douban.com/'

    al_login_cookies = {'Cookie':'bid=N-yVa1R-0ts; douban-fav-remind=1; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.746689456.1545794341.1545794341.1545794341.1; __utmc=30149280; __utmz=30149280.1545794341.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); regpop=1; ps=y; ue="liu1365102044@163.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18918; dbcl2="189182841:J50NphAHjXY"; ck=HMpI; __utmt=1; _pk_id.100001.8cb4=7c43e80eaa53e79e.1545794340.1.1545795691.1545794340.; __utmb=30149280.8.10.1545794341'}
    def postrquest(self):
        res = requests.get (self.startUrl, cookies = self.al_login_cookies)
        if res.status_code == 200:
            print ( res.text )
            # pass
        else:
            print(res.status_code)


if __name__ == '__main__':

    # autoLogin().postrquest()

    autoLogin ().getLoginPageInfor()