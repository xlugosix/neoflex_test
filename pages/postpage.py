from .basepage import BasePage
from .locators import PostPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class PostPage(BasePage):
    def should_be_autorized_user(self):
        assert self.is_element_present(*PostPageLocators.POST_TEXT), 'пользователь не авторизовался'

    def click_a_writing_button(self):
        self.browser.find_element(*PostPageLocators.POST_WRITE_LETTER).click()

    def should_be_writing_form(self):
        assert self.is_element_present(*PostPageLocators.WRITING_FORM), 'нет формы создания письма'

    def write_a_letter(self, to_whom, subj, text):
        self.browser.find_element(*PostPageLocators.SEND_TO).send_keys(to_whom)
        self.browser.find_element(*PostPageLocators.SUBJECT).send_keys(subj)
        self.browser.find_element(*PostPageLocators.TEXT).send_keys(text)

    def should_be_a_saved_message(self):
        assert self.is_element_present(*PostPageLocators.SAVED_TEXT), 'нет текста о сохранении черновика, черновик ' \
                                                                      'не сохранен'
    def click_on_close_button(self):
        self.browser.find_element(*PostPageLocators.CLOSE_BUTTON).click()


    def go_to_drafts(self):
        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Черновики')))
        self.browser.find_element(*PostPageLocators.DRAFTS).click()

    def open_draft(self):
        self.browser.find_element(*PostPageLocators.DRAFT_LETTER).click()

    def draft_should_be_filled_with_presaved_data(self, to_whom, subj, text):
        assert self.browser.find_element(*PostPageLocators.DRAFT_SEND_TO).text == to_whom, 'получатель в черновике' \
                                                                                           'не совпадает с заполненным' \


        assert self.browser.find_element(*PostPageLocators.TEXT).text == text, 'текст в черновкие не совпадает ' \
                                                                               'с заполненым'

    def exit(self):
        self.browser.find_element(*PostPageLocators.USER_PIC).click()
        self.browser.find_element(*PostPageLocators.EXIT_BUTTON).click()

    def send_letter(self):
        self.browser.find_element(*PostPageLocators.SEND_BUTTON).click()

    def should_be_sended_message(self):
        assert self.is_element_present(*PostPageLocators.LETTER_SENDED), 'письмо не отправлено'

    def go_to_sended(self):
        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Отправленные')))
        self.browser.find_element(*PostPageLocators.SENDED).click()
        self.browser.find_element(*PostPageLocators.SENDED_LETTER).click()

    def sended_letter_should_be_filled_with_presaved_data(self, to_whom, subj, text):

        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mail-User-Name')))
        assert self.browser.find_element(*PostPageLocators.SENDED_TO).text == to_whom
        assert self.browser.find_element(*PostPageLocators.SENDED_SUBJ).text == subj
        assert self.browser.find_element(*PostPageLocators.SENDED_TEXT).text == text















