from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\jhm10\Desktop\pg\파이썬\webscraping_basic\chromedriver")
# 네이버 접속
browser.get("https://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 아이디 비밀번호 입력
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
browser.implicitly_wait(time_to_wait=3)

# 아이디를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 브라우저 종료