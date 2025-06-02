# conftest.py
import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def specific_date():
    return "2024-08-15"  # Replace with the actual date you need to verify


@pytest.fixture(scope="function")
def gcp_bucket_name():
    return "your-gcp-bucket-name"  # Replace with your actual GCP bucket name


@pytest.fixture(scope="function")
def aws_staging_bucket_name():
    return "your-aws-staging-bucket-name"  # Replace with your actual AWS staging bucket name
