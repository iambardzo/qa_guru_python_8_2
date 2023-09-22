import pytest
from selene.support.shared import browser
from selene import be, have

def test_google_not_find():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('1122334455qqwwee').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу 1122334455qqwwee ничего не найдено'))