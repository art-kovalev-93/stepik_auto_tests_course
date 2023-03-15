from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_num=browser.find_element(By.CSS_SELECTOR, "#input_value")
    x=x_num.text
    y=calc(x)
    text_box=browser.find_element(By.CSS_SELECTOR, "#answer")
    text_box.send_keys(y)
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()