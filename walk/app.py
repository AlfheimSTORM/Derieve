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




@app.route('/gallery')

# define app function
def gallery():
    # set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'

    # get number
    number = 20

    # move through list
    search = gallery
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

    return render_template("index.html", text = text)




@app.route('/uic')

# define app function
def UIC():
    # set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'

    # get number
    number = 20

    # move through list
    search = UIC
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

    return render_template("uic.html", text = text)



@app.route('/usa')

# define app function
def usa():
    # set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'

    # get number
    number = 20

    # move through list
    search = usa
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

    return render_template("usa.html", text = text)




@app.route('/chicago')

# define app function
def chicago():
    # set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'

    # get number
    number = 20

    # move through list
    search = chicago
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

    return render_template("chicago.html", text = text)