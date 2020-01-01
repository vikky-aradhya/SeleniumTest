from selenium import webdriver
import pytest
from PyTestFramework.Pages.RegisterPage import RegisterPage
from PyTestFramework.GenericFunctions import ReadData
from selenium.webdriver.support.events import EventFiringWebDriver
from PyTestFramework.GenericFunctions.Screenshot import TakeScreenshots

class TestRegister:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\chromedriver.exe")
        driver = EventFiringWebDriver(driver,TakeScreenshots())
        driver.maximize_window()
        driver.get("http://newtours.demoaut.com/")
        yield
        driver.quit()
        print("Test Completed")

    def test_register(self,test_setup):
        register = RegisterPage(driver)
        register.click_register()
        register.set_contact_information(ReadData.getData("FirstName"), ReadData.getData("LastName"),
                                         ReadData.getData("Phone"), ReadData.getData("Email"))
        register.set_mailing_information(ReadData.getData("Address"), ReadData.getData("City"),
                                         ReadData.getData("State"), ReadData.getData("PostalCode"),
                                         ReadData.getData("Country"))
        register.set_user_information(ReadData.getData("Username"), ReadData.getData("Password"),
                                      ReadData.getData("Password"))
        register.click_submitregister()


