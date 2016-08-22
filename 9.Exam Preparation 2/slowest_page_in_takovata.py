"""
You're given an access log from the webpage Takovata and you need to check which page has had the slowest average
response time.

Each log in the .log file is in this format in one line:
dt="2016-02-06T13:38:45+00:00" ip="95.43.31.127" m="GET" p="http" url="/student/lecture/568015bf131b1642faa73799/"
 req_b="494" ref="http://python3.softuni.bg/student/course/" ua="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
  code="200" resp_t="0.032" resp_b="9300"

Note: some urls have GET requests which need to be removed
urls that end with /ws/ should not be counter
"""
import urllib.parse
import re
file_path = input()
url_resp_times = {}  # type: dict

with open(file_path, encoding='utf-8') as reader:
    for line in reader:
        reg = re.search('url="(?P<url>.*?)".*?resp_t="(?P<resp>.*?)"', line)
        url = reg.group("url")
        url = urllib.parse.urlparse(url).path

        if url.endswith("/ws/"):
            continue

        resp_t = float(reg.group("resp"))

        if url not in url_resp_times.keys():
            url_resp_times[url] = []

        url_resp_times[url].append(resp_t)

highest_average, url = max([(sum(lst)/float(len(lst)), url) for url, lst in url_resp_times.items()])

print(url)
print(round(highest_average, 3))

# 100/100