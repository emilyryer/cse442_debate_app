import time
from selenium import webdriver

#This test requires an existing user, called Login_test
#If user does not exist, they should be registered prior to creation.
#Username is Login_test, password is Login_pass

def generateTestEmail():
    timestamp = time.time()
    timestring = str(timestamp)
    email = timestring + 'test@test.123'
    return email

def login(username, password, driver):
    login_link = driver.find_element_by_link_text('login')
    login_link.click()
    time.sleep(.2)
    try:
        username_field = driver.find_element_by_name('username')
    except:
        print('Could not find username element in page.')
        driver.quit()
        return 1
    try:
        password_field = driver.find_element_by_name('password')
    except:
        print('Could not find password element in page.')
        driver.quit()
        return 1
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(2)
    try:
        login_button = driver.find_element_by_class_name('btn')
        login_button.click()
    except:
        print('Could not find button to log in; could not log in.')
        driver.quit()
        return 1
    time.sleep(2)
    return 0

def logout(driver):
    try:
        logout_link = driver.find_element_by_link_text('Logout')
        logout_link.click()
    except:
        print('Could not find button to logout; could not log out.')
        driver.quit()
    time.sleep(2)

def register(email, username, password, driver):
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
    email_field.send_keys(email)
    nickname_field.send_keys(username)
    password1_field.send_keys(password)
    password2_field.send_keys(password)
    time.sleep(2)
    try:
        reg_button = driver.find_element_by_class_name('btn')
        reg_button.click()
    except NoSuchElementException:
        print('Could not find button to log in.')
        driver.quit()

    time.sleep(2)

def createRoom(topic, question):
    createButton = driver.find_element_by_link_text('Create Room')
    createButton.click()
    time.sleep(1)

    nameField = driver.find_element_by_id('roomName')
    topicField = driver.find_element_by_id('roomTopic')
    createButton = driver.find_element_by_id('createButton')

    nameField.send_keys(topic)
    topicField.send_keys(question)
    time.sleep(1)
    createButton.click()
    time.sleep(2)

def delete_account(email, password, driver):
    profilelink = driver.find_element_by_link_text('My Profile')
    profilelink.click()
    deleteacc = driver.find_element_by_name('deleteacc')
    deleteacc.click()
    delemail = driver.find_element_by_id('id_del_email')
    delpassword = driver.find_element_by_id('id_delpassword')
    delemail.send_keys(email)
    delpassword.send_keys(password)
    time.sleep(1)
    submitdel=driver.find_element_by_id('submitdel')
    submitdel.click()
    time.sleep(1)

#def joinRoom(roomname, roomID):
