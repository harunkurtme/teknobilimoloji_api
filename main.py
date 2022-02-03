import requests
from bs4 import BeautifulSoup
import feedparser
import time
import threading
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

def main():
    while True:

        global info, image
        news =  feedparser.parse("https://www.bilim.org/feed/")
        x=0
        keys=news.entries[1]
        for keys in news.entries:
            r = requests.get(str(keys.link))
            source = BeautifulSoup(r.content, "lxml")
            informations = source.find_all("section", attrs={"class": "article__content entry-content js-post-gallery"})
            images = source.find_all("div", attrs={"class": "article__featured-image"})
            x+=1
            for information in informations:
                #print(information.get_text())

                info +=information.get_text()+"\n"

            for image in images:
                image=image.find("img").get("data-lazy-src")
            time.sleep(2)
            info = ""


@app.route("/")
def hello():
    return info


if __name__ == "__main__":
    image=str()
    info=str()
    threading.Thread(target=main,).start()
    app.run()
