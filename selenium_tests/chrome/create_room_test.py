import time
from selenium import webdriver
import test_functions

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('https://zippy-hold-232119.appspot.com/');
time.sleep(2) # Let the user actually see something!

email = 'test@test.123'
test_functions.register(email, 'create_test', 'create_pass', driver)

test_functions.createRoom('Test', 'Test Question', driver)

test_functions.delete_account(email, 'create_pass', driver)
driver.quit() #terminates program
