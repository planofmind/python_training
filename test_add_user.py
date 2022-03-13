# -*- coding: utf-8 -*-
import pytest
from application import Application
from user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.create_user(User(
        firstname="Дмитрий",
        middlename="Юрьевич",
        lastname="Журавлёв",
        nickname="planofmind",
        title="Title",
        company="My company",
        address="My address",
        home_phone="My home phone",
        mobile_phone="My mobile phone",
        work_phone="My work phone",
        fax="My fax",
        email="My email",
        email2="My email2",
        email3="My email3",
        homepage="My homepage",
        address2="My address2",
        phone2="My phone2",
        notes="My notes",
        bday="26",
        bmonth="September",
        byear="1987",
        aday="13",
        amonth="March",
        ayear="2022")
    )
    app.logout()


def test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.create_user(User(
        firstname="",
        middlename="",
        lastname="",
        nickname="",
        title="",
        company="",
        address="",
        home_phone="",
        mobile_phone="",
        work_phone="",
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
    app.logout()
