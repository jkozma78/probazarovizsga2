from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html')

#data.txt beolvasása az atomok vátozóba
atomok = []
with open("data.txt") as periodic:
    line = periodic.readline()

    while line:
        atomok.append(line.strip().split(','))
        line = periodic.readline()

#öszehasonlítás
for i in atomok:
    strg = f'"{i[0]}"'
    web_text = driver.find_element_by_xpath(f"//li[@data-pos={strg}]/span").text
    web_atom = f" {web_text}"
    assert web_atom == i[1]
driver.close()
