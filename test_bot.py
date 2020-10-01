import unittest
from bot import TelegramChatbot
import json

class TestBotClass(unittest.TestCase):
    def setUp(self):
        self.bot = TelegramChatbot("config.cfg")
    
    def test_init(self):
        """Test TelegramChatbot"""
        try:
            self.bot.token
            self.bot.base
        except Exception as error:
            self.assertTrue(False, error)
    
    def test_get_updates(self):
        result = self.bot.get_updates()
        self.assertEqual(result.status_code, 200, msg=f"Status code was {result.status_code} not 200. ")
        
        result = self.bot.get_updates()
        self.assertTrue(result.json()['ok'], True)
    
    def test_get_content(self):
        data = self.bot.get_updates()
        result = self.bot.get_content(json.loads(data.content))
        print(result)
        self.assertIsNotNone(result[0],msg = f"The response is an empty list")
    
    def test_get_file_details(self):
        pass

    def test_send_message(self):
        pass

    def test_display_incoming_message(self):
        pass
        