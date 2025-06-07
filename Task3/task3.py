from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException


"""
Task 3.
Using the attached list of screenshots and links to websites provide a list of the locators for elements in the red area. For each type of locator below prepare 2 examples. 2 locators by id, 2 locators by class name, etc. Be sure that your locator is leading to an exact single element, not a group of them.
You can provide different locators for the same element, like 1 locator by ID and 1 by name for a button element. But the maximum number of locators for the same element mustn’t be more than 2.
1. class name 
Example: find_element(By.CLASS_NAME, "information")
2. id
Example: find_element(By.ID, "lname")
3. name
Example: find_element(By.NAME, "newsletter")
4. CSS selector
 Example: find_element(By.CSS_SELECTOR, "#fname")
5. XPath
Example: find_element(By.XPATH, "//input[@value='f']")
6*. Relative locators
Example: locate_with(By.TAG_NAME, "input").above({By.ID: "password"})

"""

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


def check_page(driver, url, locators):
    print(f"\nChecking {url}")
    driver.get(url)
    WebDriverWait(driver, 5).until(presence_of_element_located((By.TAG_NAME, 'body')))
    for by, value in locators:
        try:
            driver.find_element(by, value)
            print(f'Found: {by} = {value}')
        except NoSuchElementException:
            print(f'Not found: {by} = {value}')



pages = {
    "https://phptravels.com/demo/": [
        (By.ID, "number"), (By.ID, "demo"), (By.CLASS_NAME, "demo_form"), (By.CLASS_NAME, "first_name"),
        (By.NAME, "business_name"), (By.NAME, "whatsapp"), (By.CSS_SELECTOR, "input[name='first_name']"),
        (By.CSS_SELECTOR, "input[name='whatsapp']"), (By.XPATH, "//input[@name='first_name']"),
        (By.XPATH, "//input[@id='number']")
    ],
    "https://phptravels.org/register.php": [
        (By.ID, "inputFirstName"), (By.ID, "inputEmail"),(By.CLASS_NAME, "form-control"),
        (By.CLASS_NAME, "form-group"), (By.NAME, "firstname"), (By.NAME, "email"),
        (By.CSS_SELECTOR, "input[name='lastname']"), (By.CSS_SELECTOR, "input#inputEmail"),
        (By.XPATH, "//input[@name='email']"), (By.XPATH, "//input[@id='inputFirstName']")
    ],
    "https://phptravels.com/blog/": [
        (By.ID, "popular-posts"), (By.ID, "post-3050"),(By.CLASS_NAME, "post-title"),
        (By.CLASS_NAME, "image-wrapper"), (By.NAME, "s"), (By.NAME, "viewport"),
        (By.CSS_SELECTOR, "#popular-posts"), (By.CSS_SELECTOR, ".image-wrapper"),
        (By.XPATH, "//*[@id='post-3050']"), (By.XPATH, "//*[@class='post-title']")
    ]
}

if __name__ == "__main__":
    driver = setup_driver()
    for url, locators in pages.items():
        check_page(driver, url, locators)

