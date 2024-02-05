import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://beej.us/guide/bgnet/html/split-wide/" #input("Enter Link: ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    href = link.get('href')
    absolute_url = urljoin(url, href) # 将相对路径转换为绝对路径
    links.append(absolute_url)


print(links)