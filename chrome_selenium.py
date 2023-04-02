from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
service=Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_browser = webdriver.Chrome(service=service, options=chrome_options)
chrome_browser.get(url)
chrome_browser.fullscreen_window()


get_message = chrome_browser.find_element(By.ID, "user-message")
get_message.clear()
get_message.send_keys('Hello, Im doing automation')
button = chrome_browser.find_element(By.CLASS_NAME, "btn-default")
button.click()

show_output = chrome_browser.find_element(By.ID, "display")

assert "Hello, Im doing automation" in chrome_browser.page_source       # Page_source will have the whole code, assert will throw error if its not.

print(show_output.get_attribute('innerHTML'))      # Will get the o/p whatever you mentioned in console.

time.sleep(1)

# Date_picker

url2 = 'https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html'

browser2 = chrome_browser.get(url=url2)

date = chrome_browser.find_element(By.CLASS_NAME, "form-control")
date.send_keys('04/03/98')

time.sleep(1)

date_range_start = chrome_browser.find_element(By.CSS_SELECTOR, '.input-daterange input:first-child')
date_range_end = chrome_browser.find_element(By.CSS_SELECTOR, '.input-daterange input:last-child')
date_range_start.send_keys('01/01/21'), date_range_end.clear(), date_range_end.send_keys('02/02/21')

chrome_browser.get_screenshot_as_png()
chrome_browser.save_screenshot('automation.png')

time.sleep(1)

# Table:
url3 = 'https://demo.seleniumeasy.com/table-pagination-demo.html#'
browser3 = chrome_browser.get(url3)
next_page = chrome_browser.find_element(By.LINK_TEXT, '3')
next_page.click()


cur_url = chrome_browser.current_url
print(cur_url)
chrome_browser.quit()

