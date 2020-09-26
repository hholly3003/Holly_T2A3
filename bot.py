import requests
import json
import configparser

class TelegramChatbot:
    def __init__(self,config):
        self.token = self.read_token_from_config_file(config)
        self.base = f"https://api.telegram.org/bot{self.token}/"
    
    #getting the token credentials for the telegram bot from the config file
    @staticmethod
    def read_token_from_config_file(config):
        parser = configparser.ConfigParser()
        parser.read(config)
    
    #getting all updates or messages that is sent to the bot
    def get_updates(self, offset = None):
        #use the getUpdates method to get all data and set a timeout parameter of 60s
        url = self.base + "getUpdates?timeout=60"
        # if the offset parameter is provided, will add the offset parameter in the url
        if offset:
            url = url + f"&offset={offset + 1}"
        response = requests.get(url)
        return json.loads(response.content)
    
    #Sending message or response from bot to the specified user
    def send_message(self, message, chat_id):
        #use the sendMessage method and specify the reciever and text to send
        url = self.base + f"sendMessage?chat_id={chat_id}&text={message}"
        # Only if there is message to send, it will sends a post request
        if message is not None:
            response = requests.post(url)

