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
        news =  feedparser.parse("https://evrimagaci.org/rss.xml")
        x=0
        keys=news.entries[1]
        # print(keys.keys())
        # print(keys.media_content[0]["url"])
        # print()
        # for keys in news.entries:
        for keys in news.entries:
            r = requests.get("https://evrimagaci.org/kanser-cerrahisinin-gelisim-seruveni-radikal-yontemler-basarili-cozumleri-nasil-dogurdu-11055")
            source = BeautifulSoup(r.content, "html.parser")
            informations = source.find_all("div", attrs={"class": "mb-10 content clearfix"})
            y = 0
            for information in informations:
                # print(information)
                # information=information.find_all("p")
                for info in information:
                    print(info.get_text())
                #print(information.get_text())

                print("--------------------------------------------------------")

            #     info +=information.get_text()+"\n"
            # print(info)
            info=""


@app.route("/")
def hello():
    return info


if __name__ == "__main__":
    image=str()
    info=str()
    threading.Thread(target=main,).start()
    # app.run()
