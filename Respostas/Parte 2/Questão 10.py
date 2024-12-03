from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    success_message = driver.find_element(By.ID, "flash")
    if "You logged into a secure area!" in success_message.text:
        print("Login bem-sucedido!")
    else:
        print("Falha no login!")

finally:
    driver.quit()
