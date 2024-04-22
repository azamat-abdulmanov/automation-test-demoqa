from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope="function")
def driver():
    chrom_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrom_service)
    yield driver
    driver.quit()