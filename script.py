from bs4 import BeautifulSoup
import urllib

url = raw_input()
pageFile = urllib.urlopen(url)
pageHtml = pageFile.read()
pageFile.close()

soup = BeautifulSoup((pageHtml))

for code in soup.find_all('pre'):
    print(code.get_text())
    if code['class']:
        print code['class']
