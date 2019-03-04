

import requests
from lxml import etree

class testFunct1(object):
    html = """
            <html>
                <head>
                    <base href='http://example.com/' />
                    <title>Example website</title>
                </head>
                <body>
                    <div id='images'>
                        <a href='image1.html'>Name: My image 1 <br/><img src='image1_thumb.jpg'/></a>
                        <a href='image2.html'>Name: My image 2 <br/><img src='image2_thumb.jpg'/></a>
                        <a href='image3.html'>Name: My image 3 <br/><img src='image3_thumb.jpg'/></a>
                        <a href='image4.html'>Name: My image 4 <br/><img src='image4_thumb.jpg'/></a>
                        <a>Name: My image 5 <br/><img src='image5_thumb.jpg'/></a>
                    </div>
                </body>
            </html>
            """

    def htmlFunct():
        page_source = etree.HTML (self.html )
        all_title = page_source.xpath ( '//title/text()' )
        print ( all_title )

        all_a_href = page_source.xpath ( '//a/@href' )
        print ( all_a_href )

        # all_a_href1 = page_source.xpath('//a[@href=="image1.html"]')
        # print(all_a_href1)

        a_image1_text = page_source.xpath ( "//body//a[1]/text()" )
        print ( a_image1_text )

        a_image1_src = page_source.xpath ( "//a[@href='image1.html']/img/@src" )
        print ( a_image1_src )

        a_image3_href = page_source.xpath ( "//a[contains(@href, '3')]/@href" )
        print ( a_image3_href )

        a_last = page_source.xpath ( "//body//a[last()]/img/@src" )
        print ( a_last )

        all_img_src = page_source.xpath ( "//img/@src" )
        print ( all_img_src )


class testFunct(object):

    def testfunc(self):

        heads={'Connection':'Keep-Alive', 'Accept':'text/html, application/xhtml+xml, */*', 'Accept-Language':'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3', 'Accept-Encoding':'gzip, deflate','User-Agent':'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}

        url='https://egame.qq.com/gamelist'

        res = requests.get (url,heads,timeout=10)
        root = etree.HTML (res.content)
        gameList = root.xpath ( "//ul[@class='livelist-mod']//li//a//p//text()")
        print(gameList)



class testClass1(object):
    html = '''

    <html>
    　　<head>
    　　　　<meta name="content-type" content="text/html; charset=utf-8" />
    　　　　<title>友情链接查询 - 站长工具</title>
    　　　　<!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
    　　　　<meta name="Keywords" content="友情链接查询" />
    　　　　<meta name="Description" content="友情链接查询" />

    　　</head>
    　　<body>
    　　　　<h1 class="heading">Top News</h1>
    　　　　<h1 class="heading111">Top News111</h1>
    　　　　<h1 class="heading222">Top News2222</h1>
    　　　　<p style="font-size: 200%">World News only on this page</p>
    　　　　Ah, and here's some more text, by the way.
    　　　　<p>... and this is a parsed fragment ...</p>
            <div> 
            <p> lwq </p>
                <div> 
                    <p> lwq33 </p>
                </div>
            </div>
    　　　　<a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a> 
    　　　　<a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a> 
    　　　　<a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a> 
    　　　　<a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
    　　　　<a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
    　　　　<a href="http://www.4399.com/" target="_blank">4399小游戏</a> 
    　　　　<a href="http://www.91wan.com/" target="_blank">91wan游戏</a>

    　　</body>
    </html>

    '''



    def testFunc(self):
        xpath_source = etree.HTML(self.html)

        # a_lists = xpath_source.xpath('//a')
        # for ele in a_lists:
        #     print(ele.text)
        #     print ( ele.attrib['href'])

        # 过滤条件  [@style,@name, @id, @value, @href, @src, @class....]
        a1 = xpath_source.xpath('//a[@href="http://www.91wan.com/"]')
        print(a1[0].text)
        print ( a1[0].attrib)

        a1 = xpath_source.xpath ( '//a[contains(@href,"www.91wan")]' )
        print ( a1[0].text )
        print ( a1[0].attrib )

        # 直接获取所有a标签下的href属性value
        a1 = xpath_source.xpath ( '//a/@href' )
        print ( a1 )


        title = xpath_source.xpath('//title')
        print(title[0].text)

        h1 = xpath_source.xpath('//h1[text()="Top News111"]')
        print(h1[0].attrib['class'])

        h11 = xpath_source.xpath('//h1[position()=1]')
        print(h11[0].attrib['class'])

        p1 = xpath_source.xpath('//body//*//p')
        for ele in p1:
            print(ele.text)

'''
    总结：
        1.from lxml import etree
        2.xpath_source = etree.HTML(html)
    *   3.使用相对路径 '//a' 获取所有的标签集合，
        4.print(ele.text)  是获取该标签下的内容
    *   5.print（ele.attrib）获取该标签下的属性字典
        6.函数text()的意思则是取得节点包含的文本。 h1 = xpath_source.xpath('//h1[text()="Top News111"]')
        7.函数position()的意思是取得节点的位置  h11 = xpath_source.xpath('//h1[position()=1]')
        8.“*”可以代替所有的节点名      p1 = xpath_source.xpath('//body//*//p') 获取body下第二级下所有p标签
    *   9.a[contains(属性key，包含的values)]          a1 = xpath_source.xpath ( '//a[contains(@href,"www.91wan")]' )  
        a标签中属性包含values的匹配
    *   10 a1 = xpath_source.xpath ( '//a/@href' )  直接获取所有a标签下的href属性value
        
        
'''

if __name__ == '__main__':
    testClass1().testFunc()
