import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage1
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"  # you can use line 12 to 14 over this line from 7 to 9
    # username = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getApplicationURL()
    # path = ".\\TestData\\LoginData.xlsx"
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("***Test _002_DDT_Login***")
        self.logger.info("*********** Verifying login ddt test *************")

        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage1(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number od rows in Excel:", self.rows)

        lst_status=[]  # empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)  # r=rows, 1 = columns
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.driver.maximize_window()  # For maximizing window
            self.driver.implicitly_wait(20)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("**Failed**")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif actual_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**Failed***")
                    lst_status.append("Fail")

                elif self.exp == 'Fail':
                    self.logger.info("**Passed**")
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
            self.logger.info("** Login DDT test passed **")
            self.driver.close()
            assert True

        else:
            self.logger.info("** Login DDT test failed **")
            self.driver.close()
            assert False


        self.logger.info("*** End of login DDT Test ***")
        self.logger.info("***** Completed TC_LoginDDT_002 *****")
