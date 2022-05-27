from selenium.webdriver.common.by import By


class SearchCustomer():
    txtEmail_id= "SearchEmail"
    txtFirstname_id="SearchFirstName"
    txtLastname_id="SearchLastName"
    btnSearch_id="search-customers"
    table_xpath="//div[@id='customers-grid_wrapper']"
    tableRows_xpath="//table[@id='customers-grid']//tr"
    tableCols_xpath="//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self, driver):  # driver from testcase
         self.driver = driver  # initiating to class variable

    def setEmail(self,email):
        self.driver.find_element(By.ID ,self.txtEmail_id ).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,self.txtFirstname_id).clear()
        self.driver.find_element(By.ID,self.txtFirstname_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.ID,self.txtLastname_id).clear()
        self.driver.find_element(By.ID,self.txtLastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id ).click()

    def getNoOfRows(self):
        return len(self.driver.find_element(By.XPATH,self.tableRows_xpath ))

    def getNoOfCols(self):
        return len(self.driver.find_element(By.XPATH,self.tableCols_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH("//table[@id='customers-grid']//tr["+str(r)+"]"))
            if emailid==email:
                flag=True
                break
        return flag