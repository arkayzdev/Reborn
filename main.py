from flask import Flask, request, jsonify, render_template
from service.search.search import SearchService
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search', methods=['GET'])
def search():
    start_time = datetime.datetime.now()
    keyword = request.args.get('keyword')
    # print(req_args)
    research = SearchService()
    all_img = list()

    all_img.append(research.pinterest(keyword))
    all_img.append(research.arena(keyword))
    all_img.append(research.savee(keyword))
    
    time = datetime.datetime.now() - start_time
    print(f"Temps : {time}, Nombre : {len(all_img[0]) + len(all_img[1]) + len(all_img[2])}")
    return all_img

if __name__ == '__main__':
    app.run()

