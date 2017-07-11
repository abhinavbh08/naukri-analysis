from pymongo import MongoClient
from requests.auth import HTTPProxyAuth
from nauk_page import get_data


client = MongoClient()
proxyDict = { 
          'http'  : '172.16.12.2:3128', 
          'https' : '172.16.12.2:3128'
        }
auth = HTTPProxyAuth('abhinav', '**********')
site_add = "https://www.naukri.com/data-scientist-jobs"

req_list, loc_list, exp_list, job_list, sal_list = get_data(site_add, proxyDict, auth)

db = client['jobs_database']
coll = db['naukri_jobs']

for i in range(0,len(loc_list)):
	data = {"Job":job_list[i] ,"Experience":exp_list[i] ,"Requirements":req_list[i] , "Location":loc_list[i] , "Salary":sal_list[i],}
	coll.insert_one(data)
