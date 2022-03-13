from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def create_user(self, user):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        wd.find_element_by_name("middlename").send_keys(user.middlename)
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        wd.find_element_by_name("title").send_keys(user.title)
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").send_keys(user.home_phone)
        wd.find_element_by_name("mobile").send_keys(user.mobile_phone)
        wd.find_element_by_name("work").send_keys(user.work_phone)
        wd.find_element_by_name("fax").send_keys(user.fax)
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("email2").send_keys(user.email2)
        wd.find_element_by_name("email3").send_keys(user.email3)
        wd.find_element_by_name("homepage").send_keys(user.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(user.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(user.bmonth)
        wd.find_element_by_name("byear").send_keys(user.byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(user.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(user.amonth)
        wd.find_element_by_name("ayear").send_keys(user.ayear)
        wd.find_element_by_name("address2").send_keys(user.address2)
        wd.find_element_by_name("phone2").send_keys(user.phone2)
        wd.find_element_by_name("notes").send_keys(user.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def destroy(self):
        self.wd.quit()
