import time
from selenium import webdriver
import test_functions

#this test creates a fake email that is unique each time by using a timestamp.

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('https://zippy-hold-232119.appspot.com/');
time.sleep(1)

email = test_functions.generateTestEmail()
test_functions.register(email, 'Reg_test', 'Reg_pass', driver)
test_functions.logout(driver)
test_functions.login(email, 'Reg_pass', driver)
test_functions.logout(driver);


driver.quit()
