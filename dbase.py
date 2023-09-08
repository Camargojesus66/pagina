from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://Jesus:camargojesus66@cluster0.te1cm6c.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["paginatennisjc"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db

