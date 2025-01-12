def get_page(ult):
	brow = webdriver.Chrome()
	name = re.compile('<h1 >(.*?)<\/h1>')
	ID = re.compile('CNVD-ID</td>.*?(CNVD-\d+-\d+).*?</td>', re.S)
	date = re.compile('公开日期<\/td>.*?(\d+-\d+-\d+).*?<\/td>', re.S)
	level = re.compile('</span>.*?([高中低])', re.S) 
	goods = re.compile('影响产品<\/td>.*?<td>(.*?)<\/td>', re.S) #
	CVE = re.compile('CVE ID<\/td>.*?(CVE-\d+-\d+)', re.S)
	discr = re.compile('描述.*?<td>(.*?)<\/td>', re.S) #
	typ = re.compile('类型.*?<td>(.*?)<\/td>', re.S)
	href = re.compile('链接<\/td>.*?<td>.*?\">(.*?)<\/a>', re.S) 
	solution = re.compile('方案.*?<td>(.*?)<\/td>', re.S)
	makeup = re.compile('厂商补丁.*?href=\"(.*?)\"', re.S)
	sign = re.compile('验证信息.*?<td>(.*?)<\/td>', re.S)
	file = re.compile('漏洞附件.*?<td>(.*?)<\/td>', re.S)
	for url in ult:
		dic = dict()
		brow.get(url)
		html = brow.page_source
		
		#name
		res = re.findall(name, html)
		dic['漏洞名称'] = res[0]
		
		#id
		res = re.findall(ID, html) 
		dic['CNVD-ID'] = res[0]
		
		#date
		res = re.findall(date, html)
		dic['公开日期'] = res[0]
		
		#level
		res = re.findall(level, html)
		dic['危害级别'] = res[0]
		
		#goods
		lis = re.findall(goods, html)[0].split('\n')
		for i in range(len(lis)):
   	 		lis[i] = re.sub('\t', ' ', lis[i])
    		lis[i] = re.sub('<br/>', ' ', lis[i])
    		lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		dic['影响产品'] = lis
		
		#CVE
		res = re.findall(CVE, html)
		dic['CVE-ID'] = res[0]
		
		#discr
		res = re.findall(discr, html)
		lis = res[0].split('\n')
		for i in range(len(lis)):
			lis[i] = re.sub('\t', ' ', lis[i])
			lis[i] = re.sub('<br/>', ' ', lis[i])
			lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		dis_string = ''
		for i in range(len(lis)):
			dis_string = dis_string + lis[i]
		dic['漏洞描述'] = dis_string
		
		#type
		res = re.findall(typ, html)
		lis = res[0].split('\n')
		for i in range(len(lis)):
			lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		dic['漏洞类型'] = lis[0]
		
		#href
		res = re.findall(href, html)
		dic['参考链接'] = res[0]
		
		#solution
		lis = re.findall(solution, html)[0].split('\n')
		for i in range(len(lis)):
			lis[i] = re.sub('\t', ' ', lis[i])
			lis[i] = re.sub('<br/>', ' ', lis[i])
			lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		so_string = ''
		for i in range(len(lis)):
			so_string = so_string + lis[i]
		dic['漏洞解决方案'] = so_string
		
		#makeup
		res = re.findall(makeup, html)[0]
		so_string = 'https://www.cnvd.org.cn' + res
		dic['厂商补丁'] = so_string
		
		#sign
		lis = re.findall(sign, html)[0].split('\n')
		for i in range(len(lis)):
			lis[i] = re.sub('\t', ' ', lis[i])
			lis[i] = re.sub('<br/>', ' ', lis[i])
			lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		so_string = ''
		for i in range(len(lis)):
			so_string = so_string + lis[i]
		dic['验证信息'] = so_string
		
		#file
		lis = re.findall(file, html)[0].split('\n')
		for i in range(len(lis)):
			lis[i] = re.sub('\t', ' ', lis[i])
			lis[i] = re.sub('<br/>', ' ', lis[i])
			lis[i] = lis[i].strip()
		lis = list(filter(None, lis))
		so_string = ''
		for i in range(len(lis)):
			so_string = so_string + lis[i]
		dic['漏洞附件'] = so_string
		#单个漏洞信息爬取完毕，保存在dic中
		#dic漏洞信息保存到数据库
		result = collection.insert_one(dic)
