import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')

#form kitöltése
driver.find_element_by_xpath('//select').send_keys(1)
driver.find_element_by_tag_name('button').click()

driver.find_element_by_xpath('//input[@class="datepicker"]').send_keys("2021.10.11")
driver.find_element_by_xpath('//select[@name="bf_time"]').send_keys("Morning")
driver.find_element_by_xpath('//select[@name="bf_hours"]').send_keys("3")
driver.find_element_by_xpath('//button[@class="next-btn next-btn2"]').click()


driver.find_element_by_xpath('//input[@name="bf_fullname"]').send_keys("Teszt Elek")
driver.find_element_by_xpath('//input[@type="email"]').send_keys("teszt@elek.hu")
driver.find_element_by_xpath('//button[@class="submit-btn"]').click()

time.sleep(2)
#elvárt eredmény összehasonlítása
assert driver.find_element_by_tag_name('h2').text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

driver.close()