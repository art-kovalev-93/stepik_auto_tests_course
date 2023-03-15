from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    answer_textbox = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    answer_textbox.send_keys(y)
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robotCheckbox.click()
    robotRules = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robotRules.click()
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()