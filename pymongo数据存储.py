import json
import pymongo
client = pymongo.MongoClient(host = 'localhost', port=27017)
#创建用户的test数据库
db = client.test
#创建数据库中的表单
collection = db.students
#插入数据，完美支持字典格式，嗨森！
student = {
    'name'= 'Susan',
    'age'= '20',
    'id'= '334214',
    'gender': 'male'
}
    #insert()函数
result = collection.insert(student)
