from flask import Flask, render_template, request, send_file
import pytube
from yt_dlp import YoutubeDL

app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('downloader.html')
    else:
        return render_template('index.html')

@app.route('/list', methods=['GET', 'POST'])
def list():

    try:
        url = request.form['input-link']
    except:
        return render_template('index.html')

    if "playlist" in url:
        
        urls_deferred = pytube.Playlist(url).video_urls
        imglist = []
        urls = []
        for i in urls_deferred:
            urls.append(i)
            imglist.append(pytube.YouTube(i).thumbnail_url)

    else:

        urls = [url]
        video = pytube.YouTube(url)
        imglist = [video.thumbnail_url]

    
    return render_template("list.html",  link = urls, img = imglist)

@app.route('/download', methods=['GET', 'POST'])
def download():
    try:
        url = request.form['button']
    except:
        return render_template('index.html')
    title = ""
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        
        title = ydl.extract_info(url, download=False).get('title', None)
        
    
    ydl_opts = {'outtmpl': 'downloads/%s.mp4'%(title), 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file("downloads/"+title+".mp4", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    