import requests
import os
from typing import Tuple


def check_photo(file_details: dict) -> bool:
    """checking the size of the photo file is not exceeds 20MB

    :param file_details: [dictionary of file details
                          that contain the file size]
    :type file_details: dict
    :return: [return True when the file size is less or equal to 20MB]
    :rtype: bool
    """
    if file_details.get("file_size") <= 20000000:
        return True
    return False


def get_photo_details(file_details: dict) -> Tuple[str, str]:
    """Getting the file path from file details.
    Set the file name using part of file_path details

    :param file_details: [Dictionary containing all file attributes]
    :type file_details: dict
    :return: [Tuple containing two strings: file_path, file_name]
    :rtype: Tuple[str, str]
    """
    file_path = file_details.get("file_path", "")
    file_name = file_path.split("/")[1]
    return file_path, file_name


def download_photo(url, file_name: str) -> str:
    """Download the file using HTTP request and save the photo
    with file_name provided

    :param url: [uri for the get request]
    :type url: [str]
    :param file_name: [save the photo into file_name]
    :type file_name: [str]
    :return: [Message of the download status]
    :rtype: str
    """
    photo = requests.get(url)
    if photo.status_code == 200:
        if os.path.isdir("photos"):
            try:
                if not os.path.isfile(f"photos/{file_name}"):
                    with open(f"photos/{file_name}", "wb") as image:
                        image.write(photo.content)
                    return "File is downloaded successfully"
                else:
                    return "File is already existed in the photos folder"
            except Exception as error:
                return error
        else:
            return """Download Fail - folder photos is not exist.
                    Please create one"""
