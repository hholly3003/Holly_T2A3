import bot
import os

# bot replying to the message 
def bot_response(message):
    reply = None
    if message is not None:
        reply = f"I have stored message : '{message}' into log file"
    return reply

def run_command(sender, first_name, last_name, text, file_id, update_id, file_size, date):
    global EXIT_MODE
    if text == "/help":
        chatbot.send_message(f"No help today. Sorry, {first_name}", sender)
        
    elif text == '/start':
        chatbot.send_message(f"Hello {first_name}! Just send me a text or picture file", sender)
        
    elif text == '/exit':
        chatbot.send_message("Terminating the bot", sender)
        EXIT_MODE = True

    elif file_id is not None:
        chatbot.display_incoming_message(date, first_name, last_name, text, file_size)
        file_details = chatbot.get_file_details(file_id)
        # Check photo's file size is not more than 20MB
        if check_photo(file_details):
            file_path, file_name = get_photo_details(file_details)
            # token = chatbot.read_token_from_config_file("config.cfg")
            photo_url = f"https://api.telegram.org/file/bot{chatbot.token}/{file_path}"          
            download_status = download_photo(photo_url,file_name)
            chatbot.send_message(download_status, sender)
        else:
            chatbot.send_message("Unable to download, The file size is exceeding 20MB", sender)
    else:
        chatbot.display_incoming_message(date, first_name, last_name, text, file_size)
        reply = bot_response(text)
        chatbot.send_message(reply,sender)

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
                