from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException
import time

# === Setup driver ===
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

# === Utility function ===
def try_find(driver, strategy, by, locator):
    try:
        element = driver.find_element(by, locator)
        print(f"✅ {strategy}: {locator}")
    except NoSuchElementException:
        pass

# === Page 1: Demo ===
def check_demo_page(driver):
    print("\n🔍 Checking https://phptravels.com/demo/")
    driver.get("https://phptravels.com/demo/")
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, "body")))

    try_find(driver, "ID", By.ID, "number")
    try_find(driver, "ID", By.ID, "demo")

    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "demo_form")
    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "first_name")

    try_find(driver, "NAME", By.NAME, "business_name")
    try_find(driver, "NAME", By.NAME, "whatsapp")

    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "input[name='first_name']")
    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "input.form-control.whatsapp")

    try_find(driver, "XPATH", By.XPATH, "//input[@name='first_name']")
    try_find(driver, "XPATH", By.XPATH, "//input[@id='number']")

    try:
        base = driver.find_element(By.ID, "number")
        rel = driver.find_element(locate_with(By.TAG_NAME, "input").above(base))
        print(f"✅ RELATIVE: Input above #number → Tag name: {rel.tag_name}")
    except:
        pass

# === Page 2: Register ===
def check_register_page(driver):
    print("\n🔍 Checking https://phptravels.org/register.php")
    driver.get("https://phptravels.org/register.php")
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, "body")))

    try_find(driver, "ID", By.ID, "inputFirstName")
    try_find(driver, "ID", By.ID, "inputEmail")

    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "form-control")
    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "form-group")

    try_find(driver, "NAME", By.NAME, "firstname")
    try_find(driver, "NAME", By.NAME, "email")

    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "input[name='lastname']")
    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "input#inputEmail")

    try_find(driver, "XPATH", By.XPATH, "//input[@name='email']")
    try_find(driver, "XPATH", By.XPATH, "//input[@id='inputFirstName']")

    try:
        base = driver.find_element(By.ID, "inputLastName")
        rel = driver.find_element(locate_with(By.TAG_NAME, "input").above(base))
        print(f"✅ RELATIVE: Input above #inputLastName → Tag name: {rel.tag_name}")
    except:
        pass

# === Page 3: Blog ===
def check_blog_page(driver):
    print("\n🔍 Checking https://phptravels.com/blog/")
    driver.get("https://phptravels.com/blog/")
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, "body")))

    try_find(driver, "ID", By.ID, "popular-posts")
    try_find(driver, "ID", By.ID, "post-3050")

    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "post-title")
    try_find(driver, "CLASS_NAME", By.CLASS_NAME, "image-wrapper")

    try_find(driver, "NAME", By.NAME, "s")  # Search box, if present
    try_find(driver, "NAME", By.NAME, "post_type")

    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "div.blog-page")
    try_find(driver, "CSS_SELECTOR", By.CSS_SELECTOR, "#footer")

    try_find(driver, "XPATH", By.XPATH, "//div[@class='blog-page']")
    try_find(driver, "XPATH", By.XPATH, "//footer[@id='footer']")

    try:
        base = driver.find_element(By.ID, "footer")
        rel = driver.find_element(locate_with(By.TAG_NAME, "div").above(base))
        print(f"✅ RELATIVE: Div above #footer → Tag name: {rel.tag_name}")
    except:
        pass

# === Main run ===
if __name__ == "__main__":
    driver = setup_driver()
    try:
        # check_demo_page(driver)
        # check_register_page(driver)
        check_blog_page(driver)
    finally:
        driver.quit()
