from selenium.webdriver.common.by import By
import time

def test_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Для визуальной проверки языка интерфейса
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_button) > 0, "Add to basket button is not present on the page"
