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
	get_page(ult)
    
    
#查询窗口
import pymongo
def main2():
	client = pymongo.MongoClient("mongodb://localhost:27017")
	#数据库
	database = client.info
	#表单
	collection = database['bugs']
	while(True):
		try:
			n = eval(input('''请选择要使用的功能：\n1  根据漏洞名查询\n2  根据CNVD_ID查询\n3  根据CVE_ID查询\n4  根据日期查询\n5  退出系统\n'''))
			if n < 1 or n > 5:
				print("输入有误，请重试\n\n")
				continue
			
			if n==1:
				name = input("输入漏洞名称: ")
				re = {'漏洞名称': {'$regex': name}}
				info_list = collection.find(re)
				for item in info_list:
					print(item)
			
			if n==2:
				name = input("输入CNVD_ID: ")
				re = {'CNVD-ID': {'$regex': name}}
				info_list = collection.find(re)
				for item in info_list:
					print(item)
			
			if n==3:
				name = input("输入CVE_ID: ")
				re = {'CVE-ID': {'$regex': name}}
				info_list = collection.find(re)
				for item in info_list:
					print(item)
			
			if n==4:
				name = input("输入日期(XXXX-XX-XX): ")
				re = {'公开日期': {'$regex': name}}
				info_list = collection.find(re)
				for item in info_list:
					print(item)
			
			if n==5:
				break
				
		except:
			print('\n\n')
			continue
