import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from pageObject.LoginPage import Login

from pageObject.LoginPage import Login

class Test_002_DDT_Login:
    baseurl=ReadConfig.getApplicationURL()#WHICH WILL GET APPLICATION URL FROM INI FILE

    #path= "./ /TestData/LoginData.xlsx " #from xl file
    path="C:/xl/LoginData.xlsx"
    logger =LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):  #setup will decide browser
        self.logger.info("********** Starting Test_002_DDT_Login Test *********") #id of test case
        self.logger.info(("*************Verifying login DDT test***********"))
        #self.driver=webdriver.Chrome()
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        #we have to access methods from LoginPage.py for that we need to create object for class Login
        self.lp=Login(self.driver) #when we call class login constructor will automatically invoke ,
                                   # constructor is expecting driver as parameter
        #IMPORT EXCEL UTIL
        #get rows
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in Excel:",self.rows)
        lst_status=[]  #Empty list variable to update list status result

        #depends upon number of rows we need to repeat loop
        for r in range(2,self.rows+1):
            #get data from xlutils
            #get/read username from xl
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            #read password
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            #read expected value to compare
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            #passing username from xl to application(testcase)

            self.lp.setUserName(self.user)
            self.lp.setPasswordName(self.password)
            #click on login button
            self.lp.Login()
            time.sleep(5)

            #validation 2 validations one is expected result(xl) and title

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=="Pass": #XL status
                    self.logger.info("*** Passed ***")
                    self.lp.Logout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.Logout()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")


            #if list contains all pass test case will pass

        if "Fail" not in lst_status:
                self.logger.info(("**** Login DDT Test passed ***"))
                self.driver.close()
                assert True
        else:
                self.logger.info("**** Login DDT Test failed ***")
                self.driver.close()
                assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("******** Completed TC_LoginDDT *******")









