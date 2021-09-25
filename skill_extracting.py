#!/usr/bin/env python
# -*- coding: UTF-8 -*-

''' 
@Author  ：Yufeng (Maple) FENG
@Date    ：2021-09-25
'''

import pandas as pd
import re

jobs = pd.read_csv('skill_analysis.csv')
jobs.head(10)

def preprocess(jd):
    # Removing garbled characters and whitespaces
    jd = jd.replace("?", "").replace("\r\n\r\n", " ").replace("\r\n", " ").replace("-", "")
    # Changing job descriptions into lower cases for further analysis
    jd = jd.lower()
    return jd

# Applying preprocessing prodecures to data
jobs['job_description'] = jobs['job_description'].apply(lambda jd: preprocess(jd))

# Defining the regular expressions to recognize different groups of skills
programming = re.compile(r'.*\s(programming|python|r\s|r\,|java|c\s|c\,|c\+\+|scala).*')
statistics = re.compile(r'.*\s(statistics|statistical).*')
machine_learning = re.compile(r'.*\s(machine\s*learning|keras|tensorflow|pytorch).*')
cloud = re.compile(r'.*\s(cloud|aws|azure|google\s+cloud).*')
big_data = re.compile(r'.*\s+(big\s+data|hadoop|spark|kubernetes).*')
relational_db = re.compile(r'.*\s(sql|mysql|oracle).*')
nlp = re.compile(r'.*\s(nlp|natural\s+language|nltk|text\s+analytics).*')
analysis_softwares = re.compile(r'.*\s(excel|tableau|power\s+bi|sas\,|sas\s|jmp|spss).*')

# Using the regular expressions to match the job descriptions
jobs['programming'] = jobs['job_description'].apply(lambda jd: 1 if programming.match(jd) else 0)
jobs['statistics'] = jobs['job_description'].apply(lambda jd: 1 if statistics.match(jd) else 0)
jobs['machine_learning'] = jobs['job_description'].apply(lambda jd: 1 if machine_learning.match(jd) else 0)
jobs['cloud'] = jobs['job_description'].apply(lambda jd: 1 if cloud.match(jd) else 0)
jobs['big_data'] = jobs['job_description'].apply(lambda jd: 1 if big_data.match(jd) else 0)
jobs['relational_db'] = jobs['job_description'].apply(lambda jd: 1 if relational_db.match(jd) else 0)
jobs['nlp'] = jobs['job_description'].apply(lambda jd: 1 if nlp.match(jd) else 0)
jobs['analysis_softwares'] = jobs['job_description'].apply(lambda jd: 1 if analysis_softwares.match(jd) else 0)

# Summarizing the frequency of each skill groups
jobs.sum(axis=0)

# Exporting as a csv file
jobs.to_csv('extracted_skills.csv', index=False)