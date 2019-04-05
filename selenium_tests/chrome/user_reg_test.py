import time
from selenium import webdriver
import test_methods

#this test creates a fake email that is unique each time by using a timestamp.

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(1)
login_link = driver.find_element_by_link_text('register')
login_link.click()
time.sleep(.2)
try:
    email_field = driver.find_element_by_name('email')
except NoSuchElementException:
    print('Could not find email element in page.')
    driver.quit()
try:
    nickname_field = driver.find_element_by_name('nickName')
except NoSuchElementException:
    print('Could not find nickname element in page.')
    driver.quit()
try:
    password1_field = driver.find_element_by_name('password1')
except NoSuchElementException:
    print('Could not find password element in page.')
    driver.quit()
try:
    password2_field = driver.find_element_by_name('password2')
except NoSuchElementException:
    print('Could not find password confirmation element in page.')
    driver.quit()
#This part creates a unique email.
timestamp = time.time()
timestring = str(timestamp)
email_field.send_keys(timestring + 'test@test.123')
nickname_field.send_keys('Reg_test')
password1_field.send_keys('Login_pass')
password2_field.send_keys('Login_pass')
time.sleep(2)
try:
    reg_button = driver.find_element_by_class_name('btn')
    reg_button.click()
except NoSuchElementException:
    print('Could not find button to log in.')
    driver.quit()

time.sleep(2)

test_methods.logout()


driver.quit()
