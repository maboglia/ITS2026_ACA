from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://search.yahoo.com/")

splashscreen = driver.find_element(By.NAME, "agree")
splashscreen.click()
cerca = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[3]/div[2]/div[1]/form/div[1]/input')
form = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[3]/div[2]/div[1]/form')

cerca.send_keys("Is python still dangerous?")
form.submit()




input("Press ENTER to exit\n")
