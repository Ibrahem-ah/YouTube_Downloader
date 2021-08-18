from random import randint
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    send_file,
    send_from_directory,
)
import youtube_dl
import os
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST", "GET"])
def download():
    if request.method == "POST":
        url = request.form["URL"]
        filename = downloadURL(url)
        print("\n\n", filename, "\n\n")

        try:
            return send_from_directory(
                "./videos", f"{filename}.webm", as_attachment=True
            )
        except:
            return send_from_directory(
                "./videos", f"{filename}.mkv", as_attachment=True
            )

    return render_template("test.html")


def downloadURL(url):
    rannum = randint(0, 100000)
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "moplaylist": True,
        "outtmpl": f"./videos/{rannum}",
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print("Could not download the video in course: {}".format(url))
    return rannum

if __name__ == "__main__":
    app.run(debug=True)
