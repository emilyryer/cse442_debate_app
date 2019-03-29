import time
from selenium import webdriver

#This test requires an existing user, called Login_test
#If user does not exist, they should be registered prior to creation.
#Username is Login_test, password is Login_pass

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(1)
login_link = driver.find_element_by_link_text('login')
login_link.click()
time.sleep(.2)
try:
    username_field = driver.find_element_by_name('username')
except:
    print('Could not find username element in page.')
    driver.quit()
try:
    password_field = driver.find_element_by_name('password')
except:
    print('Could not find password element in page.')
    driver.quit()
username_field.send_keys('test@test.123')
password_field.send_keys('Login_pass')
time.sleep(2)
try:
    login_button = driver.find_element_by_class_name('btn')
    login_button.click()
except:
    print('Could not find button to log in; could not log in.')
    driver.quit()
time.sleep(2)
try:
    logout_link = driver.find_element_by_link_text('Logout')
    logout_link.click()
except:
    print('Could not find button to logout; could not log out.')
    driver.quit()

time.sleep(2)

driver.quit()
