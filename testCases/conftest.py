import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome("C://BrowserWindows//chromedriver.exe")
        print("Launching chrome browser")
    elif browser == "edge":
         driver=webdriver.Edge ("C://BrowserWindows//msedgedriver.exe")
         print("Launching opera browser")

    return driver #driver is returning

def pytest_addoption(parser):   #this will get value  from command line
    parser.addoption("--browser")
@pytest.fixture()
def browser(request): #this will return browser value to setup
    return request.config.getoption("--browser")

##########  Pytest HTML Report #################

#It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']= 'nop commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']= 'Geetha'
#
# #It is hook for delete/Modify Environment info to HTML Report(modify default HTML report)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
