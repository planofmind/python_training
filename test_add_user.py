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
