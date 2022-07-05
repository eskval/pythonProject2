import send as send
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browdriver\chromedriver.exe")

driver.get("https://moychay.ru/")
driver.implicitly_wait(5)
driver.maximize_window()

element = driver.find_element(By.XPATH, "//input[@id='keyword']")
element.send_keys("пуэр" + Keys.RETURN)
driver.quit()











