import bs4 as BeautifulSoup
import requests
import re
import selenium
import selenium.webdriver as webdriver

url = 'http://instagram.com/_maxcalvert/'
driver = webdriver.Chrome()
driver.get(url)

