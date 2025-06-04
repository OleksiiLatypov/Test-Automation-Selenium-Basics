import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def setup_chrome_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(10)
    return driver


def perform_google_search(search_site: str, search_word: str):
    driver = setup_chrome_driver()
    try:
        driver.get(search_site)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(search_word)
        time.sleep(3)
        search_box.send_keys(Keys.RETURN)

        # wait for result and click first link
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "h3"))
        )
        print(f"clicking on: {first_result.text}")
        first_result.click()
        driver.save_screenshot("selenium_result_chrome.png")
        print("Screenshot with the execution results saved as 'selenium_result_chrome.png'")
        time.sleep(3)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()


if __name__ == "__main__":
    perform_google_search("https://www.google.com", "Selenium")
