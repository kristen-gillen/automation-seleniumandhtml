from selenium import webdriver

#initialize Chrome instance and point to driver file : using locally for this project
chrome_browser = webdriver.Chrome('./chromedriver')

#print(chrome_browser) will launch the browser

#chrome_browser.maximize_window() #may get error about version, else launches browser and states it's being controlled by automatic software
chrome_browser.maximize_window() 
#Launch a website to test
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#check for correct page before automation starts, Selenium uses html, so find elements page on inspection. Each page has title tag, so key off of this
assert 'Selenium Easy Demo' in chrome_browser.title #if returns false it errors out and exits code 
#see cheat sheet reference for "selectors"

#Here we found a way to inspect the text for a button
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(button_text.get_attribute('innerHTML'))
#Now for something more useful
#Make sure we are progressing through code correctly with "assert"

assert 'Show Message' in chrome_browser.page_source
#using inspect on html to find id - can do with Selenium (here user message)
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
#automation of typing into this box
user_message.send_keys('I AM EXTRA COOL')
#now we can show message
show_message_button.click()
#now verify that this shows the correct thing using it's id
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text
# another useful method is chrome_browser.find_element_by_css_selector (styles of website)
user_button2 = chrome_browser.find_element_by_css_selector('#get-input> .btn')
#now find a way to close browser, sometimes below method won't work
#chrome_browser.close()
chrome_browser.quit()
#can cause headaches and may not work, check forums
#write a bot to check things, can use waits to simulate a delay, sleep/wait, to be more user like and not be blocked