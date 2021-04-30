from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


for i in range(7):
	location="C:/Users/ravis/Downloads/chromedriver.exe"
	driver=webdriver.Chrome(location)
	driver.maximize_window();
	driver.get("https://www.google.com/search?rlz=1C1CHBF_enIN870IN870&sxsrf=ALeKk00DzYDHXxEvA6luzwe0m5ftdiH0rw%3A1607774376513&ei=qLDUX6TkHpiI4-EPqMyhkAc&q=buygorgeous&oq=buygo&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMgUIABDJAzICCAAyBAgAEAoyAggAMgQIABAKMgIIADIECAAQCjIECAAQCjIECAAQCjoECAAQRzoHCCMQ6gIQJzoICAAQyQMQkQI6BQgAEJECOggILhDHARCjAjoFCAAQsQM6CAgAELEDEIMBOgsILhCxAxDHARCjAjoICC4QsQMQgwE6DgguEMcBEKMCEJECEJMCOgIILjoLCC4QsQMQxwEQrwE6DgguELEDEIMBEMcBEKMCOgsILhDHARCvARDJA1Dq_RdY3pAYYNybGGgBcAF4AIAB0wGIAZ8HkgEFMC4zLjKYAQCgAQGqAQdnd3Mtd2l6sAEKyAEIwAEB&sclient=psy-ab")
	try:
		driver.find_element_by_xpath('//*[@id="rso"]/div[4]/div/div[1]/a/div/cite').click();
	except:
		driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[4]/div/div[1]/a/div/cite').click();
	driver.close();
	
