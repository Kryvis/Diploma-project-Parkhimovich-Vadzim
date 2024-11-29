import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://oma.by'

        super().__init__(web_driver, url)

    btn_menu_header_all_catalogue = WebElement(xpath='//div[@class= "header-menu_item header-menu_item__btn left-col"]')
    btn_menu_header_black_friday = WebElement(xpath='//div[@class="header-menu_item "])[1]')
    btn_menu_header_leaflet = WebElement(xpath='//div[@class="header-menu_item "])[2]')
    btn_menu_header_action = WebElement(xpath='//div[@class="header-menu_item "])[3]')
    btn_menu_header_profitable = WebElement(xpath='//div[@class="header-menu_item "])[4]')
    btn_menu_header_vacancies = WebElement(xpath='//div[@class="header-menu_item "])[5]')
    btn_menu_header_news = WebElement(xpath='//div[@class="header-menu_item "])[6]')
    btn_menu_header_installment = WebElement(xpath='//div[@class="header-menu_item "])[7]')