from bs4 import BeautifulSoup
import requests
import random
import urllib

class Ipspider():

    url_ips = 'https://www.xicidaili.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def get_ips_list(self):
        web_res = requests.get(self.url_ips,headers=self.headers,)
        soup = BeautifulSoup(web_res.text,'html')
        ips = soup.find_all('tr')
        ips_list = []
        for i in range(1,len(ips)):
            ips_info = ips[i]
            tds = ips_info.find_all('td')
            if len(tds) > 2:
                ips_list.append(tds[1].text + ':'+ tds[2].text)

            # print('*'*30)
        for ip in ips_list:
            try:
                proxy_host = 'https://' + ip
                proxy_temp = {'https:':proxy_host}
                res = urllib.urlopen(self.url,proxies=proxy_temp).read()
            except Exception  as e:
                ips_list.remove(ip)
                continue
        return ips_list

    def get_random_ip(self,ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://'+ip)
        proxy_ip = random.choice(proxy_list)
        proxys = {'http:':proxy_ip}
        return proxys


    def test_ip(self,proxies):
        para = {'catename': '一年级作文', 'p': 1, 'pagesize': '20', 'order': 'views', }
        url = 'http://ibaby.ipadown.com/api/zuowen/zw.list.php'
        res = requests.get(url,params=para,proxies=proxies,)
        resstr = str(res.content, encoding='utf-8')
        # soup = BeautifulSoup(resstr.text,'html')
        # content = soup.text
        print(resstr)


if __name__ == '__main__':
    ipspder = Ipspider()
    ips_list = ipspder.get_ips_list()
    for ip_tem in ips_list:
        print(ip_tem)
    ip = ipspder.get_random_ip(ips_list)
    print(ip)
    ipspder.test_ip(ip)
