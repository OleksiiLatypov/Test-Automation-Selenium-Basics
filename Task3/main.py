from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.relative_locator import locate_with

# Initialize WebDriver
driver = webdriver.Chrome()


def safe_find(description, locator_func):
    try:
        element = locator_func()
        print(f"{description}: ✅ Found")
        return element
    except Exception as e:
        print(f"{description}: ❌ Not Found ({str(e).splitlines()[0]})")
        return None


def get_locators(url):
    print(f"\n--- Checking locators on: {url} ---")
    driver.get(url)
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, "body")))

    # CLASS_NAME
    safe_find("CLASS_NAME 1 (demo_form)", lambda: driver.find_element(By.CLASS_NAME, "demo_form"))
    safe_find("CLASS_NAME 2 (first_name)", lambda: driver.find_element(By.CLASS_NAME, "first_name"))

    # ID
    safe_find("ID 1 (demo)", lambda: driver.find_element(By.ID, "demo"))
    safe_find("ID 2 (number)", lambda: driver.find_element(By.ID, "number"))

    # NAME
    safe_find("NAME 1 (whatsapp)", lambda: driver.find_element(By.NAME, "whatsapp"))
    safe_find("NAME 2 (business_name)", lambda: driver.find_element(By.NAME, "business_name"))

    # CSS_SELECTOR
    safe_find("CSS_SELECTOR 1 (input[name='first_name'])", lambda: driver.find_element(By.CSS_SELECTOR, "input[name='first_name']"))
    safe_find("CSS_SELECTOR 2 (input.first_name.form-control)", lambda: driver.find_element(By.CSS_SELECTOR, "input.first_name.form-control"))

    # XPATH
    safe_find("XPATH 1 //input[@name='first_name']", lambda: driver.find_element(By.XPATH, "//input[@name='first_name']"))
    safe_find("XPATH 2 //input[@class='first_name form-control']", lambda: driver.find_element(By.XPATH, "//input[@class='first_name form-control']"))

    # RELATIVE LOCATORS
    label = safe_find("RELATIVE helper (label for 'first_name')", lambda: driver.find_element(By.XPATH, "//label[@for='first_name']"))
    if label:
        safe_find("RELATIVE 1 (input below label)", lambda: driver.find_element(locate_with(By.TAG_NAME, "input").below(label)))

    right_input = safe_find("RELATIVE helper (last_name input)", lambda: driver.find_element(By.NAME, "last_name"))
    if right_input:
        safe_find("RELATIVE 2 (input to left of last_name)", lambda: driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(right_input)))


# List of URLs to test
urls = [
    "https://phptravels.com/demo/",
    "https://phptravels.org/register.php",
    "https://phptravels.com/blog/"
]

# Run locator checks
for url in urls:
    get_locators(url)

driver.quit()
