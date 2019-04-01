from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e28-jxucw.mongodb.net/test?retryWrites=true"
client = MongoClient(uri)
db = client.db_service
bikes_collection = db ["bike"]