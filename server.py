import bot

# bot replying to the message 
def bot_response(message):
    if message is not None:
        reply = f"Bot : {message}"
    return reply

update_id = None
while True:
    print("Bot is running ...")
    # Instantiate the telegramchatbot
    chatbot = bot.TelegramChatbot("config.cfg")
    # Check for any update or input given to the bots
    updates = chatbot.get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            sender = item["message"]["from"]["id"]
            reply = bot_response(message)
            chatbot.send_message(reply, sender)