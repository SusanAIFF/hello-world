import json
import pymongo
client = pymongo.MongoClient(host = 'localhost', port=27017)
#创建用户的test数据库
db = client.test
#创建数据库中的表单
collection = db.students
dblist = client.list_database_names()
test_collection_list = db.list_collection_names()

#插入数据，完美支持字典格式，嗨森！
student = {
    'name'= 'Susan',
    'age'= '20',
    'id'= '334214',
    'gender': 'male'
}
    #insert
result = collection.insert_one(student)#返回内存地址
result.inserted_id      #插入文档id值

mylist = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]
result = collection.insert_many(mylist) ##自己指定id输入


#re查询
myquery = { "name": { "$regex": "^R" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#指定查询
myquery = { "name": "RUNOOB" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#指定数据内容查询
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
  print(x)
