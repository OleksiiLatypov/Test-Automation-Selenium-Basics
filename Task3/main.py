from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://phptravels.com/demo/")
check = driver.title
print(check)

time.sleep(2)

# FIX: Use CSS_SELECTOR for multiple classes
# form = driver.find_element(By.CSS_SELECTOR, ".demo_form.bgb.br8.p3.h-100")
# names = driver.find_element(By.NAME, "first_name")

form_by_class = driver.find_element(By.CLASS_NAME, "demo_form")
header_by_class = driver.find_element(By.CLASS_NAME, "text-center")
print("Form found:", form_by_class)
print(header_by_class)

driver.quit()
