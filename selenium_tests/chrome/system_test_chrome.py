import time
from selenium import webdriver

#This test is to show that you've properly set up selenium on your system.
driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('https://zippy-hold-232119.appspot.com/');
time.sleep(5) # Let the user actually see something!

html = driver.page_source
print(html) #This should be the source for the page

driver.quit() #terminates program
