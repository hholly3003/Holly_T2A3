import unittest
from bot import TelegramChatbot
import json

class TestTelegramChatbotClass(unittest.TestCase):
    def setUp(self):
        self.bot = TelegramChatbot("config.cfg")
    
    def test_init(self):
        """Test TelegramChatbot"""
        try:
            self.bot.token
            self.bot.base
        except Exception as error:
            self.assertTrue(False, error)
    
    """
    Unable to do the automated testing below because unable to mock the input
    It need to wait user input via Telegram Chat
    """
    # def test_get_updates(self):
    #     """ Test that the response receive is OK"""
    #     result = self.bot.get_updates(offset = None)
    #     self.assertEqual(result.status_code, 200, msg=f"Status code was {result.status_code} not 200. ")
    
    def test_get_content(self):
        """Test that the data is containing a list with 8 elements"""
        data = self.bot.get_updates()
        content = self.bot.get_content(json.loads(data.content))
        self.assertTrue(isinstance(content, list),msg = "data is not type of List")
        self.assertEqual(len(content[0]),8, msg=f"There are only {len(content[0])} elements, It should contain 8 elements")
        self.assertIsNotNone(content[0],msg = f"The response is an empty list")
    
    def test_get_file_details(self):
        """Test to check the file details receive is a dictionary"""
        data = self.bot.get_updates()
        file_id = self.bot.get_content(json.loads(data.content))[0][4]
        if file_id:
            result = self.bot.get_file_details(file_id)
            self.assertTrue(isinstance(result, dict),msg = "result is not in dictionary")

    def test_send_message(self):
        """Test sending message to user and message is as string, chat_id is an int"""
        message = "Hello there"
        data = self.bot.get_updates()
        content = self.bot.get_content(json.loads(data.content))
        chat_id = content[0][0]
        self.bot.send_message(message, chat_id)
        
        self.assertTrue(isinstance(message, str), msg= f"The message is a {type(message)}, It should be a str")
        self.assertTrue(isinstance(chat_id, int), msg= f"The chat id is a {type(chat_id)}, It should be an int")