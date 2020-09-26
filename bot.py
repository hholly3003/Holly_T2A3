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
    