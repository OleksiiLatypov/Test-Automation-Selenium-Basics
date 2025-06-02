import allure
import time
import pytest
from selenium.webdriver.common.by import By


@allure.title('Test GCP bucket and AWS staging')
def test_gcp_aws_not_empty(driver, specific_date, gcp_bucket_name, aws_staging_bucket_name):

    gcp_url = f'https://storage.cloud.google.com/{gcp_bucket_name}/{specific_date}'
    aws_url = f'http://s3.amazonaws.com/{aws_staging_bucket_name}/{specific_date}'

    with allure.step(f'Chek GCP bucket {gcp_bucket_name} for {specific_date}'):
        try:
            driver.get(gcp_url)
            time.sleep(2)
            gcp_bucket_links = driver.find_elements(By.TAG_NAME, value='a')
            assert len(gcp_bucket_links) > 0, f"GCP bucket '{gcp_bucket_name}' \
            is empty for {specific_date}"
        except Exception as e:
            pytest.fail(f"Failed to verify AWS bucket: {str(e)}")

    with allure.step(f"Check AWS bucket: {aws_url}"):
        try:
            driver.get(aws_url)
            time.sleep(2)
            aws_links = driver.find_elements(By.TAG_NAME, value="a")
            assert len(aws_links) > 0, f"AWS bucket '{aws_staging_bucket_name}'\
             is empty for {specific_date}"
        except Exception as e:
            pytest.fail(f"Failed to verify GCP bucket: {str(e)}")





