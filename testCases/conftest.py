from selenium import webdriver
import pytest

# To Run Test Cases at default browser
# pytest -v -s testCases/test_login.py

# To Run Test Cases at certain Browser
# pytest -v -s testCases/test_login.py --browser chrome
# pytest -v -s testCases/test_login.py --browser firefox

# To Run Test Cases at certain Browser in parallel
# pytest -v -s -n=3 testCases/test_login.py --browser chrome
# pytest -v -s -n=3 testCases/test_login.py --browser firefox

# To Run Test Cases with Pytest HTML Report Generation
# pytest -v --html=Reports\report.html testCases/test_login.py --browser chrome
# pytest -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

# To Run Data Driven Cases Pytest HTML Report Generation
# pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser chrome


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/Administrator/PycharmProjects/nopcommerceApp/chromedriver_win32/chromedriver.exe")
        print("Launching Chrome browser......")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/Administrator/PycharmProjects/nopcommerceApp/geckodriver-v0.29.1-win64/geckodriver.exe")
        print("Launching Firefox browser......")
    else:
        driver = webdriver.Edge(executable_path="C:/Users/Administrator/PycharmProjects/nopcommerceApp/edgedriver_win64/msedgedriver")
        # driver = webdriver.Edge(executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver")
        print("Launching Edge browser......")
    return driver

def pytest_addoption(parser): #this will get value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")

############ Pytest HTML Report #########################
# It is a hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['QA Automation Engineer'] = 'Vadim Klimets'

# It is a hook for delete/Modify Environment Info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

