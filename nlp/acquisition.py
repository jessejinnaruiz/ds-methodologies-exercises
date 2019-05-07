#!/usr/bin/env python
# coding: utf-8

from requests import get
import requests
from bs4 import BeautifulSoup
import os
import json
from pprint import pprint
import re

import itertools as it
from typing import List, Dict
import pandas as pd


url = 'https://codeup.com/why-san-antonio-has-more-than-tacos-to-offer/'
headers = {'User-Agent': 'Codeup Ada Data Science'} # codeup.com doesn't like our default user-agent
response = get(url, headers=headers)

# print(response.text[:400])


soup = BeautifulSoup(response.content, 'html.parser')


article = soup.find('div', class_='mk-single-content')
# article.text


def get_article_text(url):
    # if we already have the data, read it locally
#     if path.exists('article.txt'):
#         with open('article.txt') as f:
#             return f.read()

    # otherwise go fetch the data
#     url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent': 'Codeup Ada Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='mk-single-content')

    # save it for next time
#     with open('article.txt', 'w') as f:
#         f.write(article.text)

    return article.text.strip()



# get_article_text('https://codeup.com/everyday-encounters-with-data-science/')

def get_article_titles(url):
    return re.search(r'.*?([\w-]+)/$', url)[1]


# get_article_titles('https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/')


# # Exercises

# #### Codeup Blog Articles
# 
# Scrape the article text from the following pages:
# 
# * https://codeup.com/codeups-data-science-career-accelerator-is-here/
# * https://codeup.com/data-science-myths/
# * https://codeup.com/data-science-vs-data-analytics-whats-the-difference/
# * https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/
# * https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/
# 
# Encapsulate your work in a function named get_blog_articles that will return a list of dictionaries, with each dictionary representing one article. The shape of each dictionary should look like this:


urls = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
'https://codeup.com/data-science-myths/',
'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']


def get_blog_articles():
    text = []
    titles = []
    for url in urls:
        text.append(get_article_text(url))
        titles.append(get_article_titles(url))
    articles = zip(titles, text, urls) 
    articles_dicts = [dict(zip(('title','contents', 'url'), article)) for article in articles]
    return articles_dicts



articles = get_blog_articles()
# articles


pd.DataFrame(articles)


def get_blog_articles_save(use_cache=True):
    if use_cache and os.path.exists('codeup_blog_articles.json'):
        articles = json.load(open('codeup_blog_articles.json'))
    else:
        articles = get_blog_articles()
        json.dump(articles, open('codeup_blog_articles.json', 'w'))
    return articles

# get_blog_articles_save()

# pd.DataFrame(get_blog_articles_save())





# ### News Articles
# 
# We will now be scraping text data from inshorts, a website that provides a brief overview of many different topics.
# 
# Write a function that scrapes the news articles for the following topics:
# 
# business
# sports
# technology
# entertainment
# The end product of this should be a function named get_news_articles that returns a list of dictionaries, where each dictionary has this shape:

headers = {'User-Agent': 'Codeup Ada Data Science'}
response = get('https://inshorts.com/en/read/business', headers=headers)
soup = BeautifulSoup(response.text)
news = soup.find('div', class_='news-card-content')

content = news.text


# content


base_url = 'https://inshorts.com/en/read'
sections = ['business', 'sports', 'technology', 'entertainment']


def get_article(url):

    content = url.find(class_='news-card-content').find('div', attrs={'itemprop': 'articleBody'}).text.strip()
    
    title = url.find(class_='news-card-title').find('a').text.strip()
     
#     articles_dicts = [dict(zip(('title','contents'), article)) for article in articles]

    return {
        'title': title,
        'content': content
    }


# collects articles in a given section
def get_section(section):
    url = f'{base_url}/{section}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    articles = [get_article(article) for article in soup.find_all(class_='news-card')]
    for article in articles:
        article['category'] = section
    return articles



# get_section('business')


def get_all_sections() -> List[Dict[str, str]]:
    sections2 = [get_section(section) for section in sections]
    # flatten out the nested lists with it.chain
    return list(it.chain(*sections2))


# get_all_sections()


def get_news_articles(use_cache=True) -> List[Dict[str, str]]:
    if use_cache and os.path.exists('news_articles.json'):
        articles = json.load(open('news_articles.json'))
    else:
        articles = get_all_sections()
        json.dump(articles, open('news_articles.json', 'w'))
    return articles


# get_news_articles()