import bot
from photo_handler import check_photo, get_photo_details, download_photo
import os
import json


EXIT_MODE = False

chatbot = bot. TelegramChatbot("config.cfg")

# bot replying to the message 
def bot_response(message: str) -> str:
    reply = None
    if message is not None:
        reply = f"I have stored message : '{message}' into log file"
    return reply

def check_updates(update_id : int) -> int:
    response =  chatbot.get_updates(offset = update_id)
    data = json.loads(response.content)
    parameters_list = chatbot.get_content(data)

    if EXIT_MODE:
        return 1
    if not parameters_list:
        return 0
    for parameter in parameters_list:
        update_id = parameter[5]
        run_command(*parameter)
        return update_id

def run_command(chat_id : int, first_name: str, last_name: str, text: str, file_id : str,
 update_id: int, file_size: int, date) -> None:
    global EXIT_MODE
    if text == "/help":
        chatbot.send_message(f"No help today. Sorry, {first_name}", chat_id)
        
    elif text == '/start':
        chatbot.send_message(f"Hello {first_name}! Just send me a text or picture file", chat_id)
        
    elif text == '/exit':
        chatbot.send_message("Terminating the bot", chat_id)
        EXIT_MODE = True

    elif file_id:
        chatbot.display_incoming_message(date, first_name, last_name, text, file_size)
        file_details = chatbot.get_file_details(file_id)
        # Check photo's file size is not more than 20MB
        if check_photo(file_details):
            file_path, file_name = get_photo_details(file_details)
            photo_url = f"https://api.telegram.org/file/bot{chatbot.token}/{file_path}"          
            download_status = download_photo(photo_url,file_name)
            chatbot.send_message(download_status, chat_id)
        else:
            chatbot.send_message("Unable to download, The file size is exceeding 20MB", chat_id)
    else:
        chatbot.display_incoming_message(date, first_name, last_name, text, file_size)
        reply = bot_response(text)
        chatbot.send_message(reply,chat_id)