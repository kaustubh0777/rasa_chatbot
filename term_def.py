from bs4 import BeautifulSoup
import requests

url = "https://www.investopedia.com/terms/a/acidtest.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

s = soup.find('p', id = "mntl-sc-block_1-0-1", class_ = "comp mntl-sc-block finance-sc-block-html mntl-sc-block-html")

#print(s.prettify())


for line in s:
    print(line)