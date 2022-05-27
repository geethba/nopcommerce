from selenium.webdriver.common.by import By


class Login:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_logout_linktext="Logout"

#element actions
    #initalize driver, for that constructor (constructor invokes at the time of object creation)
    def __init__(self,driver): #driver from testcase
        self.driver=driver  #initiating to class variable

        #using driver create action methods
    def setUserName(self,username): #username from testcase
        self.driver.find_element(By.ID ,self.textbox_username_id).clear()
        self.driver.find_element (By.ID,self.textbox_username_id).send_keys(username)

    def setPasswordName(self,password):
        self.driver.find_element (By.ID,self.textbox_password_id ).clear()
        self.driver.find_element (By.ID,self.textbox_password_id ).send_keys(password)

    def Login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element(By.LINK_TEXT ,self.link_logout_linktext).click()