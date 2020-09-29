import bot
import os

# bot replying to the message 
def bot_response(message):
    reply = None
    if message is not None:
        reply = f"Bot : {message}"
    return reply

update_id = None
print("Bot is running ...")

while True:    
    # Instantiate the telegramchatbot
    chatbot = bot.TelegramChatbot("config.cfg")
    # Check for any update or input given to the bots
    updates = chatbot.get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            chatbot.print_input(item)
            try:
                message = item["message"]["text"]
            except:
                message = None
            sender = item["message"]["from"]["id"]
            reply = bot_response(message)
            chatbot.send_message(reply, sender)