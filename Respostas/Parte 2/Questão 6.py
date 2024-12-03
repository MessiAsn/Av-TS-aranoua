from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("Python Selenium")
    search_bar.send_keys(Keys.RETURN)
    
    time.sleep(2)

    driver.save_screenshot("resultado.png")
    print("A captura de tela foi salva como 'resultado.png'.")

finally:
    driver.quit()
