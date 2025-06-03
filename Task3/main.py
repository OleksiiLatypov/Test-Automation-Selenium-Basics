from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.relative_locator import locate_with

# Initialize WebDriver
driver = webdriver.Chrome()

def get_locators(url):
    driver.get(url)
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, "body")))  # Ensure page loads

    print(f"\nChecking locators on: {url}")

    try:
        # --- Locate by CLASS_NAME ---
        class_locator1 = driver.find_element(By.CLASS_NAME, "demo_form")
        print("CLASS_NAME 1:", class_locator1)
        
        class_locator2 = driver.find_element(By.CLASS_NAME, "first_name")
        print("CLASS_NAME 2:", class_locator2)

        # --- Locate by ID ---
        id_locator1 = driver.find_element(By.ID, "demo")
        print("ID 1:", id_locator1)

        id_locator2 = driver.find_element(By.ID, "number")
        print("ID 2:", id_locator2)

        # --- Locate by NAME ---
        name_locator1 = driver.find_element(By.NAME, "whatsapp")
        print("NAME 1:", name_locator1)

        name_locator2 = driver.find_element(By.NAME, "business_name")
        print("NAME 2:", name_locator2)

        # --- Locate by CSS_SELECTOR ---
        css_locator1 = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
        print("CSS_SELECTOR 1:", css_locator1)

        css_locator2 = driver.find_element(By.CSS_SELECTOR, "input.first_name.form-control")
        print("CSS_SELECTOR 2:", css_locator2)

        # --- Locate by XPATH ---
        xpath_locator1 = driver.find_element(By.XPATH, "//input[@name='first_name']")
        print("XPATH 1:", xpath_locator1)

        xpath_locator2 = driver.find_element(By.XPATH, "//input[@class='first_name form-control']")
        print("XPATH 2:", xpath_locator2)

        # --- Relative Locators ---
        label_first_name = driver.find_element(By.XPATH, "//label[@for='first_name']")
        relative_locator1 = driver.find_element(locate_with(By.TAG_NAME, "input").below(label_first_name))
        print("RELATIVE 1:", relative_locator1)

        last_name_input = driver.find_element(By.NAME, "last_name")
        relative_locator2 = driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(last_name_input))
        print("RELATIVE 2:", relative_locator2)

    except Exception as e:
        print(f"Error locating elements: {e}")

# Execute for multiple URLs
urls = [
    "https://phptravels.com/demo/",
    "https://phptravels.org/register.php",
    "https://phptravels.com/blog/"
]

for url in urls:
    get_locators(url)

driver.quit()
