from bs4 import BeautifulSoup
import requests

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EB%A7%A4%EB%AC%BC"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

lists = soup.find_all("tr", attrs={"data-tradetype":"SLR_A1"})
for i in range(0,5):
    trade = lists[i].find("td").get_text()
    locate = lists[i].find("td", attrs={"class":"fs_v2"}).get_text()
    title = lists[i].find("a")["title"]
    if "헬리오시티" in title:
        title = title[6:]
    area = lists[i].find_all("td", attrs={"class":"fs"})[0].get_text()
    price = lists[i].find_all("td", attrs={"class":"fs"})[1].get_text()
    layer = lists[i].find_all("td", attrs={"class":"fs"})[2].get_text()

    print("="*10 + f" 매물{i+1} " + "="*10)
    print(f"거래 : {trade}")
    print(f"소재지 : {locate}")
    print(f"면적 : {area} (공급/전용)")
    print(f"가격 : {price} (만원)")
    print(f"동 : {title}")
    print(f"층 : {layer}")