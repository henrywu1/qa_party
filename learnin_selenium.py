import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.todaytix.com/')

# find the sign up button
signUpButton = browser.find_element_by_xpath('//*[@class="_3yUQHBPYKz"]//*[@class="_2PIKsw2AV2"]')
# click it
signUpButton.click()

# find and assert the modal comes out
modal = browser.find_element_by_xpath('//*[@class="_1Yxt62AL-1"]')

# find email input
emailField = modal.find_element_by_xpath('//input[@name="email"]')
# find that label thingy
emailLabelEle = emailField.find_element_by_xpath('parent::*/label')

# assert the label is correct when empty
assert emailLabelEle.text == 'Email Address'

browser.quit()
