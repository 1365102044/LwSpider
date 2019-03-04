
from aip import AipOcr
from lw.com.demo2 import *
import urllib.request
import ssl
import os

class LWocrTool(object):

    def __init__(self,isDelete=False):

        # 该参数只有使用 图片地址为HTTPS地址使用，默认识别后，本地图片不删除
        self.isDelete = isDelete

        # 临时保存的路径
        self.tempPicPath = 'tempPic.jpg'

        """ 你的 APPID AK SK """
        APP_ID = '11439127'
        API_KEY = 'FVIEx6aEEbYFOOVrndgrB0S2'
        SECRET_KEY = 'uSAqQDITFzp2Z0YKBvHrxVkVsLSGP6fy'

        # 新建一个AipOcr
        self.client = AipOcr ( APP_ID, API_KEY, SECRET_KEY )

    # 获取本地图片的文字
    def ocr_localPic(self,picture):

        """ 如果有可选参数 """
        options = {}
        options["detect_direction"] = "true"
        options["probability"] = "true"
        pic_res = self.client.basicAccurate ( picture, options )
        if len ( pic_res['words_result'] ) > 0:
            res = pic_res['words_result'][0]['words']
            if os.path.exists ( self.tempPicPath ) and self.isDelete:
                os.remove ( self.tempPicPath )
            return res
        else:
            return '未识别'

    # 获取网络图片中的文字
    def orc_urlPic(self,picUrl):
        """ 如果有可选参数 """
        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（含位置信息版）, 图片参数为远程url图片 """
        pic_res = self.client.generalUrl ( picUrl, options )
        if len(pic_res['words_result']) > 0:
            res = pic_res['words_result'][0]['words']
            return res
        else:
            return '未识别'

    # 当图片地址是HTTPS时，先把图片临时保存在当前路径下，再识别
    def tempSaveImage(self, imgUrl):

        # urllib 当URL为HTTPS时 需要SSL
        ssl._create_default_https_context = ssl._create_unverified_context

        # 图片下载到本地
        urllib.request.urlretrieve ( imgUrl, self.tempPicPath )

    # 获取本地图片
    def readImage(self,picPath):
        with open ( picPath, 'rb' ) as fp:
            image = fp.read ()
            res = self.ocr_localPic ( image )
            return res

    # 判断是网络图片地址还是本地图片地址
    def lw_ocr(self,picPath):

        if 'https' in picPath:
            # raise RuntimeError('暂时不支持https')

            # 把图片下载到本地
            self.tempSaveImage(picPath)

            # 本地读取图片
            return self.readImage(self.tempPicPath)

        elif 'http' in picPath:
            # 网络图片
            return self.orc_urlPic(picPath)

        else:
            # 本地读取图片
            return self.readImage ( picPath )


if __name__ == '__main__':

    # res = LWocrTool ().lw_ocr ( '../demo2/验证码.jpg' )
    # print(res)

    # res = LWocrTool().lw_ocr('https://www.douban.com/misc/captcha?id=vBWSq88fSYwDBYkJJWVqj2yu:en&size=s')
    # print ( res )
    pass