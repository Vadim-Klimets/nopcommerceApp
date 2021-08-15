import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


# To Run Test Cases at default browser
# pytest -v -s testCases/test_login.py

# To Run Test Cases at certain Browser
# pytest -v -s testCases/test_login.py --browser chrome
# pytest -v -s testCases/test_login.py --browser firefox

# To Run Test Cases at certain Browser in parallel
# pytest -v -s -n=3 testCases/test_login.py --browser chrome
# pytest -v -s -n=3 testCases/test_login.py --browser firefox

# To Run Test Cases with Pytest HTML Report Generation
# pytest -v --html=Reports\report.html testCases/test_login.py --browser chrome
# pytest -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

# To Run Data Driven Cases Pytest HTML Report Generation
# pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser chrome

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*************** Test_002_DDT_Login   **************")
        self.logger.info("*************** Verifying Login Test **************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel:", self.rows)


        lst_status=[] # Empty list variable

        for r in range (2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed ...")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test *******")
        self.logger.info("****** Completed TC_Login_DDT_002 ******");