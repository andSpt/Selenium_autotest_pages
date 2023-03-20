from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class PageObject(BasePage):


    def should_be_add_to_basket(self):
        assert (button_add_to_basket := self.get_element(ProductPageLocators.ADD_TO_BASKET)), "Button 'Add_to_backet' is not presented"
        return button_add_to_basket


    def should_be_name_product(self):
        assert (name_product := self.get_element(ProductPageLocators.NAME_PRODUCT)), "Name product is not presented"
        return name_product.text


    def should_be_price_product(self):
        assert (price_product := self.get_element(ProductPageLocators.PRICE_PRODUCT)), "Price product is not presented"
        return price_product.text


    def go_to_basket_page(self):
        assert (link := self.get_element(ProductPageLocators.BASKET_LINK)), "Link to busket is not presented"
        link.click()