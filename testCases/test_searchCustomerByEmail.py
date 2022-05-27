import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.LoginPage import Login
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer

class Test_SearchCustomerByEmail_004:
    baseURL= ReadConfig.getApplicationURL()
    useremail=ReadConfig.getuseremail()
    password=ReadConfig.getpasword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_search_CustomerByEmail(self,setup):
        self.logger.info("************** SearchCustomerByEmail_004 *******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPasswordName(self.password)
        self.lp.Login()
        self.logger.info("********** Login successful")

        self.logger.info("********* Starting search customer by Email *********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersmenu()
        self.addcust.clickOncustomersMenuItem()

        self.logger.info("************ searching customer by emailID *********")
        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(4)
        self.driver.close()
        #assert True==status
        self.logger.info("************ TC_SearchCustomerByEmail_004 Finished *********")








