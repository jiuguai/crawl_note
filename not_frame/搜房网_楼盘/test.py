import pymongo

# 连接
cli = pymongo.MongoClient("127.0.0.1",port=27017)

# 创建数据库
# db = cli.zhihu

# 创建集合
collection = cli.zhihu.qa



# 添加
collection.insert([{"username":"zero",'type':1},
    {"username":"wind",'type':2}

    ])
collection.insert({"user":"zero"})

# 查找数据
## 返回多条
cursor = collection.find({'username':"zero"})
print(list(cursor))
## 返回一条
data1 = collection.find_one({'user':"zero"})
print(data1)

# 更新
collection.update_one({"user":"zero"},{"$set":{"age":18,"type":"test"}})
collection.update_many({"username":"zero"},{"$set":{"age":18}})

# 删除
collection.delete_one({"usernam":"zero"})
collection.delete_many({"usernam":"zero"})
cli.close()