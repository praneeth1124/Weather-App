
from requests_html import HTMLSession

s = HTMLSession()

query = ''
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'})


print(r.html.find('span#wob_tm', first=True).text)