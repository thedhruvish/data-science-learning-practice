import pymongo
M_URL = "mongodb://localhost:27017"

client = pymongo.MongoClient(M_URL)

mydb = client["py"]
mycol = mydb["user"]

# show the collection
# print(mydb.list_collections)
# print(mydb.list_collection_names())

data = [
    {"name":"jay","age":18,"address":"Surat Gujrat"},
    {"name":"ronak","age":52,"address":"Surat Gujrat"},
    {"name":"kem","age":145,"address":"Surat Gujrat"},
    {"name":"raj","age":58,"address":"Surat Gujrat"},
]

# mycol.insert_one(data)
# mycol.insert_many(data)

# i = mycol.find_one()
# print(i)

for i in mycol.find():
    print(i)

da = mycol.find({},{"name":"kem"})


for i in da:
    print(i)