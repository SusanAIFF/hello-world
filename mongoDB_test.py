import pymongo
client = pymongo.MongoClient()
db = client['test']
col = db['test_collection']
dic1 = {"漏洞名称": "ABB zenon Editor存在dll劫持漏洞", "CNVD-ID": "CNVD-2019-30358", "公开日期": "2019-10-06", "危害级别": "高", "影响产品": ["ABB集团 zenon Editor v7.50 32 bit"], "CVE-ID": "", "漏洞描述": "ABB集团位列全球500强企业，总部位于瑞士苏黎世，致力于为工业和电力行业客户提供解决方案。ABB zenon Editor存在dll劫持漏洞，攻击者可利用该漏洞获取服务器权限。", "漏洞类型": "通用型漏洞", "参考链接": "", "漏洞解决方案": "厂商尚未提供修复方案，请关注厂商主页更新：https://new.abb.com/cn/", "厂商补丁": "https://www.cnvd.org.cn/patchInfo/show/177347", "验证信息": "已验证", "漏洞附件": "附件暂不公开"}
dic2 = {"漏洞名称": "Advantech WebAccess/SCADA缓冲区溢出漏洞（CNVD-2019-32464）", "CNVD-ID": "CNVD-2019-32464", "公开日期": "2019-09-21", "危害级别": "高", "影响产品": ["Advantech WebAccess/SCADA &lt;=8.3.5"], "CVE-ID": "CVE-2019-10989", "漏洞描述": "Advantech WebAccess/SCADA是中国台湾研华（Advantech）公司的一套基于浏览器架构的SCADA软件。该软件支持动态图形显示和实时数据控制，并提供远程控制和管理自动化设备的功能。Advantech WebAccess/SCADA 8.3.5及之前版本中存在缓冲区溢出漏洞，攻击者可利用该漏洞执行代码。", "漏洞类型": "通用型漏洞", "参考链接": "", "漏洞解决方案": "厂商已发布了漏洞修复程序，请及时关注更新：https://www.advantech.com/", "厂商补丁": "https://www.cnvd.org.cn/patchInfo/show/181497", "验证信息": "(暂无验证信息)", "漏洞附件": "(无附件)"}
x = col.insert_many([dic1, dic2])
for x in col.find():
	print(x)
