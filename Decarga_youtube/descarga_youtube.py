from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        path = request.form.get('path')
        filename = request.form.get('filename')
        format = request.form.get('format')

        yt = YouTube(url)

        if not filename:
            filename = yt.title

        # Descargando el video en formato mp4
        if format == 'video':
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            stream.download(output_path=path, filename=filename)
            filename += '.mp4'
        # Descargando el audio en formato mp3
        elif format == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=path, filename=filename)
            # Renombrando la extensión del archivo a .mp3
            base, ext = os.path.splitext(os.path.join(path, filename))
            new_file = base + '.mp3'
            os.rename(os.path.join(path, filename)+ext, new_file)
            filename += '.mp3'

        return render_template('success.html', filename=filename)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
