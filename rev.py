import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# http://suninjuly.github.io/registration2.html
link = r"https://suninjuly.github.io/registration1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element(By.XPATH, "//label[text()[contains(.,\"First name\")]]/following-sibling::input")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.XPATH, "//label[text()[contains(.,\"Last name\")]]/following-sibling::input")
    last_name.send_keys("Petrov")
    email = driver.find_element(By.XPATH, "//label[text()[contains(.,\"Email\")]]/following-sibling::input")
    email.send_keys("ipetrov@smolensk.ru")

    button_send = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_send.click()

    time.sleep(1)
    welcome_text = driver.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()
