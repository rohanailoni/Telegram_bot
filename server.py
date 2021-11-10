import os
from Bot import telegram_chatbot
from pymongo import MongoClient
from Monitor import checker
import schedule
import time
API_Key="2140031887:AAGQH2FIYkwjXCFkMpcurakML3EJd0ITA8Q"
Mongo="mongodb+srv://rohan:Z9RicwzgtBzh4hzI@cluster0.29lux.mongodb.net/Isa_da?retryWrites=true&w=majority"

bot = telegram_chatbot(API_Key)
###########connecting to mongo client#############
cluster=MongoClient(Mongo)
db=cluster["Isa_da"]
collection=db["status"]
######################################
Owner_id="1246896341"

def make_reply(msg):
    reply = None
    print(msg)
    if msg is not None:
        if msg=="/status":
            reply=""
            
            dict=checker().Status()
            collection.insert_one(dict)
            for i in dict:
                reply=reply+i+":--"+str(dict[i])+"\n\n\n"
        elif msg=="/battery":
            reply=""
            dict=checker().Battery()
            for i in dict:
                reply=reply+i+":--"+str(dict[i])+"\n\n\n"
        elif msg=="/ram":
            reply=""
            
            dict=checker().Ram_usage()
            
            for i in dict:
                reply=reply+i+":--"+str(dict[i])+"\n\n\n"
        elif msg=="/cpu":
            reply=""
            
            dict=checker().cpu_usage()
            
            for i in dict:
                reply=reply+i+":--"+str(dict[i])+"\n\n\n"
        else:

            reply = "okay\n hellow \n how are you"
    return reply


def critical_changer():
    reply=".............Automatic Message Written in python.......................\n\n\n\n"
    dict=checker().Status()
    collection.insert_one(dict)
    for i in dict:
        reply=reply+i+":--"+str(dict[i])+"\n"
    bot.send_message(reply,Owner_id)

#schedule.every(10).seconds.do(critical_changer)
i=0
update_id = None
while True:
    #schedule.run_pending()
    print(i)
    updates = bot.get_updates(offset=update_id)
    i+=1
    if i==10:
        critical_changer()
        i=0
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

