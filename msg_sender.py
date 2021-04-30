from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

location="C:/Users/ravis/Downloads/chromedriver.exe"
driver=webdriver.Chrome(location)

driver.get("https://web.whatsapp.com/")

driver.maximize_window()
act=ActionChains(driver)
name=input("Enter name or group name:")
msg=input("Enter message:")
count=int(input("Enter count:"))

input("Enter anything after scanning")

user=driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for i in range(count):
	msg_box.send_keys(msg)
	act.send_keys(Keys.TAB).perform()
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print('success')