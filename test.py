from service.scraping.pinterest import PinterestService

pin = PinterestService()
html = pin.link_parser("https://www.pinterest.fr/pin/61783826128938057/")

# image_div = html.select("div > img")
# src = image_div[4].get('src')

div = html.find('div', attrs={"data-test-id": "pin-closeup-image"})
# div = html.select("div")
print(div.img.get('src'))

# with open("div.html", "w", encoding="utf-8") as f:
#         f.write(str(div))