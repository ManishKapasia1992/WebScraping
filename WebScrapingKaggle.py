# These are the basic libraries
import pandas as pd
import numpy as np
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
import os
import requests

# Importing libraries for Scraping
from twitterscraper import query_tweets
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from newspaper import Article
import scrapy
import praw

# Scrapping Twitter

# begin_date = dt.date(2020, 6, 15)
# end_date = dt.date(2020, 6, 16)

# limit = 100
# lang = 'english'

# def tweet(emp):
#     tweets = query_tweets(emp, begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
#     Df = pd.DataFrame(t.__dict__ for t in tweets)
#     print(Df.columns)
#     Texts = list(tweets.text)
#     for i in Texts :
#         print("  -----------------------------------------------------------------------------------------")
#         print(i)
#         print("  -----------------------------------------------------------------------------------------")

# tweet()

# Scraping Newspapers/Articles

# def scrap(url):
#     Client = urlopen(url)
#     xml_page = Client.read()
#     Client.close()
#     soup_page = BeautifulSoup(xml_page, 'xml')
#     news_list = soup_page.find_all('item')

    # print news title, url and publish date
    # for news in news_list:
    #     news_list = set()
    #     print(news.title.text), print(news.link.text), print(news.pubDate.text)

# scrap('http://news.google.com/news/rss')

# Scraping Newspapers/Articles

# A new article from TOI
# url = 'https://timesofindia.indiatimes.com/'

# TOI_Article = Article(url, language='en')

# import nltk
# nltk.download('punkt')

# To download the article
# TOI_Article.download()

# To parse the article
# TOI_Article.parse()

# To perform natural language processing ie..nlp
# TOI_Article.nlp()

# print("Article's Title:")
# print(TOI_Article.title)
# print('n')

# print("Article's Text:")
# print(TOI_Article.text)
# print('n')

# print("Article's Summary:")
# print(TOI_Article.summary)
# print('n')

# print("Article's Keywords")
# print(TOI_Article.keywords)

# Scraping Reddit

# def headline(company):
#     headlines = set()
    # reddit = praw.Reddit(client_id='F2uCF0oF0q46GA',
                         # client_secret='5Vo58uJsQLDfoswrzOflyWWfNdQ',
                         # user_agent='roshan220206')
    # for submission in reddit.subreddit('google').new(limit=None):
    #     headlines.add(submission.title)

#     print(headlines)
# headline('google')

# for submission in reddit.subreddit('python').hot(limit=5):
    # print(submission) # it will generate the thread ids
    # print(dir(submission))
    # print(submission.title)
    # if not submission.stickied:
        # print(submission.title)
        # print('Title: {}, ups: {}, downs: {}, have we visited: {}'.format(submission.title,
        #                                                                   submission.ups, submission.downs, submission.visited))

# We can also subscribe and unsubscribed

# subreddit = reddit.subreddit('pyhton')
# subreddit.subscribe() # it will throw an error if not logged in to the reddit website
# subreddit.unsubscribe()

# we can do either using function like
# def scrap(url):
#     Client = urlopen(url)
#     html_page = Client.read()
#     Client.close()
#     page_soup = BeautifulSoup(html_page, 'html.parser')
#     print(page_soup.h1)

# scrap('https://www.amazon.com/s?k=earphones+with+microphone&i=deals-intl-ship&crid=30JNNDE0ZE1NI&sprefix=earph%2Cdeals-intl-ship%2C626&ref=nb_sb_ss_fb_1_5')

# my_url = 'https://www.newegg.com/Video-Cards-Video-Dev/ices/Category/ID-38?Tpk=graphics%20card'
# u_Client = urlopen(my_url)
# html_page = u_Client.read()
# u_Client.close()
#
# soup_page = BeautifulSoup(html_page, 'html.parser')
# print(soup_page.h1)

# Exercises

# Load the webpage

# r = urlopen('https://keithgalli.github.io/web-scraping/example')
# page_html = r.read()
# r.close()
# soup = BeautifulSoup(page_html, 'html.parser')
#
# print(soup)

# r = requests.get('https://keithgalli.github.io/web-scraping/webpage.html')

# webpage = BeautifulSoup(r.content, 'html.parser')

# print(webpage.prettify())

# Task 1: To grab all of the social links from the webpage

# By using the select statement
# links = webpage.select('ul.socials a')
# actual_links = [link['href'] for link in links]
# print(actual_links)

# By using the find statement
# links = webpage.find('ul', attrs={'class': 'socials'})
# ulinks = webpage.find('ul', {'class': 'socials'})
# links = ulinks.findAll('a')
# actual_links = [link['href'] for link in links]
# print(actual_links)

# links = webpage.select('li.social a')
# actual_links = [link['href'] for link in links]
# print(actual_links)

# Scrap the table
import pandas as pd


# table = webpage.select('table.hockey-stats')[0]
# columns = table.find('thead').find_all('th')
# print(table)
# column_names = [c.string for c in columns]
# print(column_names)

