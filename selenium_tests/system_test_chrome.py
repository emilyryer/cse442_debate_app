import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

html = driver.page_source
print(html) #this is going to be painfully long, but it works, I swear
driver.quit()
