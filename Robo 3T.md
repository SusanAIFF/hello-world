链接mongodb数据库
双击robo3t.exe
create--填写一个名字，一般项目名字，比如sms或中文都可
Stock  Management System  ,股票管理系统 ，简写为SMS
点击test ，没问题就save
点击connect

3，查询表里的数据条数
db.getCollection('curriculums').find({}).count();
即，后面加上 .count()

4，col 集合中的数据按字段 likes 的降序排列：
db.col.find({}).sort({"likes":-1})

5，update数据
db.courses.updateMany(
{ "cid" : "5bc562345dbd0e4618aa9484"},
{ set:{字段名:数值}}
)

6，查询字段内的字段
数据内的字段是这样的，很多数据里是多个学生，这里就想查询包含学生id是34的：

"teachers" : [ 
        1.0, 
        2.0, 
        3.0
    ],
    "students" : [ 
        {
            "id" : 8,
            "name" : "测试学生3",
            "age" : 8,
            "sex" : "male",
            "region" : "上海"
        }
    ]
想要查出id是34的数据
db.getCollection('classes').find({"students.id":34})

刚还尝试的一个方式是：全文检索
MongoDB 在 2.6 版本以后是默认开启全文检索的，如果你使用之前的版本，你需要使用以下代码来启用全文检索:
db.adminCommand({setParameter:true,textSearchEnabled:true})
对 post_text 字段建立全文索引
db.posts.ensureIndex({post_text:"text"})

db.getCollection('classes').ensureIndex({students:"text"})
对students字段建立全文索引
使用全文索引
db.posts.find({$text:{$search:"runoob"}})

db.getCollection('classes').find({$text:{$search:"23401"}})
搜索内容不对
,可能的原因是id是int类型。全文索引是针对string类型的。

7，模糊查询
sql:
select * from user where name like "%花%";

mongo:

db.user.find(name:/花/);

例子：查看students里的name包含 ”测试“ 的数据。
db.getCollection('classes').find({"students.name":/测试/})
若是以a为开头的：
db.getCollection('classes').find({"students.name":/^测试/})

8,数组查询
实例，一节课的老师的id可能有多个，这样：
"teachers" : [ 391, 659, 1534 ]
需求：查询包含老师id为1534的所有的数据
很简单~
db.getCollection('classes').find({teachers:1534})

9，查询只显示部分字段
classes表中只显示id和title两个字段
下面的 status:"700" 为查询条件
db.getCollection('classes').find({status:"700"},{_id:1,title:1})

10,给数组追加一个数据
需求：给数据内的老师id多加一个1534，即让老师多一节课,如果已经存在了就不添加了。

db.getCollection('classes').update({"_id" : ObjectId("5bc995e391e99773f9096114")},{$addToSet:{ "teachers":NumberInt(1539)}})
这里使用的是$addToSet

添加2个数据。需要和$each配合
db.getCollection('classes').update({"_id" : ObjectId("5bc995e391e99773f9096114")},{$addToSet:{ "teachers":{$each:[NumberInt(11232),NumberInt(2800)]}})

11,查询一个字段为不同值的时候
需求：title为‘K2D23’或‘K2D41’或’S1050‘的数据
db.getCollection('classes').find({title:{$in:['K2D23','K2D41','S1050']}})
这里使用的是$in
资料来自于：http://flamepeak.com/2016/10/25/MongoDB-learning-part3-20161025/
