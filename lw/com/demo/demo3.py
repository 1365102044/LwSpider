
from bs4 import BeautifulSoup

file = open('demo3_test.html','r',encoding='UTF-8')
file_r = file.read()
soup = BeautifulSoup(file_r,'html.parser')
# print(soup)

# 第一个元素是a
# print(soup.find('a'))
# 所有的元素a
# print(soup.find_all("a"))

# p元素中的属性
# print(soup.p.attrs)

# id ='auto-test-1'
print(soup.find_all(id='auto-test-1'))

# 查找a标签 class=baidu的
print(soup.find_all('a',class_='sort-menu'))