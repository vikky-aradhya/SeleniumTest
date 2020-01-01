from datetime import datetime
from selenium.webdriver.support.events import AbstractEventListener
import allure

class TakeScreenshots(AbstractEventListener):
    def on_exception(self, exception, driver):
        global directory
        now = datetime.now()
        time = now.strftime("%d%m%Y%H%M%S")
        directory = "C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\PyTestFramework\\Screenshots\\screenshot" + time + ".png"
        driver.get_screenshot_as_file(directory)
        allure.attach.file(directory)