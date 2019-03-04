
# selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lxml import etree
import time

def func1():
    # 声明 chrome
    browser = webdriver.Chrome ()
    # 声明 Firefox
    # browser = webdriver.Firefox()

    try:
        browser.get ( 'https://www.baidu.com' )
        input = browser.find_element_by_id ( 'kw' )
        input.send_keys ( 'Python爬虫' )
        input.send_keys ( Keys.ENTER )
        wait = WebDriverWait ( browser, 10 )
        wait.until ( EC.presence_of_all_elements_located ( (By.ID, 'content_left') ) )
        # print ( browser.current_url )
        # print ( browser.get_cookies () )
        print ( browser.page_source )
    finally:
        browser.close ()


def func2():
    # from selenium import webdriver

    browser = webdriver.Chrome ()  # 声明浏览器
    browser.get ( 'https://www.zhihu.com' )  # 访问网页
    search_input = browser.find_element_by_id ( 'Popover1-toggle' )  # 查找节点
    print ( search_input )
    search_input.send_keys('python爬虫')
    commitbnt = browser.find_element_by_class_name("Button SearchBar-askButton Button--primary Button--blue")
    commitbnt.click()
    browser.close ()  # 关闭浏览器

def func3():



    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    search_input = browser.find_element_by_id('kw')
    search_input.send_keys('三体')
    time.sleep(2)
    search_input.clear()
    search_input.send_keys('黑洞')
    submit = browser.find_element_by_id('su')
    submit.click()
    time.sleep(3)

    xpath_source = browser.page_source
    print(type(xpath_source))

    getdata(xpath_source)

    browser.close()

def getdata(datas):
    xpath_source = etree.HTML(datas)
    a_all = xpath_source.xpath('//a')
    for ele in a_all:
        print(ele.text,ele.attrib['href'])

if __name__ == '__main__':
    func3 ()

