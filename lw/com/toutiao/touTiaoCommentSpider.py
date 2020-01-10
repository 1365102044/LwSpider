import pymysql
from bs4 import BeautifulSoup
import requests
import time


class CommentSpider():
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        # ':authority': 'www.toutiao.com',
        # ':method': 'GET',
        # ':path': '/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E6%9C%BA%E5%88%B6%E7%A0%82&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1574839785600',
        # ':scheme': 'https',
        'accept': 'application/json, text/javascript',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=51f447455d62fff3440874e8c164aa35; tt_webid=6763493864759281166; __tasessionId=spntjkw651574838504576;s_v_web_id=91427c14e9fc9c4d801a3c76cf7ce20b',
        'referer': 'https://www.toutiao.com/search/?keyword=%E6%9C%BA%E5%88%B6%E7%A0%82',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    def __init__(self):
        # self.db = pymysql.connect(host='127.0.0.1', user='root', password='1113', database='compostion',
        #                           cursorclass=pymysql.cursors.DictCursor)
        pass

    def get_article(self, kw):
        # url = 'https://www.toutiao.com/search/?keyword=机制砂'
        time_cur = int(round(time.time() * 1000))
        para = {
            'aid': '24',
            'app_name': 'web_search',
            'offset': '0',
            'format': 'json',
            'keyword': '机制砂',
            'autoload': 'true',
            'count': '20',
            'en_qc': '1',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis',
            'timestamp': str(time_cur)
        }
        # 1574839244483
        # 1574839771272
        # url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E6%9C%BA%E5%88%B6%E7%A0%82&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp='+str(time_cur)
        url = 'https://www.toutiao.com/api/search/content'
        print(url)
        print(para)
        res = requests.get(url, headers=self.headers, params=para)
        print(res.content)
        soup = BeautifulSoup(res.content, 'xml')
        article_list = soup.find_all('div', class_='articleCard')
        for article in article_list:
            comment_num = article.find_all('a', class_='lbtn comment')
            print(comment_num.text)


if __name__ == '__main__':
    CommentSpider().get_article('机制砂')
