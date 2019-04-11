import time
from selenium import webdriver
import test_functions

#This test requires an existing user, called Login_test
#If user does not exist, they should be registered prior to creation.
#Email is test@test.123, Username is Login_test, password is Login_pass

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('https://zippy-hold-232119.appspot.com/');
time.sleep(1)

email = 'hello@123.hello'
test_functions.register(email, 'Prof_test', 'Prof_pass', driver)

profilelink = driver.find_element_by_link_text('My Profile')
profilelink.click()
time.sleep(1)

cpass = driver.find_element_by_name('cpass')
cpass.click()
oldPass = driver.find_element_by_name('old_password')
newPass1 = driver.find_element_by_name('new_password1')
newPass2 = driver.find_element_by_name('new_password2')
oldPass.send_keys('Prof_pass')
newPass1.send_keys('Prof_pass1')
newPass2.send_keys('Prof_pass1')
time.sleep(1)
submitButton = driver.find_element_by_id('submitcpass')
submitButton.click()
time.sleep(1)

cuser = driver.find_element_by_name('cuser')
cuser.click()
cuserTest = driver.find_element_by_id('id_new_username')
cuserTest.send_keys('Prof_test_new')
time.sleep(1)
submitButton = driver.find_element_by_id('submitcuser')
submitButton.click()
time.sleep(1)

deleteacc = driver.find_element_by_name('deleteacc')
deleteacc.click()
delemail = driver.find_element_by_id('id_del_email')
delpassword = driver.find_element_by_id('id_delpassword')
delemail.send_keys(email)
delpassword.send_keys('Prof_pass1')
time.sleep(1)
submitdel=driver.find_element_by_id('submitdel')
submitdel.click()
time.sleep(1)

test_functions.login(email, 'Prof_pass1', driver)

driver.quit()
