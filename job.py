from bs4 import BeautifulSoup
import requests

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
print('enter a skill you are familiar with')
good_skill = input('>')
html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={good_skill}&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_= 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'More Info: {more_info}')