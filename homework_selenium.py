from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('.\chromedriver.chromedriver.exe')

url = 'https://www.spacex.com/launches/'
driver.get(url)
sleep(5)

req = driver.page_source

driver.quit()

soup = BeautifulSoup(req, 'html.parser')

launches = soup.select('.item')
# print(launches)
for launch in launches:
    date = launch.select_one('.date').text.strip()
    
    label = launch.select_one('.label').text.strip()
    
    print(date, ' | ', label)