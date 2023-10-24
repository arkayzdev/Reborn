from flask import Flask, request, render_template
from service.search.search import SearchService
from service.download.download import Download
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
    all_img = research.search_all(keyword)
    
    treatment_time = datetime.datetime.now() - start_time
    nb_links = len(all_img[0]) + len(all_img[1]) + len(all_img[2])
    print(f"Temps : {treatment_time}, Nombre : {nb_links}")
    
    return all_img


@app.route('/search/<website>', methods=['GET'])
def searchOne(website):
    req_args = request.view_args
    website = req_args['website']
    start_time = datetime.datetime.now()
    keyword = request.args.get('keyword')
    
    research = SearchService()
    all_img = research.search_one(keyword, website)
    
    treatment_time = datetime.datetime.now() - start_time
    nb_links = len(all_img[0])
    print(f"Temps : {treatment_time}, Nombre : {nb_links}")
    
    return all_img


@app.route('/download', methods=['GET'])
def download():
    start_time = datetime.datetime.now()
    keyword = request.args.get('keyword')
    
    research = SearchService()
    all_img = research.search_all(keyword)
    Download.download_all_img(all_img, keyword)


    treatment_time = datetime.datetime.now() - start_time
    nb_links = len(all_img[0]) + len(all_img[1]) + len(all_img[2])
    print(f"Temps : {treatment_time}, Nombre : {nb_links}")
    
    return all_img
    
if __name__ == '__main__':
    app.run()

