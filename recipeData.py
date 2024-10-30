import requests
from bs4 import BeautifulSoup

url = 'https://recipe.rakuten.co.jp/category/'  # 替换为你的URL

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 提取分类名称和URL
categories = soup.find_all('li', class_='list_3row__item refine_recipe__item')

category_list = []

for category in categories:
    name = category.find('span', class_='list_3row__text').text.strip()
    link = category.find('a')['href']
    category_list.append({'name': name, 'url': link})

# 打印结果
for item in category_list:
    print(f'分类名称: {item["name"]}')
    print(f'URL: {item["url"]}')