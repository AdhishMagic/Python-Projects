import requests
from bs4 import BeautifulSoup

search = 'weather in New York'
url = f'https://www.google.com/search?q={search}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
weather_info = soup.find('div', class_='BNeawe')

if weather_info:
    print(weather_info.text)
else:
    print("Weather information not found. Google may have changed its page structure or blocked the request.")