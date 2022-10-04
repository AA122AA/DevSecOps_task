import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017, username="artem", password="0000")
db = client.serv_2_db # Создаем бд
db.command("createUser", "artem", pwd="0000", roles=["readWrite"]) # Создаем пользователя с ролью readWrite
text = db.text # Создаем коллекцию text 
docs = text.insert_one({"text": "hello world"}) # Вставляем документ 