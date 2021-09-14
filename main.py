from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
try:
    browser.get('https://mail.yandex.ru')
    browser.find_element_by_css_selector('.HeadBanner-Button-Enter').click()
    browser.find_element_by_id('passp-field-login').send_keys('TestNeoflexUser')
    browser.find_element_by_id('passp:sign-in').click()
    sleep(3)
    browser.find_element_by_id('passp-field-passwd').send_keys('123456xU')
    browser.find_element_by_id('passp:sign-in').click()
    sleep(330)
finally:
    browser.quit()