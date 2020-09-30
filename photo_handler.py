import requests
import os


# check file if it is a photo
def check_photo(file_details):
    print("Checking photo")
    if file_details.get("file_size") <= 20000000:
        return True
    return False

def get_photo_details(file_details):
    file_path = file_details.get("file_path", "")
    file_name = file_path.split("/")[1]
    return file_path, file_name

def download_photo(url, file_name):
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
            return "Download Fail - folder photos is not exist. Please create one"