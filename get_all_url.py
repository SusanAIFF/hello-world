ult = []
def get_url_list(ult, start_url):
#爬取1-50页所有漏洞的网页链接，保存到ult的列表中
	brow = webdriver.Chrome()

	for i in range(2):
		url = start_url + str(i*20)
		brow.get(url)

		html = brow.page_source
		soup = bs(html, 'lxml')
		collect = soup.find_all(name = "a")

		for j in range(20):
			ult.append(collect[j].attrs['href'])

		time.sleep(1)

	brow.close()

