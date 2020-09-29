import requests
import json
import configparser
import os
from datetime import datetime

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
    def get_updates(self, offset = None):
        #use the getUpdates method to get all data and set a timeout parameter of 60s
        url = self.base + "getUpdates?timeout=60"
        # if the offset parameter is provided, will add the offset parameter in the url
        if offset:
            url = url + f"&offset={offset + 1}"
        response = requests.get(url)
        json_response = json.loads(response.content)
        parameter_list = []

        for update in json_response["result"]:
            update_id = update["update_id"]
            sender = update["message"]["from"]["id"]    #Sender / Chat ID
            first_name = update["message"]["from"].get("first_name", "")
            last_name = update["message"]["from"].get("last_name", "")
            date = update["message"]["date"]
            file_id = None
            try:
                text = update["message"]["text"]
            except:
                text = None
                file_id = update["message"]["photo"][0].get("file_id", "")
            
            parameters = (sender, first_name, last_name, text, file_id, update_id, date)
            parameter_list.append(parameters)
        return parameter_list

    
    #get the file info
    def get_file_details(self, file_id):
        url = self.base + f"getFile?file_id={file_id}"
        file_details = requests.get(url)
        json_files_details =  json.loads(file_details.content)
        return json_files_details.get("result")
    
    def download_photo(self, file_path):
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        print(url)
        photo = requests.get(url)
        
        if photo.status_code == 200:
            try:
                with open("photos/image.jpg", "wb") as image:
                    image.write(photo.content)
            except FileNotFoundError:
                error = "Download Fail - folder photos is not exist. Please create one"
                return error
    
    #Sending message or response from bot to the specified user
    def send_message(self, message, chat_id):
        #use the sendMessage method and specify the reciever and text to send
        url = self.base + f"sendMessage?chat_id={chat_id}&text={message}"
        # Only if there is message to send, it will sends a post request
        if message is not None:
            requests.post(url)

    # Print all incoming message
    def print_input(self, data):
        print("[<<<] Message Received %s" % datetime.fromtimestamp(data["message"]["date"]).strftime("%d-%m-%Y %H:%M:%S"))
        
        # Obtaining the sender details
        first_name = data["message"]["from"].get("first_name", "")
        last_name = data["message"]["from"].get("last_name", "")
        
        #Check if the message is a text or photo
        try:
            content = data["message"]["text"]
            print(f"\tText: {content}")
        except:
            filesize = data["message"]["photo"][0].get("file_size", "")
            print("\tThe message received is a file")
            print(f"\tFile Size: {filesize} bytes")

        print(f"\tFrom: {first_name} {last_name}")
        print("-" * os.get_terminal_size().columns)
    
    