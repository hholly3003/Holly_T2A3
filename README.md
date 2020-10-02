# Telegram Chatbot

## Help and Installation Guide
*System Requirement*: Ensure that Python3 is installed on your machine.

Once the application file is downloaded to your computer, Navigate to directory of the main.py file that should be available under *src* folder.

## Description
Telegram Chatbot is a bot that is used as our personal assistance to save our file to the server or specified remote location just by sending it via the bot. As initial development, it is only implemented to support photo file. There is file size limitation for the API to download it, which is 20MB.

**How It Works**
The bot will wait for any incoming message from user and act accordingly to each type of message. It utilises Telegram Bot API to get response and sending message using requests module. The response received from the API is a JSON file.

The user is interacting with the bot by using Telegram's user interface. It is a chat window that can be accessed by downloading the Telegram apps in mobile or via web browser.

At the moment, The bot only supports three types of messages:  text, photo file, and several bot command.

**Getting Incoming Message:**
User is interacting with the bot by sending a message via the bot chat window in Telegram's user interface. It is using getUpdates method from the API to get incoming message. The bot is doing long poling to keep waiting for the latest update by using the getUpdates method and set the offset parameter into {latest update_id + 1}

**Handling the Message Received and Sending Response**
The bot will act accordingly to each message received. This handle by **run_command** function in server.py
You can define more bot commands and handle other file type like documents inside this function.
These are all type of messages that is handled by the bot:
>>  
    - Text : Accept any text and the bot will send a confirmation for receiving the message.
    - Photo File: Maximum file size is 20 MB and it will download the picture file and store it locally under photos folder. If photos folder did not exist, it will not download the file.
    - Bot Command available:
        /start : Welcome message to the sender
        /help: Listing out all command available with description
The bot also able to send a response message back to the user by utilising the sendMessage method. 