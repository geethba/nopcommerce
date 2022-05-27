import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    #Add customer page
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath='//a[@href="/Admin/Customer/List"]//p'
    btnAddnew_xpath='//a[@class="btn btn-primary"]'
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_id='Gender_Male'
    rdFemaleGender_id='Gender_Female'
    txtDob_id="DateOfBirth"
    txtCompanyName_id="Company"
    chkIsTax_id="IsTaxExempt"

    txtnews_xpath="//body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    txtNewsLetter_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds']"
    txtnews_firstvalue_xpath=" // select[ @ id = 'SelectedNewsletterSubscriptionStoreIds'] // option[ @ value = '1']"
    txtnews_secondvalue_xpath = " // select[ @ id = 'SelectedNewsletterSubscriptionStoreIds'] // option[ @ value = '2']"
    # lstNews_yourstore_xpath="//option[contains(text(),'Your store name')]"
    # lstNew_Teststore_xpath="//option[contains(text(),'Test store 2')]"
    txtCustomerRoles_xpath='//div[@role="listbox"][1]'
    lstItemAdministrators_xpath= "//select[@id='SelectedCustomerRoleIds']//option[1]"
    lstItemForumModerater_xpath="//select[@id='SelectedCustomerRoleIds']//option[2]"
    listItemGuest_xpath="//select[@id='SelectedCustomerRoleIds']//option[3]"
    listItemRegistered_xpath="//select[@id='SelectedCustomerRoleIds']//option[4]"
    listItemVendors_xpath="//select[@id='SelectedCustomerRoleIds']//option[5]"
    drpmgrofvendor_id="VendorId"

    txtAdmincomment_xpath="//*[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self, driver):  # driver from testcase
        self.driver = driver

    def clickOnCustomersmenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOncustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath ).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath ).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id ).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id ).click()

    def setDob(self,dob):
        self.driver.find_element(By.ID,self.txtDob_id).send_keys(dob)

    def setCompanyname(self,comname):
        self.driver.find_element(By.ID,self.txtCompanyName_id ).send_keys(comname)


    def setIsTax(self):
        self.driver.find_element(By.ID,self.chkIsTax_id).click()

    def setNewsLetter(self,news):
        self.driver.find_element(By.XPATH,self.txtnews_xpath).click()
        if news == 'Your store name':
            itemnews=self.driver.find_element(By.XPATH, self.txtnews_firstvalue_xpath)
        else:
            itemnews = self.driver.find_element(By.XPATH, self.txtnews_secondvalue_xpath)
        print(itemnews)

        self .driver.execute_script("arguments[0].click();", itemnews)





    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstItemAdministrators_xpath )
        elif role =="Forum Moderators":
           self.listitem=self.driver.find_element(By.XPATH,self.lstItemForumModerater_xpath )
        elif role == "Guest":
            time.sleep(3)
            #self.driver.find_element(By.XPATH("//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[2])")).click()
            self.driver.find_element(By.XPATH("//span[@title='delete']")).click()
            self.listitem=self.driver.find_element(By.XPATH,self.listItemGuest_xpath)
        elif role=="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.listItemRegistered_xpath )
        elif role=="Vendors":
            self.listitem =self.driver.find_element(By.XPATH,self.listItemVendors_xpath )
        else:
            self.listitem= self.driver.find_element(By.XPATH,self.listItemVendors_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.ID,self.drpmgrofvendor_id))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdmincomment_xpath ).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath ).click()




