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
    
    research = SearchService()
    all_img = research.search(keyword)
    
    treatment_time = datetime.datetime.now() - start_time
    nb_links = len(all_img[0]) + len(all_img[1]) + len(all_img[2])
    print(f"Temps : {treatment_time}, Nombre : {nb_links}")
    
    return all_img

if __name__ == '__main__':
    app.run()

