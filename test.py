import requests
image_url = "https://dr.savee-cdn.com/things/6/4/37398385f4d11399aa4bcd.webp"
img_data = requests.get(image_url).content
with open('downloaded_imgs/image_name.jpg', 'wb') as handler:
    handler.write(img_data)