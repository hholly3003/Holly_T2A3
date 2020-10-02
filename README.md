# Telegram Chatbot

## Help and Installation Guide
*System Requirement*: Ensure that **Python3** is installed all dependecies on your machine.
* Obtain the API Token
    - You will need to have a Telegram account. Open the application and search for @botfather
    - Create new bot by type in  **/newbot** and setup the bot name and username
    - You will see a new API token is generated
    - Open config.cfg file and replace [TOKEN_KEY] with the API token  
* Create virtual environment and activate
    ``` 
    python3 -m venv venv
    source venv/bin/activate
    ```
* Install Dependencies
    ``` 
    pip install -r requirements.txt
    ```
* Run
    ```
    python main.py
    ```
* Dependencies available on *requirements.txt*
    ```
    certifi==2020.6.20
    chardet==3.0.4
    idna==2.10
    mypy==0.782
    mypy-extensions==0.4.3
    requests==2.24.0
    typed-ast==1.4.1
    typing-extensions==3.7.4.3
    urllib3==1.25.10
    ```

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

**Control Flow Diagram**

## Project Implementation
** Trello Board

## Testing
The application is using [CI/CD pipeline](https://github.com/hholly3003/Holly_T2A3/actions) that run automated testing everytime pushing new code to the master branch and deploy it into an EC2 instance on AWS services.