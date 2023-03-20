from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_page(self):
        self.should_be_basket_url()
        self.should_be_name_product()
        self.should_be_price_product()


    def should_be_basket_url(self):
        """Проверка на url-адрес корзины"""

        current_url = self.browser.current_url
        assert "basket" in current_url, "There is no 'busket' in the link"

    def should_be_name_product(self):
        """Проверка присутствия присутствия товара в корзине и return его наименования"""

        assert (name_product := self.get_element(
            BasketPageLocators.NAME_PRODUCT)), "Price product is not presented"
        return name_product.text


    def should_be_price_product(self):
        """Проверка присутствия цены товара в корзине и return ее"""

        assert (price_product := self.get_element(
            BasketPageLocators.PRICE_PRODUCT)), "Price product is not presented"
        return price_product.text