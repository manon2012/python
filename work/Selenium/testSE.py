from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.soso.com")


# driver.find_element_by_id("query").send_keys("python")
# driver.find_element_by_id("stb").click()

# time.sleep(2)
#
# driver.back()

f=open("sr",'r')
fh=f.readlines()
print(fh)
dic={}
for i in fh:
    # driver = webdriver.Chrome()
    # driver.get("http://www.soso.com")
    print("000")
    driver.find_element_by_id("query").send_keys(i)
    print("111")
    time.sleep(1)
    driver.find_element_by_id("stb").click()
    print("222")
    time.sleep(2)
    print("1111111")
    title=driver.title
    print (title )
    if i in title:
        dic[i]="good"
    #driver.quit()
    time.sleep(2)
    driver.back()
#
# print (dic)


# title=driver.title
# print (title )
# if "python" in title:
#     print("good")



