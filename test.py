from service.scraping.pinterest import PinterestService

pin = PinterestService()
info = pin.get_img_info("https://www.pinterest.fr/pin/591097519864154653/", ["None"], 0)
print(info)