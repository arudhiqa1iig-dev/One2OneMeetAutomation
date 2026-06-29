from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_home_page_loads(driver):
    home_page = HomePage(driver)
    home_page.open()

    assert home_page.is_loaded()
    assert home_page.has_contact_link()


def test_contact_page_is_reachable(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_contact()

    contact_page = ContactPage(driver)
    assert contact_page.is_loaded()


def test_login_page_is_available(driver):
    login_page = LoginPage(driver)
    login_page.open()

    assert login_page.is_loaded()
    assert login_page.username_field_is_visible()
