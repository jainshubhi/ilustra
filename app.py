import os, requests
from flask import Flask, request, render_template, redirect, url_for

################################### CONFIG #####################################
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

GENIUS_API_URL = 'http://api.genius.com/'

################################### ROUTES #####################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    song = request.args.get('song')
    headers = {'Authorization': 'Bearer ' + os.environ['GENIUS_CLIENT_ACCESS'],
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.get(GENIUS_API_URL + 'search', params={'q':song.replace('+', ' ')},
        headers=headers).json()
    print(r.keys())
    return render_template('search_result.html', results=r['response']['hits'])

@app.route('/play')
def play():
    pass

if __name__ == '__main__':
    app.run()
