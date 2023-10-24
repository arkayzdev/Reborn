import os

class Directory:
    def directory_exists(path: str):
        if os.path.exists(path):
            return True
        return False 

    def create_directory(path: str):
        os.makedirs(path)