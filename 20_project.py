import requests, re
from bs4 import BeautifulSoup
from requests.api import head

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

def today_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%B2%AD%EC%A3%BC+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    weather = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
    l_t = soup.find("span", attrs={"class":"min"})
    low_temp = l_t.find("span", attrs={"class":"num"}).get_text()
    h_t = soup.find("span", attrs={"class":"max"})
    high_temp = h_t.find("span", attrs={"class":"num"}).get_text()
    m_rain = soup.find("span", attrs={"class":"point_time morning"})
    a_rain = soup.find("span", attrs={"class":"point_time afternoon"})
    mor_rain = m_rain.find("span", attrs={"class":"num"}).get_text()
    nig_rain = a_rain.find("span", attrs={"class":"num"}).get_text()
    dust = soup.find("dl", attrs={"class":"indicator"})
    find_dust = dust.find_all("dd")[0].get_text()
    micro_dust = dust.find_all("dd")[1].get_text()


    print("[오늘의 날씨]")
    print(f"{weather}")
    print(f"현재 {temp}℃ (최저 {low_temp}℃ / 최고 {high_temp}℃")
    print(f"오전 강수확률 {mor_rain}% / 오후 강수확률 {nig_rain}%")
    print("\n")
    print(f"미세먼지 {find_dust}")
    print(f"초미세먼지 {micro_dust}")

def headline_news():
    url = "https://news.naver.com/"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    print("\n[헤드라인 뉴스]")

    soup = BeautifulSoup(res.text, "lxml")
    newsss = soup.find("ul", attrs={"class":"hdline_article_list"})
    newss = newsss.find_all("div", attrs={"class":"hdline_article_tit"})


    for i in range(0,5):
        news = newss[i].get_text()
        link = "https://news.naver.com/" + newss[i].find("a")['href']
        print(f"{i+1}. {news.strip()} \n(링크 : {link})")

def it_news():
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    print("\n[IT 뉴스]")

    soup = BeautifulSoup(res.text, "lxml")
    newsss = soup.find("ul", attrs={"class":"type06_headline"})
    newss = newsss.find_all("li")


    for i in range(0,3):
        news = newss[i].find_all("dt")[1].get_text()
        link = newss[i].find("a")['href']
        print(f"{i+1}. {news.strip()} \n(링크 : {link})")

def eng():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    print("\n[오늘의 영어 회화]")

    soup = BeautifulSoup(res.text, "lxml")

    find_class = soup.find_all("div", attrs={"class":"conv_txtBox"})
    eng_exams = find_class[1].find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    kor_exams = find_class[0].find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("(영어 지문)")
    for eng_exam in eng_exams:
        print(f"{eng_exam.get_text().strip()}")
    print("\n(한글 지문)")
    for kor_exam in kor_exams:
        print(f"{kor_exam.get_text().strip()}")

if __name__ == "__main__":
    today_weather()
    headline_news()
    it_news()
    eng()
