import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False, driver_path=r"C:/Users/azb/Downloads/Compressed/hromedriver_win"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path 
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('detach', True)
        self.teardown = teardown
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com")
        try:
            cancel_btn = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Dismiss sign-in info."]')
            cancel_btn.click()
        except:
            pass

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        try:
            cancel_btn = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Dismiss sign-in info."]')
            cancel_btn.click()
        except:
            pass

        xpath_expression = f"//button[contains(., '{currency}')]"
        selected_currency_element = self.find_element(
            By.XPATH,
            xpath_expression
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)
        xpath_expression = f"//li[contains(., '{place_to_go}')]"
        first_result = self.find_element(
            By.XPATH,
            xpath_expression
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f"span[data-date='{check_in_date}']"
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f"span[data-date='{check_out_date}']"
        )
        check_out_element.click()
    
    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]'
        )
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                   By.CSS_SELECTOR,
                    'body > div#indexsearch.xpi__content__wrapper.xpi__content__wrappergray.xpi__content_hero_banner:nth-child(6) > div.hero-banner-searchbox:nth-child(2) > div > div > form.a0ac39e217 > div.ffa9856b86.db27349d3a.cc9bf48a25:nth-child(1) > div.f9cf783bde:nth-child(3) > div.d67edddcf0 > div.a207cf5a0d:nth-child(2) > div.a5da3001f3.a73af396c3 > div.df856d97eb:nth-child(1) > div.b2b5147b20:nth-child(1) > div.e98c626f34:nth-child(3) > button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.cd7aa7c891:nth-child(1)'
            )
            decrease_adults_element.click()
            
            adults_value_element = self.find_element(
                By.ID, 'group_adults'
            )
            adults_value = adults_value_element.get_attribute('value')
            
            if int(adults_value) == 1:
                break
        
        increase_adults_element = self.find_element(
            By.CSS_SELECTOR,
            'body > div#indexsearch.xpi__content__wrapper.xpi__content__wrappergray.xpi__content_hero_banner:nth-child(6) > div.hero-banner-searchbox:nth-child(2) > div > div > form.a0ac39e217 > div.ffa9856b86.db27349d3a.cc9bf48a25:nth-child(1) > div.f9cf783bde:nth-child(3) > div.d67edddcf0 > div.a207cf5a0d:nth-child(2) > div.a5da3001f3.a73af396c3 > div.df856d97eb:nth-child(1) > div.b2b5147b20:nth-child(1) > div.e98c626f34:nth-child(3) > button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.d64a4ea64d:nth-child(3)'
        )
        
        for _ in range(count-1):
            increase_adults_element.click()
        
    
    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        )
        search_button.click()
    
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(
            By.ID,
            'search_results_table'
        )
        
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)

        