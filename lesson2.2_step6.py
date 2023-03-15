from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x=x_element.text
    y = calc(x)
    answer_textbox = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_textbox.send_keys(y)
    check_box_element=browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_box_element.click()
    radio_element=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)
    radio_element.click()
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()