
class LoginPage():

    login_username_textbox_name = "userName"
    login_password_textbox_name = "password"
    login_button_name = "login"

    #creating constructor
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name(self.login_username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.login_password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()


