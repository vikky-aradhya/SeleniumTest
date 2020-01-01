from selenium import webdriver
import pytest
from PyTestFramework.Pages.loginPage import LoginPage
from PyTestFramework.GenericFunctions import ReadData

class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://newtours.demoaut.com/")
        yield
        driver.quit()
        print("Test Completed")

    def test_login(self,test_setup):
        login = LoginPage(driver)
        login.enter_username(ReadData.getData("UserID"))
        login.enter_password(ReadData.getData("PWD"))
        login.click_login()
