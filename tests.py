from pages.postpage import PostPage
from time import sleep
to_whom = 'testmail@test.ru'
subj = 'test_neoflex'
text = 'Это письмо для тестового задания'


# class Test_1():
#     def test_step_1(self, browser):
#         page = PostPage(browser, 'https://mail.yandex.ru', 15)
#         browser.set_window_size('1920', '1080')
#         page.open_page()
#         page.authorize_user('TestNeoflexUser', '123456xU')
#         page.should_be_autorized_user()
#
#     def test_step_2(self, browser):
#         page = PostPage(browser, 'https://mail.yandex.ru', 15)
#         page.click_a_writing_button()
#         page.should_be_writing_form()
#
#     def test_step_3(self, browser):
#         page = PostPage(browser, 'https://mail.yandex.ru', 15)
#         page.write_a_letter(to_whom, subj, text)
#         page.should_be_a_saved_message()
#
#     def test_step_4(self, browser):
#         page = PostPage(browser, 'https://mail.yandex.ru', 25)
#         page.go_to_drafts()
#         page.open_draft()
#         page.draft_should_be_filled_with_presaved_data(to_whom, subj, text)
#
#     def test_step_5(self, browser):
#         page = PostPage(browser, 'https://mail.yandex.ru', 15)
#         page.exit()
#         page.should_be_password_field()


class Test2():
    def test_step_1(self, browser):
        page = PostPage(browser, 'https://mail.yandex.ru', 15)
        browser.set_window_size('1920', '1080')
        page.open_page()
        page.authorize_user('TestNeoflexUser', '123456xU')
        page.should_be_autorized_user()

    def test_step_2(self, browser):
        page = PostPage(browser, 'https://mail.yandex.ru', 15)
        page.click_a_writing_button()
        page.should_be_writing_form()

    def test_step_3(self, browser):
        page = PostPage(browser, 'https://mail.yandex.ru', 15)
        page.write_a_letter(to_whom, subj, text)
        page.send_letter()
        page.should_be_sended_message()

    def test_step_4(self, browser):
        page = PostPage(browser, 'https://mail.yandex.ru', 15)
        # sleep(10)
        page.go_to_sended()
        # sleep(10)
        page.sended_letter_should_be_filled_with_presaved_data(to_whom, subj, text)

    def test_step_5(self, browser):
        page = PostPage(browser, 'https://mail.yandex.ru', 15)
        page.exit()
        page.should_be_password_field()












