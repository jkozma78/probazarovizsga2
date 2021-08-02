import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html')

# a filmek számának ellenőrzés, mindegyik h2-es elmben van tehát ezeket számoljuk
time.sleep(3)
assert len(driver.find_elements_by_tag_name("h2")) == 24

# az új film adatainak felvitele és a save gomb kattintása
driver.find_element_by_xpath('//button[@class="mostra-container-cadastro"]').click()
time.sleep(2)
driver.find_element_by_id("nomeFilme").send_keys("Black widow")
driver.find_element_by_id("anoLancamentoFilme").send_keys("2021")
driver.find_element_by_id("anoCronologiaFilme").send_keys("2020")
driver.find_element_by_id("linkTrailerFilme").send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
driver.find_element_by_id("linkImagemFilme").send_keys(
    "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg")
driver.find_element_by_id("linkImdbFilme").send_keys("https://www.imdb.com/title/tt3480822/")
driver.find_element_by_xpath('//button[@onclick="salvarFilme()"]').click()

# az ellenőrizendő h2-es elemek száma 25 kell legyen
assert len(driver.find_elements_by_tag_name("h2")) == 25

driver.close()
