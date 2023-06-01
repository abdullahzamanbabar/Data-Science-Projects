from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            By.ID,
            'filter_group_class_:R14q:'
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR,
            '*'
        )
        
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    
    def sort_price_lowest_first(self):
        button1 = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        button1.click()
        button2 = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-id="price"]'
        )
        button2.click()

