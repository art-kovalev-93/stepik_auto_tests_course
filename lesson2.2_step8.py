from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    name_element = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name_element.send_keys("Artem")
    last_name_element = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name_element.send_keys("Kovalev")
    email_element = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_element.send_keys("test@test.sru")
    add_file=browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'short_bio.txt')  # добавляем к этому пути имя файла
    add_file.send_keys(file_path)
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()