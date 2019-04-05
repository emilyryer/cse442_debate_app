import time
from selenium import webdriver
import test_methods

#This test requires an existing user, called Login_test
#If user does not exist, they should be registered prior to creation.
#Username is Login_test, password is Login_pass

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(1)
test_methods.login('test@test.123', 'Login_pass')
test_methods.logout();


driver.quit()
