import pymysql
import jieba
from os import path
import matplotlib.pyplot as plt
from PIL import Image
import numpy as  np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class wordcloudDemo():
    # 源码所在目录
    d = path.dirname(__file__)

    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',user='root',password='1234567890',database='lwqdata',cursorclass=pymysql.cursors.DictCursor)

    # 把数据 拼接成 字符串
    def get_datas(self):
        cursor = self.db.cursor()
        cursor.execute('select productSize from jd_comment_t limit 0,1500;')
        datas = cursor.fetchall()
        str_datas = ''
        # for dic in datas:
        #     str_datas = str_datas + dic['title'] + ' '
        # self.jieba_datas(str_datas)

        for dic in datas:
            str_datas = str_datas + dic['productSize'] + ' '
        self.show_wordcloud(str_datas)

    # 把字符串 分解成 词汇字符串
    def jieba_datas(self, str):
        res = ' '.join(jieba.lcut(str))
        self.show_wordcloud(res)

    # 配置wordcloud
    def show_wordcloud(self,str_datas):
        # print('str_datas: '+str_datas)

        wordcloud = WordCloud(font_path='SimHei.ttf',   #如果是中文必须要添加这个，否则会显示成框框
                              background_color='white',
                              width=1000,
                              height=1000,
                              margin=2,
                              mask=self.get_back_img()).generate(str_datas)
        wordcloud.to_file('res_size.jpg')  # 保存图片
        plt.imshow(wordcloud.recolor(color_func=self.get_back_color()),interpolation='bilinear',)   #用plt显示图片
        plt.axis('off') #不显示坐标轴
        plt.show()      #显示图片

    # 配置词云 字体颜色
    def get_back_color(self):
        alice_coloring = np.array(Image.open(path.join(self.d, "back_img.jpg")))
        # create coloring from image
        image_colors = ImageColorGenerator(alice_coloring)
        return image_colors

    # 配置词云的 形状图片
    def get_back_img(self):
        return np.array(Image.open(path.join(self.d, "back_img.jpg")))


if __name__ == '__main__':
    wordcloudDemo().get_datas()