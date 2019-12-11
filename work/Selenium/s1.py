from selenium import webdriver
import time
import json

driver= webdriver.Chrome()
driver.get("http://www.soso.com")
dic={}

f= open("sr","r")
fh=f.readlines()
print (fh)
#fh=["1\n","2"]

for i in fh:
    driver.find_element_by_id("query").send_keys(i.strip())
    driver.find_element_by_id("stb").click()
    time.sleep(2)
    if i in driver.title:
        dic[i]="ok"
    time.sleep(5)
    driver.back()
    time.sleep(1)

driver.quit()
print (dic)
with open("result","w") as ff:
    ff.write(str(dic))
