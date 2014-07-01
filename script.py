from bs4 import BeautifulSoup
import urllib

url = raw_input()
pageFile = urllib.urlopen(url)
pageHtml = pageFile.read()
pageFile.close()

soup = BeautifulSoup((pageHtml))

for code in soup.find_all('pre'):
    if code.get('class'):
        print code.get_text()
