from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Set Implicit Wait (Applies globally)
driver.implicitly_wait(5)

# Open Google
driver.get("https://www.google.com")

# Accept Cookies (if required)
try:
    accept_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
    )
    accept_cookies.click()
except:
    pass  # Continue if no cookie popup appears

# Locate Search Box (Explicit Wait)
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Wait for Search Results to Load
first_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h3"))
)
first_result.click()

# --- Screenshot ---
driver.save_screenshot("selenium_search_result.png")
print("Screenshot saved: selenium_search_result.png")

# Close the browser
driver.quit()
