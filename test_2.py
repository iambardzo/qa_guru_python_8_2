from selene import  be, have, browser

def test_first_less1(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_second_less2(browser_open):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('11223344qqwweerr').press_enter()
    browser.element('[id="search"]').should(have.text('текс 11223344qqwweerr не найден'))