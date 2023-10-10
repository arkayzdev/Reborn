from flask import Flask
from service.scraping.are_na import AreNaService as arena
from service.scraping.pinterest import PinterestService as pin
from service.scraping.savee_it import SaveeItService as savee

app = Flask(__name__)

@app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/search/<search>', methods=['GET'])
def search(search: str):


if __name__ == '__main__':
    app.run()

