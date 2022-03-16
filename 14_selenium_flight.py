from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r"C:\Users\jhm10\Desktop\pg\파이썬\webscraping_basic\chromedriver")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_element_by_link_text("27")[0].click()
# browser.find_element_by_link_text("28")[0].click()

# 다음달 27일, 28일 선택
browser.find_element_by_xpath('//*[@id="l_8"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[5]/td[3]/a').click()
browser.find_element_by_xpath('//*[@id="l_8"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[5]/td[4]/a').click()

# 이번달 27일, 다음달 28일 선택
# browser.find_element_by_link_text("27")[0].click()
# browser.find_element_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
time.sleep(1)
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text) # 성공했을 때 결과 출력
finally:
    browser.quit()

# 첫 번째 결과 출력
# elem = browser.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')


