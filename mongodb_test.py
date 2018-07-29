import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client.Python3_docs
collection =db.themes
result = collection.insert(cotent)



# 1. 先链接数据库
# 2. 创建新数据库或连接旧数据库
# 3. 在上面的数据库下创建表
# 4. 在特定数据库的特定表下插入数据

# 数据库名.表名.aggregate

db = client.mydb
collection = db.students


