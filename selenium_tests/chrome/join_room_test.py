import time
from selenium import webdriver
import test_functions

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('https://zippy-hold-232119.appspot.com/');
time.sleep(2) # Let the user actually see something!

email1 = test_functions.generateTestEmail()
test_functions.register(email1, 'create_test1', 'create_pass1', driver)

test_functions.createRoom('Test', 'Test Question')

#This is where we get the room ID

test_functions.logout()
email2 = test_functions.generateTestEmail()
test_functions.register(email2, 'create_test2', 'create_pass2', driver)'
