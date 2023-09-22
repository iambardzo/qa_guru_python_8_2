import pytest
from selene.support.shared import browser
from selene import be, have

def test_search_2(setting_browser):
    browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
    browser.element('[name="q"]').type('ыфа!2512афыа1йафывп!"№!"4').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("В поиске нет результатов...")