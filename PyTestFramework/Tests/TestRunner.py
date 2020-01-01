import os
import shutil
from datetime import datetime

allureSourcePath = "C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\PyTestFramework\\reports\\allure_json"
allureDestPath = "C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\PyTestFramework\\reports\\allure_report"

shutil.rmtree(allureSourcePath)

os.system("cd C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\PyTestFramework\\Tests")
os.system("pytest --alluredir="+allureSourcePath)

now = datetime.now()
time = now.strftime("%d%m%Y%H%M%S")
os.mkdir(allureDestPath + "\\" + time, 777)

os.system("allure generate " + allureSourcePath + " -o " + allureDestPath + "\\" + time)