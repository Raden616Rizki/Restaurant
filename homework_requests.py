import requests
from bs4 import BeautifulSoup

url = 'https://www.spacex.com/launches/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

launches = soup.find_all('div', {
    'class': ['item'],
})

for launch in launches:
    date = launch.select_one('.date').text.strip()
    
    label = launch.select_one('.label').text.strip()

    print(date, ' -> ', label)