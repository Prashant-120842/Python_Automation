from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\prashant_malusare\\PycharmProjects\\nopcommerceApp\\Drivers\\chromedriver.exe")
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")

    else:
        driver = webdriver.Ie("C:\\Users\\prashant_malusare\\PycharmProjects\\nopcommerceApp\\Drivers\\chromedriver.exe")

    return driver

   # driver = webdriver.Chrome("C:\\Users\\prashant_malusare\\PycharmProjects\\nopcommerceApp\\Drivers\\chromedriver.exe")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#############Pytest HTML report ################

# it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'pavan'

#it is hook for delete/modify environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
