import unittest
from photo_handler import check_photo, get_photo_details

class TestPhotoHandlerFunctions(unittest.TestCase):
    def test_check_photo(self):
        file_details = {"file_size" : 20000000}
        
        result = check_photo(file_details)
        self.assertTrue(result, msg = "The file size is too big.")
    
    def test_get_photo_details(self):
        file_details = {
            "file_path" : "photos/file_10.jpg",
            "file_size" : 1000000 }
        file_path, file_name = get_photo_details(file_details)

        self.assertTrue(isinstance(file_path, str), msg = "File path is not found")
        self.assertTrue(isinstance(file_name, str), msg = "File name is not set")
        