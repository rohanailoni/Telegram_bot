from typing import Collection
import pymongo
from pymongo import MongoClient
API_Key="2140031887:AAGQH2FIYkwjXCFkMpcurakML3EJd0ITA8Q"
Mongo="mongodb+srv://rohan:Z9RicwzgtBzh4hzI@cluster0.29lux.mongodb.net/Isa_da?retryWrites=true&w=majority"

###########connecting to mongo client#############
cluster=MongoClient(Mongo)
db=cluster["Isa_da"]
collection=db["status"]
###################################################


post={"name":"rohan","score":5}
collection.insert_one(post)
