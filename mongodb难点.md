安装：
从官网下载msi文件后，傻瓜安装会卡住不动，需要重新建一个路径
MongoDB/Server/4.0/
我选择的是4.0，安装时选择custom选项，不要选上compass的安装选项，电脑桌面完全一片黑，但任务栏能正常使用
查阅大量资料也只是解决了连接问题，还是未能完全正常启动服务。

目前解决方法：
用cd命令打开mongod.exe所在的目录，并输入mongod.exe --nojournal --dbpath .（在系统的服务进程中，MongoDB还是未启动）
启动MongoDB服务后，在idle中正常使用即可

爬取数据可能重复，使用try：except：语句

查看条数：
db['collection名字'].count()
