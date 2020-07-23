import pymongo
from pymongo import MongoClient
from datetime import datetime as dt
from pprint import pprint as pp
from bson.objectid import ObjectId

uri = 'mongodb://192.168.59.128:27017/'
client = MongoClient(uri, username='root', password='Root@1234.')


# db = client['test-database']
# db = client.test_database
# collection = db['test-collection']
# collection = db.test_collection
db = client.test
posts = db.posts

# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": dt.utcnow()}
#
# post_id = posts.insert_one(post).inserted_id
# print(post_id)

# print(db.list_collection_names())
# pp(posts.find_one())
# pp(posts.find_one({"author": "Mike"}))
# pp(posts.find_one({"author": "Eliot"}))
# pp(posts.find_one({"_id": post_id}))
# post_id_as_str = str(post_id)
# posts.find_one({"_id": post_id_as_str})  # No result
# posts.find_one({'_id': ObjectId(post_id)})  # correct

# new_posts = [{
#     "author": "Mike",
#     "text": "Another post!",
#     "tags": ["bulk", "insert"],
#     "date": dt(2009, 11, 12, 11, 14)},
#     {"author": "Eliot",
#      "title": "MongoDB is fun",
#      "text": "and pretty easy too!",
#      "date": dt(2009, 11, 10, 10, 45)}]
#
# result = posts.insert_many(new_posts)
# pp(result.inserted_ids)

# for post in posts.find():
#     pp(post)
#
# print('\n----------------------------------')
#
# for post in posts.find({"author": "Mike"}):
#     pp(post)
#
# print('\n----------------------------------')
#
# print(posts.count_documents({}))
# print(posts.count_documents({"author": "Mike"}))
#
# d = dt(2009, 11, 12, 12)
# for post in posts.find({"date": {"$lt": d}}).sort("author"):
#     pp(post)

# result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
# print(result)
# print(sorted(list(db.profiles.index_information())))

# user_profiles = [{'user_id': 211, 'name': 'Luke'}, {'user_id': 212, 'name': 'Ziltoid'}]
# result = db.profiles.insert_many(user_profiles)
# pp(result)

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
pp(result)
result = db.profiles.insert_one(duplicate_profile)
pp(result)
