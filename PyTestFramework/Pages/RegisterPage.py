from selenium.webdriver.support.ui import Select


class RegisterPage():
    # Register link
    Regiser_link_xpath = "//a[text()='REGISTER']"

    # contact_information
    firstname_textbox_name = "firstName"
    lastname_textbox_name = "lastName"
    phone_number_textbox_name = "phone"
    email_textbox_name = "userName"

    # mailing_information
    address_textbox_name = "address1"
    city_textbox_name = "city"
    state_textbox_name = "state"
    postal_code_textbox_name = "postalCode"
    country_dropdown_name = "country"

    # user_information
    register_username_textbox_name = "email"
    register_password_textbox_name = "password"
    conf_password_textbox_name = "confirmPassord"

    # Clickregister_button
    register_button_name = "register"
    registered_user_name = "//b[contains(text(),' Note: Your user name is')]"

    # creating constructor
    def __init__(self, driver):
        self.driver = driver

    def click_register(self):
        self.driver.find_element_by_xpath(self.Regiser_link_xpath).click()

    def set_contact_information(self, firstname, lastname, phonenumber, emailaddress):
        rTitle = self.driver.title

        self.driver.find_element_by_name(self.firstname_textbox_name).send_keys(firstname)
        self.driver.find_element_by_name(self.lastname_textbox_name).send_keys(lastname)
        self.driver.find_element_by_name(self.phone_number_textbox_name).send_keys(phonenumber)
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(emailaddress)

    def set_mailing_information(self, addressdetial, cityname, statename, postal, countryname):
        self.driver.find_element_by_name(self.address_textbox_name).send_keys(addressdetial)
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(cityname)
        self.driver.find_element_by_name(self.state_textbox_name).send_keys(statename)
        self.driver.find_element_by_name(self.postal_code_textbox_name).send_keys(postal)
        select = Select(self.driver.find_element_by_name(self.country_dropdown_name))
        select.select_by_visible_text(countryname)

    def set_user_information(self, username, password, cnfpassword):
        self.driver.find_element_by_name(self.register_username_textbox_name).send_keys(username)
        self.driver.find_element_by_name(self.register_password_textbox_name).send_keys(password)
        self.driver.find_element_by_name(self.conf_password_textbox_name).send_keys(cnfpassword)

    def click_submitregister(self):
        self.driver.find_element_by_name(self.register_button_name).click()
        userName = self.driver.find_element_by_xpath(self.registered_user_name).text
        userName = userName.split('Note: Your user name is ')[1]