# table_rows = table.find('tbody').find_all('tr')
# print(table_rows)

# l = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     # row = [str(tr.string).strip() for tr in td]
#     row = [str(tr.get_text()).strip() for tr in td]
#     l.append(row)

# print(l[1])

# df = pd.DataFrame(l, columns=column_names)
# df = df.loc[df['Team'] != 'Did not play']
# print(df.head())

# Grab all the fun facts that use word 'is'
# import re
# fun_facts = webpage.select('ul.fun-facts li')
# fun_facts = webpage.find('ul', attrs={'class': 'fun-facts'}).findAll('li')
# print(fun_facts)
# fun_facts_data = [f.text for f in fun_facts]
# print(fun_facts_data)
# is_data = [fact.find(text=re.compile('is')) for fact in fun_facts]
# is_data = [fact.find_parent().get_text() for fact in is_data if fact]
# is_data = [fact for fact in is_data if fact]
# print(is_data)

# Download the images
url = 'https://keithgalli.github.io/web-scraping/'

r = requests.get(url + 'webpage.html')

webpage = BeautifulSoup(r.content, 'html.parser')

# image = webpage.find('img')
# image = webpage.select('div.row div.column img')
# image = webpage.find('div', attrs={'class': 'row'}).findAll('img')
# print(image)
# image_url = image[0]['src']
# full_url = url + image_url
# print(image_url)

# img_data = requests.get(full_url).content
# with open(r'C:\Users\admin\Desktop\lake_como.jpg', 'wb') as handler:
#     handler.write(img_data)

# Solve the mystery challenge
files = webpage.select('div.block a')
# print(files)
relative_files = [f['href'] for f in files]
# print(relative_files)

url = 'https://keithgalli.github.io/web-scraping/'

for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    BeautifulSoup_page = BeautifulSoup(page.content, 'html.parser')
    # print(BeautifulSoup_page.body.prettify())
    secret_word_elements = BeautifulSoup_page.find('p', attrs={'id': 'secret-word'})
    secret_word = secret_word_elements.string
    print(secret_word)

# Extracting the iphone related data from flipkart website

my_url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=8c424152-b868-4e7b-a6c6-fe2e11016a44&as-searchtext=iph'

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, 'html.parser')

containers = page_soup.findAll("div", {'class': "_3O0U0u"})
# print(len(containers)) # This is the total no. of items on the site
# print(BeautifulSoup.prettify(containers[0]))
container = containers[0]
# print(container.div.img['alt'])

# price = container.findAll('div', {'class': "_1vC4OE _2rQ-NK"})
# print(price[0].text)

# ratings = container.findAll('div', {'class': "hGSR34"})
# print(ratings[0].text)

# Now lets create a file to extract this data
filename = 'C:\\Users\\admin\\Desktop\\Iphone_Products.csv'
f = open(filename, 'w')

headers = 'Product_Name.Pricing.Ratings\n'
f.write(headers)

for container in containers:
    product_name = container.div.img['alt']

    price_container = container.findAll('div', {'class': "_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    ratings_container = container.findAll('div', {'class': "hGSR34"})
    rating = ratings_container[0].text

    # print('product_name:' + product_name)
    # print('price:' + price)
    # print('rating:' + rating)

    # String Parsing
    price = ''.join(price.replace('₹', 'Rs'))
    # price = price.replace('₹', 'Rs')

    # print('price:' + price)

    print(product_name.replace(',', '|') + ',' + price.replace(',', '') + ',' + rating + '\n')
    f.write(product_name.replace(',', '|') + ',' + price.replace(',', '') + ',' + rating + '\n')

f.close()

# containers = soup.find_all('div', attrs={'class': '_3O0U0u'})
# container = soup.findAll('div', attrs={'class': 'bhgxx2 col-12-12'})
# print(containers)
# print(len(container))
# print(len(containers))
# print(bs.prettify(containers[0]))
# print(containers[0].prettify())
# container = containers[0]
# name = container.find('div', attrs={'class': '_3wU53n'})
# print(name.text)
# ratings = container.find('div', attrs={'class': 'niH0FQ'})
# print(ratings.string)
# price = container.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
# print(price.text)
# print(container.div.img['alt'])

# ratings = container.find('div', attrs={'class': 'niH0FQ'})
# ratings = container.find('div', attrs={'class': 'hGSR34'})
# print(ratings.text)

# names = [container.find('div', attrs={'class': '_3wU53n'}).text for container in containers]
# prices = [container.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).text for container in containers]
# ratings = [container.find('div', attrs={'class': 'hGSR34'}).text for container in containers]
#
# new_prices = [p.replace('₹', 'Rs') for p in prices]
# df = pd.DataFrame({'Name': names, 'Price': new_prices, 'Rating': ratings})
# print(df)
#
# iphone_data = df.to_csv(r'C:\Users\admin\Desktop\Iphone_data.csv')
