from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")

    driver.switch_to.frame("iframeResult")

    button = driver.find_element(By.XPATH, "/html/body/button")
    button.click()

    time.sleep(2)

    alert = Alert(driver)
    alert.accept()

    print("Alerta fechado com sucesso!")

finally:
    driver.quit()
