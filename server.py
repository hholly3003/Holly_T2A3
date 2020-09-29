import bot
import os

# bot replying to the message 
def bot_response(message):
    reply = None
    if message is not None:
        reply = f"I have stored message : '{message}' into log file"
    return reply

update_id = None
print("Bot is running ...")
while True:    
    # Instantiate the telegramchatbot
    chatbot = bot.TelegramChatbot("config.cfg")
    # Check for any update or input given to the bots
    updates = chatbot.get_updates(offset = update_id)
    updates = updates[0]
    if updates:
        
        update_id = updates[5]
        print(update_id)
        if updates[3] != None:
            reply = bot_response(updates[3])
            chatbot.send_message(reply, updates[0])
        if updates[4] != None:
            file_details = chatbot.get_file_details(updates[4])
            file_path = file_details.get("file_path", "")
            file_name = file_path.split("/")[1]
            download_status = chatbot.download_photo(file_path, file_name)
            chatbot.send_message(download_status,updates[0])
                