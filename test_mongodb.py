
from pymongo.mongo_client import MongoClient

uri="mongodb+srv://mahamaniparvas_db_user:maha994@cluster0.ut5ipqv.mongodb.net/?retryWrites=true&w=majority&tls=true"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)    