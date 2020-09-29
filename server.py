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
            print(item)
            update_id = item["update_id"]
            chatbot.print_input(item)
            sender = item["message"]["from"]["id"]
            try:
                message = item["message"]["text"]
                reply = bot_response(message)
                chatbot.send_message(reply, sender)
            except:
                file_id = item["message"]["photo"][0].get("file_id", "")
                file_details = chatbot.get_file_details(file_id)
                file_path = file_details.get("file_path", "")
                photo = chatbot.download_photo(file_path)
                if isinstance(photo,str):
                    chatbot.send_message(photo,sender)
                