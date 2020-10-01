import unittest
from server import *
from bot import TelegramChatbot

class TestServerFunctions(unittest.TestCase):
    def setUp(self):
        self.bot = TelegramChatbot("config.cfg")

    def test_bot_response(self):
        bot_reply = bot_response("Hello")
        expected_message = "I have stored message : 'Hello' into log file"
        self.assertEqual(bot_reply,expected_message,msg = f"The expected message is {expected_message}")

    def test_check_updates(self):
        data = self.bot.get_updates()
        content = self.bot.get_content(json.loads(data.content))
        update_id = content[0][5]
        
        result = check_updates(update_id)
        self.assertTrue(isinstance(result, int), msg = "An unexpected type of updates received")
    
    def test_run_command(self):
        data = self.bot.get_updates()
        content = self.bot.get_content(json.loads(data.content))
        content = content[0]

        run_command(content[0],content[1], content[2],content[3], content[4], content[5], content[6],content[7])
        