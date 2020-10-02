import bot
from photo_handler import check_photo, get_photo_details, download_photo
import json


EXIT_MODE = False

chatbot = bot. TelegramChatbot("config.cfg")


def bot_response(message: str) -> str:
    """Bot response when received text message from user

    :param message: [the message send by user]
    :type message: str
    :return: [Confirmation that bot received the message]
    :rtype: str
    """
    reply = None
    if message is not None:
        reply = f"I have received your message : '{message}'"
    return reply


def check_updates(update_id: int) -> int:
    """Check the type of messages received from user.
    It can be a text, photo, bot command, or unknown type.

    :param update_id: [the unique identifier for each
    message received from user]
    :type update_id: int
    :return: [the update id for long polling purposes]
    :rtype: int
    """
    response = chatbot.get_updates(offset=update_id)
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


def run_command(chat_id: int, first_name: str, last_name: str,
                text: str, file_id: str,
                update_id: int, file_size: int, date) -> None:
    """It is the action that bot will take accordingly to the messages
    received

    :param chat_id: [used to identify the recipient of bot response]
    :type chat_id: int
    :param first_name: [name of the sender]
    :type first_name: str
    :param last_name: [name of the sender]
    :type last_name: str
    :param text: [text message received from sender]
    :type text: str
    :param file_id: [a unique file identifier]
    :type file_id: str
    :param update_id: [unique update / message identifier]
    :type update_id: int
    :param file_size: [the size of the phot received in bytes ]
    :type file_size: int
    :param date: [date the message received ]
    :type date: [int]
    """
    global EXIT_MODE
    if text == "/help":
        chatbot.send_message(f"No help today. Sorry, {first_name}", chat_id)

    elif text == '/start':
        chatbot.send_message(f"Hello {first_name}! " +
                             "Just send me a text or picture file",
                             chat_id)

    elif text == '/exit':
        chatbot.send_message("Terminating the bot", chat_id)
        EXIT_MODE = True

    elif file_id:
        chatbot.display_incoming_message(date, first_name, last_name,
                                         text, file_size)
        file_details = chatbot.get_file_details(file_id)

        # Check photo's file size is not more than 20MB
        if check_photo(file_details):
            file_path, file_name = get_photo_details(file_details)
            url = "https://api.telegram.org/file/bot"
            photo_url = f"{url}{chatbot.token}/{file_path}"
            download_status = download_photo(photo_url, file_name)
            chatbot.send_message(download_status, chat_id)
        else:
            error = "Unable to download, file size is exceeding 20MB"
            chatbot.send_message(error, chat_id)
    else:
        chatbot.display_incoming_message(date, first_name,
                                         last_name, text, file_size)
        reply = bot_response(text)
        chatbot.send_message(reply, chat_id)
