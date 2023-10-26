import requests
from service.download.directory import Directory as dir

class Download: 
    def download_img(self, img_url, path, img_name, extension):
        img_url = img_url
        img_data = requests.get(img_url).content
        with open(f'{path}{img_name}.{extension}', 'wb') as handler:
            handler.write(img_data)

    def download_all_img(self, imgs: list[dict], keyword: str):
        index = 0
        for website in imgs:
            for image in website:
                img_url = image.img_link
                path = f"resources/download/img/{keyword}/"
                if not dir.directory_exists(path):
                    dir.create_directory(path)
                img_name = f"img{index}"
                extension = image.format
                
                self.download_img(img_url, path, img_name, extension)
                index += 1


