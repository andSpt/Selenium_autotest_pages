from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main p[class=price_color]")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")


class BasketPageLocators():
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.basket-items h3 ")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color.align-right")
