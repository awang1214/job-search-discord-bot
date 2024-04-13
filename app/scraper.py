import requests
import json
        
class Job:
    def __init__(self, logo, company_name, title, app_url, remote, min_salary, max_salary):
        self.company_logo = logo
        self.company_name = company_name
        self.title = title
        self.app_url = app_url
        self.remote = remote
        self.min_salary = min_salary
        self.max_salary = max_salary
        
    def __str__(self):
        return f"\n{self.company_logo}\nCompany name: {self.company_name}\nTitle: {self.title}\nApplication URLs: {self.app_url}\nRemote: {self.remote}\nSalary: ${self.min_salary} - ${self.max_salary}\n"

def jobToString(job_list):
    string = ""
    for job in job_list:
        string += str(job)
    return string

def split_string_by_length(text):
    chunks = []
    for i in range(0, len(text), 2000):
        chunks.append(text[i:i+2000])
    return chunks
    
def getJobs(keywords):
    url = "https://jsearch.p.rapidapi.com/search"
    job_list = []
    for keyword in keywords:
        querystring = {"query":keyword}
        headers = {
            "X-RapidAPI-Key": "cb531831b6msha0e134819ad53acp138145jsn7b04bacd6faf",
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        
        response_json = response.json()
        for job in response_json["data"]:
            job_list.append(Job(job["employer_logo"], job["employer_name"], job["job_title"], job["job_apply_link"], job["job_is_remote"],job["job_min_salary"], job["job_max_salary"]))
    
    return jobToString(job_list)