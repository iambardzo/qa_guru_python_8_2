import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session')
def browser_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture(scope='function')
def browser_open(browser_size):
    browser.open('https://google.com')
    yield
    browser.quit()