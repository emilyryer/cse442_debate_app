import time
from selenium import webdriver
import test_functions

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(2) # Let the user actually see something!

email = test_functions.generateTestEmail()
test_functions.register(email, 'create_test', 'create_pass', driver)

createButton = driver.find_element_by_link_text('Create Room')
createButton.click()
time.sleep(1)

nameField = driver.find_element_by_id('roomName')
topicField = driver.find_element_by_id('roomTopic')
createButton = driver.find_element_by_id('createButton')

nameField.send_keys('Test')
topicField.send_keys('This is the question')
time.sleep(1)
createButton.click()
time.sleep(1)


driver.quit() #terminates program
