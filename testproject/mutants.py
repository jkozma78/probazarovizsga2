from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')

labels = driver.find_elements_by_xpath('//label')  # csapatok rádió gombjai, ezeket kattintjuk
teams = ("original", "force", "factor", "hellfire")  # csapatok nevei
res = {labels[i]: teams[i] for i in range(len(teams))}  # közös dictionary-be rendezve

teamtags = []
characters = []

# minden oldalon kiolvassuk és listába rendezzük a megjelenő és a csapathoz tartozó karaktereket
# változó elnevezések random ötlet volt
for i in res:

    fg = driver.find_elements_by_xpath(f'//*[contains(@data-teams, {res[i]})]/h2')

    for ee in fg:
        if ee.text != "":
            teamtags.append(ee.text)

    for d in driver.find_elements_by_tag_name("h2"):
        if d.text != "":
            characters.append(d.text)
    i.click()
# a két generált lista összehasonlítása
assert characters == teamtags
driver.close()
