import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage1
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"  # you can use line 12 to 14 over this line from 7 to 9
    # username = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    logger = LogGen.loggen()


    def test_homePageTitle(self, setup):

        self.logger.info("***********Test_001_Login*************")
        self.logger.info("***********Verifying home page title *************")
        #self.driver = webdriver.Chrome("C:\\Users\\prashant_malusare\\PycharmProjects\\nopcommerceApp\\Drivers\\chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)

        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** home page title is passed*************")



        else:
            #self.driver.save_screenshot("C:\\Users\\prashant_malusare\\PycharmProjects\\nopcommerceApp\\Screenshots\\"
                                      #  + "test_homePageTitle.png") (both syntax working its optional for line 25 and 45
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")

            self.driver.close()
            self.logger.error("*********** home page title is failed *************")
            assert False

    def test_login(self, setup):
        self.logger.info("*********** Verifying the login test *************")

        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage1(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actual_title = self.driver.title


        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** login test is passed *************")



        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

            self.driver.close()

            self.logger.error("***********  login test is failed *************")
            assert False

