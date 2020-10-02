import requests
import json
import configparser
import os
from datetime import datetime
from requests.models import Response

class TelegramChatbot:
    def __init__(self,config):
        self.token = self.read_token_from_config_file(config)
        self.base = f"https://api.telegram.org/bot{self.token}/"
    
    #getting the token credentials for the telegram bot from the config file
    @staticmethod
    def read_token_from_config_file(config):
        parser = configparser.ConfigParser()
        parser.read(config)
        return parser.get("creds","token")
    
    #getting all updates or messages that is sent to the bot
    def get_updates(self, offset = None) -> Response:
        #use the getUpdates method to get all data and set a timeout parameter of 60s
        url = self.base + "getUpdates?timeout=60"
        # if the offset parameter is provided, will add the offset parameter in the url
        if offset:
            url = url + f"&offset={offset + 1}"
        response = requests.get(url)
        return response

    def get_content(self, data) -> list:
        parameter_list = []

        for update in data["result"]:
            update_id = update["update_id"]
            sender = update["message"]["from"]["id"]    #Sender / Chat ID
            first_name = update["message"]["from"].get("first_name", "")
            last_name = update["message"]["from"].get("last_name", "")
            date = update["message"]["date"]
            file_id = ""
            file_size = ""
            try:
                text = update["message"]["text"]
            except:
                text = ""
                file_id = update["message"]["photo"][0].get("file_id", "")
                file_size = update["message"]["photo"][0].get("file_size", "")
            
            parameters = (sender, first_name, last_name, text, file_id, update_id, file_size, date)
            parameter_list.append(parameters)
        return parameter_list

    #get the file info
    def get_file_details(self, file_id) -> dict:
        url = self.base + f"getFile?file_id={file_id}"
        file_details = requests.get(url)
        json_files_details =  json.loads(file_details.content)
        return json_files_details.get("result")
        
    #Sending message or response from bot to the specified user
    def send_message(self, message : str, chat_id: int) -> None:
        #use the sendMessage method and specify the reciever and text to send
        url = self.base + f"sendMessage?chat_id={chat_id}&text={message}"
        # Only if there is message to send, it will sends a post request
        if message is not None:
            requests.post(url)

    # Print all incoming message
    def display_incoming_message(self, date, first_name, last_name, text, file_size):
        print("[<<<] Message Received %s" % datetime.fromtimestamp(date).strftime("%d-%m-%Y %H:%M:%S"))
      
        # Check if the message is a text or photo
        if not file_size:
            content = text
            print(f"\tText: {content}")
        else:
            print("\tThe message received is a file")
            print(f"\tFile Size: {file_size} bytes")

        print(f"\tFrom: {first_name} {last_name}")
        print("-" * os.get_terminal_size().columns)
