
import requests
from bs4 import BeautifulSoup
from lw.com.tools import LWFuncTools
from lw.com.tools.LWFuncTools import lwprint
from lxml import etree
from lw.com.tools.LWCsvTool import LWCsvTools
from lw.com.tools.LWOcrTool import LWocrTool
import time

class zhiPinItem(object):
	job_Name = ''			# 职位名
	job_xinzi = ''			# 薪资
	job_skill = ''			# 技能要求
	job_address = ''		# 地址
	job_education = ''  	# 学历
	job_years = ''			# 工作年限
	com_Name = ''			# 公司名
	com_infor = ''			# 公司基本信息
	url = ''				# 地址
	publishTime = ''		# 发布时间
	cur_page = ''			# 当前页
	


class zhipinSpider(object):
	
	# startUrl = 'https://www.zhipin.com/c101010100-p100203/?ka=hot-position-5'
	baseurl = 'https://www.zhipin.com'
	# https://www.zhipin.com/job_detail/95c7b10ce17777b41XR-3Nq7ElM~
	
	sellpTime = 1
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
	}
	
	def __init__(self):
		self.lwcsv = LWCsvTools('zhipin.csv')
		self.lwcsv.lw_writeHeaders(['职位','薪资','技能要求','工作地址','公司名','公司信息','发布时间','url','当前页数'])
		
		
		# 列表地址
		for i in range (1, 20):
			url = 'https://www.zhipin.com/c101010100-p100203/?page=' + 'str(i)' + '&ka=page-' + str (i)
			self.startSpider (url,i)
			time.sleep(5)
			time.sleep(self.sellpTime)
	
	
	# 		开始抓取数据
	def startSpider(self,url,cur_page):
		
		res = requests.get(url,headers=self.headers)
		
		if res.status_code != 200:
			lwprint('+++++++++++++++列表++请求失败！url:'+url + '++++++++++cur_page:'+str(cur_page))
			return
		
		pageSource = etree.HTML(res.content)
		
		# 判读是否是验证码界面
		title = pageSource.xpath('//div[@id="wrap"]/div[@class="capcha-box"]/div[@class="tips"]/text()')
		if len(title) > 0 :
			lwprint('\n\n++++++++++++++++++被检测到了+++++++++++++cur_page:'+str(cur_page))
			checkcode_infor = pageSource.xpath('//div[@id="wrap"]/div[@class="capcha-box"]')[0]
			action_url = checkcode_infor.xpath('.//form')[0].attrib["action"]
			codeimage_url = checkcode_infor.xpath('.//form/p/img')[0].attrib["src"]
			lwprint(action_url,codeimage_url)
			self.handleYanZheng(action_url,codeimage_url,cur_page)
			return
		
		
		# 数据正常
		lists = pageSource.xpath('//div[@class="job-primary"]')
		for ele in lists:
			
			item =  zhiPinItem()
			item.job_Name = ele.xpath('.//div[@class="job-title"]/text()')[0]
			item.job_xinzi = ele.xpath('.//span[@class="red"]/text()')[0]
			job_infor_temp =  ele.xpath ('.//div[@class="info-primary"]/p/text()')
			
			try:
				item.job_address =  job_infor_temp[0]
				item.job_years = job_infor_temp[1]
				item.job_education =  job_infor_temp[2]
			except:
				item.job_address = job_infor_temp
			finally:
				pass
			
			item.com_Name = ele.xpath('.//div[@class="company-text"]//a/text()')[0]
			item.com_infor = ele.xpath ('.//div[@class="company-text"]/p/text()')[0]
			
			item.publishTime = ele.xpath('.//div[@class="info-publis"]/p/text()')[0]
			item.url = ele.xpath('.//div[@class="info-primary"]/h3/a')[0].attrib["href"]
			item.cur_page = str(cur_page)
			
		
			
			# 获取详情页数据
			self.getPageDeatilInfor(item)
		
		
			
	def getPageDeatilInfor(self,item):
		
		res = requests.get(self.baseurl+item.url,headers=self.headers)
		
		if res.status_code != 200:
			lwprint('+++++++++++++++详情++请求失败！url:'+item.url + '++++++++++cur_page:'+item.cur_page)
			return
		
		pageSource = etree.HTML (res.content)
		
		# 判读是否是验证码界面
		title = pageSource.xpath ('//div[@id="wrap"]/div[@class="capcha-box"]/div[@class="tips"]/text()')
		if len(title) > 0:
			lwprint ('\n\n++++++++++++++++++被检测到了+++++++++++++cur_page:' + item.cur_page)
			checkcode_infor = pageSource.xpath ('//div[@id="wrap"]/div[@class="capcha-box"]')[0]
			action_url = checkcode_infor.xpath ('.//form')[0].attrib["action"]
			codeimage_url = checkcode_infor.xpath ('.//form/p/img]')[0].attrib["src"]
			if 'str(i)' in action_url:
				action_url.replace('str(i)',item.cur_page)
			self.handleYanZheng (action_url, codeimage_url)
			
			return
		
		
		# 详情数据 正常
		job_infor_list = pageSource.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')
		job_infor = ''
		for ele in job_infor_list:
			job_infor = job_infor + ele.replace('\n','').replace(' ','')
		
		item.job_skill = job_infor
		
		lwprint(item.url,'curpage: '+item.cur_page)
		self.lwcsv.lw_writeListToCsv([item.job_Name,
									  item.job_xinzi,
									  item.job_skill,
									  item.job_address,
									  item.com_Name,
									  item.com_infor,
									  item.publishTime,
									  item.url,
									  item.cur_page])
	
	
	# 当被检测到时，处理验证码
	def handleYanZheng(self,action_url,codeimage_url,cur_page):
		
		# 识别验证码
		code =  LWocrTool().lw_ocr(self.baseurl + codeimage_url).replace(' ','')
		lwprint('+++++++++++++识别到验证码:'+ code)
		
		param = {'captcha':code}
		res =  requests.post(self.baseurl+action_url,data = param)
		if res.status_code == 200:
			
			self.sellpTime = 0
		else:
			lwprint('\n++++++++++++++++验证失败！！+++++++++++++++++++++\n')
			self.sellpTime += 6
		
		time.sleep (6)
		url = 'https://www.zhipin.com/c101010100-p100203/?page=' + 'str(cur_page)' + '&ka=page-' + str (cur_page)
		self.startSpider (url, cur_page)
		
# 		/captcha/verifyCaptcha?redirect=http://www.zhipin.com/job_detail/95c7b10ce17777b41XR-3Nq7ElM~


# 	href="/c101010100-p100203/?page=2"
# https://www.zhipin.com/c101010100-p100203/?page=2&ka=page-2
# https://www.zhipin.com/c101010100-p100203/?page=3&ka=page-3
# https://www.zhipin.com/c101010100-p100203/?page=4&ka=page-4

# 	 https://www.zhipin.com
# 	/captcha?randomKey=kqx1LpWaJWmumHZjQxa9et2dfWHOUAHU

if __name__ == '__main__':
	zhipinSpider()
