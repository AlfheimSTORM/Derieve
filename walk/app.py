# add code fpr flask app object
from flask import Flask, render_template

app = Flask(__name__)

# dependencies
from bs4 import BeautifulSoup
import requests
import re




# set route for user navigation
@app.route('/')

def index():
    return render_template("index.html")




@app.route('/pinterest')

# define app function
def pinterest():
    # set up list
    pinterest = "Pinterest"
    youtube = 'Youtube'
    facebook = 'Facebook'
    twitter = 'Twitter'

    # get number
    number = 20

    # move through list
    search = pinterest
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = (soup.text)

    return render_template("pinterest.html", text = text)




@app.route('/youtube')

# define app function
def youtube():
    # set up list
    pinterest = "Pinterest"
    youtube = 'Youtube'
    facebook = 'Facebook'
    twitter = 'Twitter'

    # get number
    number = 20

    # move through list
    search = youtube
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = (soup.text)

    return render_template("youtube.html", text = text)



@app.route('/facebook')

# define app function
def facebook():
    # set up list
    pinterest = "Pinterest"
    youtube = 'Youtube'
    facebook = 'Facebook'
    twitter = 'Twitter'

    # get number
    number = 20

    # move through list
    search = facebook
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = (soup.text)

    return render_template("facebook.html", text = text)




@app.route('/twitter')

# define app function
def twitter():
    # set up list
    pinterest = "Pinterest"
    youtube = 'Youtube'
    facebook = 'Facebook'
    twitter = 'Twitter'

    # get number
    number = 20

    # move through list
    search = twitter
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = (soup.text)

    return render_template("twitter.html", text = text)