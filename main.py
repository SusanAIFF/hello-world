#启动MongoDB，爬取漏洞链接，漏洞信息
import pymongo
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
def main1():
	start_url = "https://ics.cnvd.org.cn/?max=20&offset="
	#用户
	client = pymongo.MongoClient("mongodb://localhost:27017")
	#数据库
	database = client.info
	#表单
	collection = database.bugs
	get_url_list(ult, start_url)
	get_page(ult, fpath)
    
    
#查询窗口
import pymongo
def main2():
    