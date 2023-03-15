from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    chess_picture = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x=chess_picture.get_attribute("valuex")
    y = calc(x)
    answer_textbox = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_textbox.send_keys(y)
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robotCheckbox.click()
    robotRules = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotRules.click()
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()