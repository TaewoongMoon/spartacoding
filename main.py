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




from pymongo import MongoClient
url = 'mongodb://Moony:jullie6096@ds011459.mlab.com:11459/heroku_nxq5fr78?retryWrites=false'
client = MongoClient(url)
db = client['heroku_nxq5fr78']
collection = db['test']

# collection.insert_one({'name':'bobby','age':21})
# collection.insert_one({'name':'kay','age':27})
# collection.insert_one({'name':'john', 'age':30})

# rows = collection.find({})
# collection.update_one
# collection.delete_one
# for row in rows:
#     print(row)

# all_collection = list(collection.find())
#  print(all_collection['name'])
rows = collection.find()
result = []
for row in rows:
  if 'age' in row:
    if row['age'] > 21:
      result.append(row['age'])

max_age = max(result)

rows = collection.find()

max_age_result = []

for row in rows:
  if 'age' in row:
    if row['age'] == max_age:
      max_age_result.append(row)

print(len(max_age_result))