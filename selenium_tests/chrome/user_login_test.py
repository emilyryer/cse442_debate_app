import time
from selenium import webdriver
import test_functions

#This test requires the registration test to pass. If a user cannot register, then they also cannot log in

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(1)
test_functions.login('test@test.123', 'Login_pass', driver)
test_functions.logout(driver);


driver.quit()
