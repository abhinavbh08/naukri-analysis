from selenium.webdriver import Chrome
from selenium import webdriver
import time
from bs4 import BeautifulSoup

site_add = "https://www.naukri.com/data-scientist-jobs"
web_driver_address = r"C:\\Users\\hp\\Downloads\\chromeDriver\\chromedriver.exe"

def get_page_source(site_add):
    driver = Chrome(web_driver_address)
    driver.implicitly_wait(30)
    driver.get(site_add)
    time.sleep(2)
    data = driver.page_source
    driver.close()
    soup = BeautifulSoup(data)
    return soup

def get_data(site_add):

    key_skills_list = []
    location_list = []
    experience_list = []
    salary_list = []

    for i in range(0, 4):

        soup = get_page_source(site_add)
        all_rows = soup.find(class_="srp_container fl")
        data_rows = all_rows.find_all(class_="row")
        for item in data_rows:
            each_row = item.find('a')
            if each_row is None:
                continue
            link = each_row['href']
            print(link)
            in_soup = get_page_source(link)
            single_job = in_soup.find(class_="top")
            salary_list.append(single_job.find(class_="salary").find("span").get_text())
            experience_list.append(single_job.find(class_="exp").find("span").get_text())
            location_list.append(single_job.find(class_="loc").find("a").get_text())
            key_skills = in_soup.find(class_="key-skill").findAll("a")
            for skill in key_skills:
                key_skills_list.append(skill.find("span").get_text())

        print('\n')
    butt = all_rows.find(class_="pagination")
    anchor = butt.find('a')
    site_add = anchor['href']
    print('\n')

    return requirements_list, location_list, salary_list, experience_list

get_data(site_add)
