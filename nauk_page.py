import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from requests.auth import HTTPProxyAuth

proxyDict = { 
          'http'  : '172.16.12.2:3128', 
          'https' : '172.16.12.2:3128'
        }
auth = HTTPProxyAuth('abhinav', '********')

#page = requests.get("https://www.naukri.com/data-scientist-jobs")
#soup = BeautifulSoup(page.content, 'html')

site_add = "https://www.naukri.com/data-scientist-jobs"
'''
#driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(site_add)
'''

def get_data(site_add, proxyDict, auth):
	i = 0
	req_list = []
	loc_list = []
	exp_list = []
	sal_list = []
	job_list = []

	while(i<4):
#		page = requests.get(site_add,proxies=proxyDict, auth=auth)
		page = requests.get(site_add)
		print("Done")
		soup = BeautifulSoup(page.content, 'html')
		all_rows = soup.find(class_ = "srp_container")
		data_rows = all_rows.find_all(class_ = "row ")
		for item in data_rows:
			req_inside=[]
			each_row = item.find('a')
			link = each_row['href']
			print(link)
			in_page = requests.get(link)
			in_soup = BeautifulSoup(in_page.content, 'html')
			seven_day = in_soup.find(class_ = "ksTags")
			if seven_day:
				items = seven_day.find_all('a')
				for item in items:
					req_inside.append(item.get_text().lstrip())
				items = seven_day.find_all('span')
				for item in items:
					req_inside.append(item.get_text().lstrip())
				req_list.append(req_inside)
			job = in_soup.find(class_ = "hdSec")
			if job:
				job_name = job.find('h1')
				job_list.append(job_name.get_text().lstrip())

				exp = job.find(class_ = 'p')
				exp_div = exp.find('span')
				exp_list.append(exp_div.get_text())

				loc_div = exp.find('a')
				loc_list.append(loc_div.get_text())

			sal = in_soup.find(class_="sal")
			if sal:
				sal_list.append(sal.get_text().lstrip())

			print('\n')
		butt = all_rows.find(class_ = "pagination")
		anchor = butt.find('a')
		site_add = anchor['href']
		i = i+1
		print('\n')

	return req_list, loc_list, exp_list, job_list, sal_list

'''
driver.wait = WebDriverWait(driver, 5)
button = driver.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "grayBtn")))
button.click()
'''
