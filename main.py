from pymongo import MongoClient
url = 'mongodb://Moony:jullie6096@ds011459.mlab.com:11459/heroku_nxq5fr78?retryWrites=false'
client = MongoClient(url)
db = client['heroku_nxq5fr78']
collection = db['test']

collection.insert_one({'a':'b'})

rows = collection.find({})
collection.update_one
collection.delete_one
for row in rows:
    print(row)
