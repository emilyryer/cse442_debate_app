import time
from selenium import webdriver
import test_functions

#This test requires an existing user, called Login_test
#If user does not exist, they should be registered prior to creation.
#Email is test@test.123, Username is Login_test, password is Login_pass

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(1)
test_functions.login('test@test.123', 'Login_pass', driver)

profilelink = driver.find_element_by_link_text('My Profile')
profilelink.click()
time.sleep(1)

cpass = driver.find_element_by_name('cpass')
cuser = driver.find_element_by_name('cuser')
deleteacc = driver.find_element_by_name('deleteacc')

test_functions.logout(driver)
driver.quit()
