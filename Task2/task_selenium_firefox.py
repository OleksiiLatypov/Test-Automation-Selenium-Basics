from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException


def get_title_chrome(url: str) -> str:
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(5)  # Wait max 5 seconds
        driver.get(url)
        get_title = driver.title
        return f"Google Chrome Browser:\n {get_title}"
    except TimeoutException:
        return 'Error: Page load timed out'
    except WebDriverException as e:
        return f'WebDriver error: {e}'
    except Exception as e:
        return f"Element not found or error occurred:, {e}"
    finally:
        if driver:
            driver.quit()


def get_title_firefox(url: str) -> str:
    driver = None
    try:
        # Set up Firefox options
        options = FirefoxOptions()

        # Specify firefox geckodriver PATH
        service = Service("geckodriver")

        # Launch the driver
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_page_load_timeout(5)
        driver.get(url)

        get_title = driver.title
        return f"Firefox Browser:\n {get_title}"
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
    google_chrome = get_title_chrome(url=BASE_URL)
    firefox = get_title_firefox(url=BASE_URL)
    print(google_chrome)
    print(firefox)
