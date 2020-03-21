from selenium.webdriver import Chrome
from selenium import webdriver
import time
from bs4 import BeautifulSoup

web_driver_address = r"C:\\Users\\hp\\Downloads\\chromeDriver\\chromedriver.exe"


# options = webdriver.ChromeOptions()
driver = Chrome(web_driver_address)
driver.implicitly_wait(30)
site_add = "https://www.naukri.com/job-listings-Solution-Developer-data-Scientist-data-Analyst-Machine-Learning-Tatvic-Ahmedabad-2-to-4-years-060320901433?src=jobsearchDesk&sid=15842656797941&xp=1&px=1"
driver.get(site_add)
time.sleep(2)
data = driver.page_source
driver.close()
data = BeautifulSoup(data)
single_job = data.find(class_="top")
salary = single_job.find(class_="salary").find("span").get_text()
experience = single_job.find(class_="exp").find("span").get_text()
location = single_job.find(class_="loc").find("a").get_text()
key_skills_list = []
key_skills = data.find(class_="key-skill").findAll("a")
for skill in key_skills:
    key_skills_list.append(skill.find("span").get_text())
abc = 5

driver = Chrome(web_driver_address)
driver.implicitly_wait(30)
driver.get(site_add)
time.sleep(2)
data = driver.page_source
driver.close()
data = BeautifulSoup(data)
data