from monitor import telegram_chatbot
import pymongo
from pymongo import MongoClient
API_Key="2140031887:AAGQH2FIYkwjXCFkMpcurakML3EJd0ITA8Q"
Mongo="mongodb+srv://rohan:Z9RicwzgtBzh4hzI@cluster0.29lux.mongodb.net/Isa_da?retryWrites=true&w=majority"

bot = telegram_chatbot(API_Key)
###########connecting to mongo client#############
cluster=MongoClient(Mongo)
db=cluster["Isa_da"]



def make_reply(msg):
    reply = None
    if msg is not None:
        reply = "okay\n hellow \n how are you"
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    
    try:
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                from_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)
    except KeyError:
        print("Key not found")

