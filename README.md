# Telegram Chatbot

## Description
Telegram Chatbot is a bot that will wait for any incoming message and act accordingly to each type of message. It utilises Telegram Bot API to get the updates of the incoming message send by user through telegram user interface (telegram chat). 

User is interacting with the bot by sending a message via the bot chat window in Telegram's user interface. It is using getUpdates method from the API to get incoming message. The bot is doing long poling to keep waiting for the latest update by using the getUpdates method and set the offset parameter into {latest update_id + 1}

At the moment, It only supports text, photo file, and several bot command.
>>  
    - Text : Accept any text 
    - Photo File: Maximum file size is 20 MB and it will download the picture file and store it locally.
    - Bot Command available:
        /start : Welcome message to the sender
        /help: Listing out all command available with description


