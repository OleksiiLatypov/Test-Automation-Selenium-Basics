from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get("https://phptravels.com/demo/")
check = driver.title
print(check)

time.sleep(2)

# FIX: Use CSS_SELECTOR for multiple classes
# form = driver.find_element(By.CSS_SELECTOR, ".demo_form.bgb.br8.p3.h-100")
# names = driver.find_element(By.NAME, "first_name")
#
# form_by_class = driver.find_element(By.CLASS_NAME, "demo_form")
# header_by_class = driver.find_element(By.CLASS_NAME, "first_name")
# #print("Form found:", form_by_class)
# print(header_by_class)
#
#
# # ID
# button_by_id = driver.find_element(By.ID, "demo")
# enter_number_id = driver.find_element(By.ID, "number")
# print(enter_number_id)
#
# whatsapp_by_name = driver.find_element(By.NAME, "whatsapp")
# business_by_name = driver.find_element(By.NAME, "business_name")
#
# print(f'WHATSAPP: {whatsapp_by_name}')


first_name_css1 = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
print("CSS_SELECTOR 1:", first_name_css1)

first_name_css2 = driver.find_element(By.CSS_SELECTOR, "input.first_name.form-control")
print("CSS_SELECTOR 2:", first_name_css2)


# --- 5. Locate by XPATH ---
first_name_xpath1 = driver.find_element(By.XPATH, "//input[@name='first_name']")
print("XPATH 1:", first_name_xpath1)

first_name_xpath2 = driver.find_element(By.XPATH, "//input[@class='first_name form-control']")
print("XPATH 2:", first_name_xpath2)

# --- 6. Relative locators ---
label_first_name = driver.find_element(By.XPATH, "//label[@for='first_name']")


first_name_relative1 = driver.find_element(locate_with(By.TAG_NAME, "input").below(label_first_name))
print("RELATIVE 1:", first_name_relative1)

# Locate using position relative to last name
last_name_input = driver.find_element(By.NAME, "last_name")
first_name_relative2 = driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(last_name_input))
print("RELATIVE 2:", first_name_relative2)



driver.quit()
