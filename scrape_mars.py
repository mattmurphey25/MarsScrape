
# coding: utf-8

# In[231]:


from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time


# In[232]:
def init_browser():
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():

    browser = init_browser()

    mars_data = {}

    # In[233]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[234]:


    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    

    # In[253]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # In[236]:


    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')



    # In[239]:


    html = browser.html
    soup = bs(html, 'html.parser')

    figure = soup.find('figure', class_='lede')
    image_url = figure.find('a')['href']
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url
    mars_data['featured_image_url'] = featured_image_url

    # In[240]:


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)


    # In[241]:


    html = browser.html
    soup = bs(html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_data['mars_weather'] = mars_weather

    # In[242]:


    url = 'http://space-facts.com/mars/'

    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['description', 'value']
    df = df.iloc[1:]
    df.set_index('description', inplace=True)


    # In[243]:


    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    mars_data['html_table'] = html_table

    # In[244]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[245]:


    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    html = browser.html
    soup = bs(html, 'html.parser')

    cerberus_title = soup.find('h2', class_='title').text
    figure = soup.find('img', class_='wide-image')['src']
    cerberus_url = 'https://astrogeology.usgs.gov' + figure


    # In[246]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[247]:


    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html = browser.html
    soup = bs(html, 'html.parser')

    schiaparelli_title = soup.find('h2', class_='title').text
    figure = soup.find('img', class_='wide-image')['src']
    schiaparelli_url = 'https://astrogeology.usgs.gov' + figure


    # In[248]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[249]:


    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    html = browser.html
    soup = bs(html, 'html.parser')

    syrtis_title = soup.find('h2', class_='title').text
    figure = soup.find('img', class_='wide-image')['src']
    syrtis_url = 'https://astrogeology.usgs.gov' + figure


    # In[250]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[251]:


    html = browser.html
    soup = bs(html, 'html.parser')

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html = browser.html
    soup = bs(html, 'html.parser')

    valles_title = soup.find('h2', class_='title').text
    figure = soup.find('img', class_='wide-image')['src']
    valles_url = 'https://astrogeology.usgs.gov' + figure


    # In[252]:


    hemisphere_image_urls = [
        {"title": valles_title, "img_url": valles_url},
        {"title": cerberus_title, "img_url": cerberus_url},
        {"title": schiaparelli_title, "img_url": schiaparelli_url},
        {"title": syrtis_title, "img_url": syrtis_url},
    ]


    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_data