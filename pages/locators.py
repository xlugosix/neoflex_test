from selenium.webdriver.common.by import By


class PostPageLocators():
    POST_TEXT = (By.CSS_SELECTOR, '.PSHeaderService-Text')
    POST_WRITE_LETTER = (By.CSS_SELECTOR, '.mail-ComposeButton-Text')
    WRITING_FORM = (By.CSS_SELECTOR, '.composeHeader-Text')
    SEND_TO = (By.CSS_SELECTOR, '.composeYabbles')
    SUBJECT = (By.CSS_SELECTOR, '.composeTextField')
    TEXT = (By.CSS_SELECTOR, '.cke_wysiwyg_div')
    SAVED_TEXT = (By.CSS_SELECTOR, '.composeHeader-SavedAt')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '.ControlButton_button_close')
    DRAFTS = (By.PARTIAL_LINK_TEXT, 'Черновики')
    DRAFT_LETTER = (By.PARTIAL_LINK_TEXT, 'test_neoflex')
    DRAFT_SEND_TO = (By.CSS_SELECTOR, '.ComposeYabble-Text')
    DRAFT_SUBJECT = (By.CSS_SELECTOR, 'span.composeHeader-Title > span')
    USER_PIC = (By.CSS_SELECTOR, '.user-pic')
    EXIT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Выйти из сервисов Яндекса')
    SEND_BUTTON = (By.CSS_SELECTOR, '.ComposeControlPanel-SendButton')
    SENDED = (By.PARTIAL_LINK_TEXT, 'Отправленные')
    LETTER_SENDED = (By.CSS_SELECTOR, '.ComposeDoneScreen-Title')
    SENDED_LETTER = (By.PARTIAL_LINK_TEXT, 'test_neoflex')
    TRIANGLE = (By.CSS_SELECTOR, '.mail-Message-Head-Recievers-More')
    SENDED_TO = (By.CSS_SELECTOR, '.mail-User-Name')
    SENDED_SUBJ = (By.CSS_SELECTOR, '.mail-Message-Toolbar-Subject')
    SENDED_TEXT = (By.CSS_SELECTOR, '.mail-Message-Body-Content')



class BasePageLocators():
    POST_ICON = (By.CSS_SELECTOR, '.PSHeaderIcon-Image_Mail')
    ENTER_BUTTON = (By.CSS_SELECTOR, '.HeadBanner-Button-Enter')
    LOGIN_FIELD = (By.ID, 'passp-field-login')
    LOGIN_ENTER_BUTTON = (By.ID, 'passp:sign-in')
    PASSWORD_FIELD = (By.ID, 'passp-field-passwd')

