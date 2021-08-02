from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')

# elszámolunk 1-től százig és ha megjelenik a "Yes! That is it." felirat, akkor összehasonlítjuk a számlálókat
for i in range(1, 100):
    driver.find_element_by_tag_name("input").send_keys(i)

    driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    driver.find_element_by_tag_name("input").clear()
    try:
        if (driver.find_element_by_xpath('//p[@class="alert alert-success"]').text) == "Yes! That is it.":
            break
        assert i == int(driver.find_element_by_xpath('//span[@class="badge ng-binding"').text)
    except:
        pass

# határéertéken kívüli bevitelek tesztelése
testdata = {"-19": "Guess higher.", "255": "Guess lower."}

for i in (testdata):
    driver.find_element_by_tag_name("input").send_keys(i)
    driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    driver.find_element_by_tag_name("input").clear()
    (driver.find_element_by_xpath('//p[@class="alert alert-warning"]').text) == testdata[i]

driver.close()
