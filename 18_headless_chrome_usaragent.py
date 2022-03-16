from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

browser = webdriver.Chrome(r"C:\Users\jhm10\Desktop\pg\파이썬\webscraping_basic\chromedriver.exe", options=options)
browser.maximize_window()