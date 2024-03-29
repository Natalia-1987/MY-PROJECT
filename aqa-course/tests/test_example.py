from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import allure


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


""" Тест проверяет, что на веб-странице по указанному URL существует элемент (кнопка), содержащий часть текста 
    "Click", и этот элемент отображается. Если элемент найден и отображается, то утверждение успешно пройдено, 
    в противном случае тест будет считаться неудачным."""


@allure.parent_suite("parent suite - Browser")
@allure.feature('Simple button')
@allure.story('displayed button by link text')
@allure.label("owner", "nafanya")
def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()


""" Тест проверяет, что на веб-странице по указанному URL существует кнопка с уникальным идентификатором 
    'submit-id-submit', и эта кнопка отображается. 
    Если элемент найден и отображается, то утверждение успешно пройдено, 
    в противном случае тест будет считаться неудачным."""


@allure.parent_suite("parent suite - Browser")
@allure.feature('Simple button')
@allure.story('displayed button by id')
@allure.label("owner", "nafanya")
def test_button_exist_2(browser):
    with allure.step('Open page by check button "click"'):
        browser.get('https://www.qa-practice.com/elements/button/simple')
    with allure.step('Check resul the button'):
        btn_click = browser.find_element(By.ID, 'submit-id-submit')
        assert btn_click.is_displayed()
        assert 'Click' == btn_click.get_attribute('value')
    allure.attach(browser.get_screenshot_as_png(), name = 'text_attachments', attachment_type = AttachmentType.JPG)


"""Будем использовать декоратор @pytest.mark.parametrize для определения различных тестовых случаев. 
    Каждый тестовый случай представляет собой кортеж из входных данных (input_a, input_b) и ожидаемого результата (expected). 
    Каждый такой кортеж представляет один тестовый случай."""


@allure.parent_suite("parent suite - BE")
@allure.title('title')
@allure.description('description')
@allure.suite('suite')
@allure.epic("epic")
@allure.feature('feature')
@allure.story('story')
@allure.severity('Normal')
@allure.issue("SOL-001")
@allure.testcase("SOL-001")
@allure.label("owner", "hooch")
@pytest.mark.parametrize("input_a, input_b, expected", [(1, 2, 3), (5, 5, 10), (0, 0, 0)])
def test_addition_parametrized(input_a, input_b, expected):
    result = input_a + input_b
    assert result == expected, f"Expected {expected}, but got {result}"
