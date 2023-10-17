from flask import Flask, request, jsonify
from service.search.search import SearchService

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    # print(req_args)
    research = SearchService()
    all_img = list()

    all_img.append(research.pinterest(keyword))
    # all_img.append(research.arena(keyword))
    # all_img.append(research.savee(keyword))
    
    return all_img

if __name__ == '__main__':
    


    app.run()

