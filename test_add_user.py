# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

from user import User


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_user(wd, User(
                         firstname="Ertyu",
                         middlename="Sdfgh",
                         lastname="Cvbnm",
                         nickname="FFFFF",
                         title="Title_here",
                         company="Company_here",
                         address="Address_here",
                         home="111",
                         mobile="222",
                         work="333",
                         fax="444",
                         email="qwe@qwe.ru",
                         email2="asd@asd.ru",
                         email3="zxc@zxc.ru",
                         homepage="homepage_here",
                         address2="Adress_here",
                         phone2="Home_here",
                         notes="Notes_here",
                         bday="23",
                         bmonth="December",
                         byear="2000",
                         aday="15",
                         amonth="April",
                         ayear="2020")
                         )
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_user(wd, User(
                         firstname="",
                         middlename="",
                         lastname="",
                         nickname="",
                         title="",
                         company="",
                         address="",
                         home="",
                         mobile="",
                         work="",
                         fax="",
                         email="",
                         email2="",
                         email3="",
                         homepage="",
                         address2="",
                         phone2="",
                         notes="",
                         bday="-",
                         bmonth="-",
                         byear="",
                         aday="-",
                         amonth="-",
                         ayear="")
                         )
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_user(self, wd, user):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        wd.find_element_by_name("middlename").send_keys(user.middlename)
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        wd.find_element_by_name("title").send_keys(user.title)
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").send_keys(user.home)
        wd.find_element_by_name("mobile").send_keys(user.mobile)
        wd.find_element_by_name("work").send_keys(user.work)
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

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
