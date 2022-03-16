import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers)
# res.raise_for_status() #문제 발생시 즉시 종료
with open("mygoogle.html", 'w', encoding="utf-8") as f:
    f.write(res.text)