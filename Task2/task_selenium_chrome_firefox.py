from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException


def get_title(url: str, browser: str) -> str:
    driver = None
    try:
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            options = FirefoxOptions()
            # Specify firefox geckodriver PATH
            service = Service("geckodriver")
            # Launch the driver
            driver = webdriver.Firefox(service=service, options=options)
        else:
            return 'Error: Unknown browser'

        driver.set_page_load_timeout(10)
        driver.get(url)
        site_title = driver.title
        return f'{browser} browser: {site_title}'
    except TimeoutException:
        return 'Error: Page load timed out'
    except WebDriverException as e:
        return f'WebDriver error: {e}'
    except Exception as e:
        return f"Element not found or error occurred:, {e}"
    finally:
        if driver:
            driver.quit()


if __name__ == '__main__':
    BASE_URL = 'https://google.com'
    google_chrome = get_title(BASE_URL, 'chrome')
    firefox = get_title(BASE_URL, 'firefox')
    print(google_chrome)
    print(firefox)

# command to run
# python task_selenium_chrome_firefox.py
