import time
from .pages.product_page import *
from .pages.basket_page import BasketPage



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()

    #Ищем кнопку "Добавить в корзину" и сохраняем в button_add_to_busket
    button_add_to_basket = page.should_be_add_to_basket()

    # Ищем наименование товара и сохраняем в name_product
    name_product_on_product_page = page.should_be_name_product()

    # Ищем стоимость товара и сохраняем в price_product
    price_product_on_product_page = page.should_be_price_product()

    # Добавляем товар в корзину
    button_add_to_basket.click()

    #Проверочный код
    page.solve_quiz_and_get_code()

    # time.sleep(20)


    #Переходим на страницу корзины
    page.go_to_basket_page()



    basket_page = BasketPage(browser, browser.current_url)

    #Проверяем, что находимся на странице корзины
    basket_page.should_be_basket_url()

    #Проверка и возврат наименования товара в корзине
    name_product_basket_page = basket_page.should_be_name_product()
    # print(name_product_basket_page, name_product_on_product_page)

    #Проверка и возврат цены товара в корзине
    price_product_basket_page = basket_page.should_be_price_product()



    #Сравниваем наименование и цену товара на странице товара и в корзине
    assert name_product_on_product_page == name_product_basket_page, "Название товара в корзине не соответствует"
    assert price_product_on_product_page == price_product_basket_page, "Цена товара в корзине не соответствует"
