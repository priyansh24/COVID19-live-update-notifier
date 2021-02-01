
# # Desktop Notifier for COVID-19
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/",
    headers = header)
html = urlopen(req)
obj = bs(html)
new_cases = obj.find("li", {"class": "news_li"}).strong.text.split()[0]
death = list(obj.find("li", {"class": "news_li"}).
    strong.next_siblings)[1].text.split()[0]

notifier = ToastNotifier()
message  = "New Cases - "+ new_cases+"\nDeath - "+death
notifier.show_toast(title="COVID-19 Update", msg=message,
                    duration=20, icon_path="virus.ico")

