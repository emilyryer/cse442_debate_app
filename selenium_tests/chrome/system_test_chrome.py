import time
from selenium import webdriver

#This test is to show that you've properly set up selenium on your system.
driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('University at buffalo') #Types this text into the search_box element
search_box.submit()
time.sleep(5) # Let the user actually see something!

html = driver.page_source
print(html) #this is going to be painfully long, but it makes sense, I swear

driver.quit() #terminates program
