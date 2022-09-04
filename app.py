from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])




def index():

 url = "https://www.businesstoday.in/technology"
 req=requests.get(url)
 soup=BeautifulSoup(req.content,"html.parser")
 datatobeshown=soup.find_all("div",class_="widget-listing",limit=6)
 displaynews=""
 for data in datatobeshown:
     corpnews=data.div.div.a["title"]
     displaynews+='\u2022 '+ corpnews+'\n'
 return render_template("index.html",News=displaynews)