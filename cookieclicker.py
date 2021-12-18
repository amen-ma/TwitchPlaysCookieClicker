from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


base_url = "https://orteil.dashnet.org/cookieclicker/"

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get(base_url)

print(driver.title)


driver.implicitly_wait(5)

cookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")


actions = ActionChains(driver)
#actions.click(cookie)

#print(cookie_count.text)

for i in range(5000):
    actions.click(cookie).perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
