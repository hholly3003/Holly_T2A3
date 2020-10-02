import bot
from server import check_updates
import sys


chatbot = bot.TelegramChatbot("config.cfg")
print("Chatbot is running . . . .")   
update_id = None
EXIT_MODE = False

while True:
    try:
        if not EXIT_MODE:
            update_id = check_updates(update_id)
        else:
            sys.exit()
    except KeyboardInterrupt:
        print('Interrupt by user..')
        break