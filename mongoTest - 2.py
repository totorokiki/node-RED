from pymongo import MongoClient

conn = MongoClient('192.168.0.12', 27017) # MongoClient('라즈베리파이 ip', 포트번호)

db = conn.Test
coll = db.collection

post = {"name" : "user01",
		"Follow" : 57}

x = coll.insert_one(post)
print(x)
