import requests
import json





class telegram_chatbot():

    def __init__(self, config):
        self.token = config
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=10"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        print(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            
            requests.get(url)



t=telegram_chatbot("2140031887:AAGQH2FIYkwjXCFkMpcurakML3EJd0ITA8Q")
