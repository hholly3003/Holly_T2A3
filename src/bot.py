import requests
import json
import configparser
import os
from datetime import datetime
from requests.models import Response


class TelegramChatbot:
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = f"https://api.telegram.org/bot{self.token}/"

    @staticmethod
    def read_token_from_config_file(config):
        """Getting the token key from config files

        :param config: [config files contain token key]
        :type config: [file]
        :return: [the valus of creds and token]
        :rtype: [str]
        """
        parser = configparser.ConfigParser()
        parser.read(config)
        return parser.get("creds", "token")

    def get_updates(self, offset=None) -> Response:
        """getting incoming messages from the user

        :param offset: getting the updates of specific message,
        defaults to None
        :type offset: [int], optional
        :return: [response in JSON format]
        :rtype: Response
        """
        url = self.base + "getUpdates?timeout=60"
        if offset:
            url = url + f"&offset={offset + 1}"
        response = requests.get(url)
        return response

    def get_content(self, data) -> list:
        """Extracting data from JSON File and store
        important data into parameter list.

        :param data: [content obtain from JSON File]
        :type data: [list]
        :return: [list of parameter_list that have tuple on each element]
        :rtype: list
        """
        parameter_list = []

        for update in data["result"]:
            update_id = update["update_id"]
            sender = update["message"]["from"]["id"]
            first_name = update["message"]["from"].get("first_name", "")
            last_name = update["message"]["from"].get("last_name", "")
            date = update["message"]["date"]
            file_id = ""
            file_size = ""
            try:
                text = update["message"]["text"]
            except Exception:
                text = ""
                file_id = update["message"]["photo"][0].get("file_id", "")
                file_size = update["message"]["photo"][0].get("file_size", "")
            parameters = (sender, first_name, last_name, text,
                          file_id, update_id, file_size, date)
            parameter_list.append(parameters)
        return parameter_list

    def get_file_details(self, file_id: str) -> dict:
        """Getting file details such as file path and file size
        using the method getFile available from API

        :param file_id: [parameter required to obtain the file details]
        :type file_id: str
        :return: [dictionary that contain all file details attributes]
        :rtype: dict
        """
        url = self.base + f"getFile?file_id={file_id}"
        file_details = requests.get(url)
        json_files_details = json.loads(file_details.content)
        return json_files_details.get("result")

    def send_message(self, message: str, chat_id: int) -> None:
        """Send message in a string to specified user based on their chat_id
        using sendMessage method in the API

        :param message: [Content of the message to send]
        :type message: str
        :param chat_id: [recipient]
        :type chat_id: int
        """
        url = self.base + f"sendMessage?chat_id={chat_id}&text={message}"
        if message is not None:
            requests.post(url)

    def display_incoming_message(self, date: int, first_name: str,
                                 last_name: str, text: str, file_size: int):
        """Print out all incoming message to the terminal

        :param date: [date the message is received by Telegram Server]
        :type date: [int]
        :param first_name: [the sender first name]
        :type first_name: [str]
        :param last_name: [sendes's last name]
        :type last_name: [str]
        :param text: [content of text message]
        :type text: [str]
        :param file_size: [file size of photo message]
        :type file_size: [int]
        """
        print("[<<<] Message Received %s" % datetime.fromtimestamp
              (date).strftime("%d-%m-%Y %H:%M:%S"))

        if not file_size:
            content = text
            print(f"\tText: {content}")
        else:
            print("\tThe message received is a file")
            print(f"\tFile Size: {file_size} bytes")

        print(f"\tFrom: {first_name} {last_name}")
        print("-" * os.get_terminal_size().columns)
