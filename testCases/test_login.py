import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from pageObject.LoginPage import Login

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getuseremail() #from ini file
    Password=ReadConfig.getpasword()#from ini file

    logger =LogGen.loggen()


    @pytest.mark.sanity
    def test_homepagetitle(self,setup):

       self.logger.info("******************Test_001_Login**************")   #testcase id
       self.logger.info("******************Verifying Home Page Title")
       #self.driver=webdriver.Chrome()
       self.driver=setup #whatever driver is returning it is stored here
       #using driver launch application
       self.driver.get(self.baseurl )
       act_title=self.driver.title
       time.sleep(4)


       if act_title == "Your store. Login":
           assert True
           self.driver.close()
           self.logger.info("*********Home page title is passed************")

       else:

           self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
           self.driver.close()
           self.logger.error("**********Home page title is failed*******")
           assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_log(self,setup):

        self.logger.info(("*************Verifying login test***********"))
        #self.driver=webdriver.Chrome()
        self.driver=setup
        self.driver.get(self.baseurl)
        #we have to access methods from LoginPage.py for that we need to create object for class Login
        self.lp=Login(self.driver) #when we call class login constructor will automatically invoke ,
                                   # constructor is expecting driver as parameter
        self.lp.setUserName(self.username)
        self.lp.setPasswordName(self.Password)
        time.sleep(2)
        self.lp.Login()
        act_title = self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********Login test case passed**********")



        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testlogin.png")
            self.driver.close()
            self.logger.info("*********Login test case passed**********")
            assert False


