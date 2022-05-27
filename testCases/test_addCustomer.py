import string
import time

import pytest
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.LoginPage import  Login
from pageObject.AddCustomerPage import AddCustomer
import random



class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getuseremail()
    password=ReadConfig.getpasword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************Test_003_AddCustomer ***********")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=Login(self.driver) #obj for LoginPage pageobj

        self.lp.setUserName(self.username)
        self.lp.setPasswordName(self.password)
        self.lp.Login()

        self.logger.info("********** Login successful********")

        self.logger.info("************* Starting Add customer Test ****************")

        self.addcust=AddCustomer(self.driver)  #obj for AddcustomerPage pageobj

        time.sleep(3)
        self.addcust.clickOnCustomersmenu()
        time.sleep(3)
        self.addcust.clickOncustomersMenuItem()
        self.addcust.clickonAddnew()

        self.logger.info("********* Providing customer info ********************")

        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)

        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Nirjith")
        self.addcust.setLastName("Bal")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/06/1985")
        self.addcust.setCompanyname("ABC")
        self.addcust.setIsTax()
        self.addcust.setNewsLetter("Test store 2")
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing....")
        self.addcust.clickOnSave()

        self.logger.info("************ Saving customer info *************")

        self.logger.info(("************* Adding customer validation started ********"))

        self.msg=self.driver.find_element(By.TAG_NAME,'Body').text
        print(self.msg)


        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.error("********** Add customer Test Failed ***********")
            assert False
        self.driver.close()
        self.logger.info("************* Ending Add customer test ***********")



def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))