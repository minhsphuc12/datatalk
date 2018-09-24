# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:34:58 2018

@author: phucnm
"""


from urllib.request import urlopen


#url = 'https://github.com/maiing/datatalk/blob/master/diem_thi_THPT_2018/THPT%202018%20Ha%20Giang.csv'
path = 'C://Users//phucn//Documents//git//datatalk//datatalk//diem_thi_THPT_2018//THPT_2018_Ha_Giang.csv'


## open url with urlopen
#response = urlopen(url, 'rt')
#
## open url with requests
#import requests
#
#r = requests.get(url)
#response = r.iter_lines()
#
## open url with open
#import codecs
##ifile = open(url, 'rb')
#
## read with csv
#import csv
#cr = csv.reader(response)
#cr2 = codecs.iterdecode(cr, 'utf-8')
#
#cr = csv.reader(response, delimiter = ',')
#
#for row in cr2:
#    print(row)
### issue is to deal with csv.reader object

# read with pandas
import pandas as pd
data = pd.read_csv(path)

data.head()
list(data)
list(data.columns.values)
# how many row in this set of Ha Giang
data['ID'].count()

## descriptive analysis
# highest math score
data['Math'].max()
# highest literature score --------
data['Viet'].max()
print('Highest math score is {}'.format(data['Math'].max()))
print('Highest literature score is {}'.format(data['Viet'].max()))
print('Highest english score is {}'.format(data['English'].max()))
print('Highest physics score is {}'.format(data['Physics'].max()))
print('Highest chemistry score is {}'.format(data['Chemistry'].max()))
print('Highest biology score is {}'.format(data['Biology'].max()))
print('Highest history score is {}'.format(data['History'].max()))
print('Highest geography score is {}'.format(data['Geography'].max()))

subjects = ['Math', 'Viet', 'English', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography']
subjects = list(data)[2:10]
for subject in subjects:
    print('Highest {} score is {}'.format(subject, data[subject].max()))
    print('Lowest {} score is {}'.format(subject, data[subject].min()))
    print('Average {} score is {}'.format(subject, round(data[subject].mean(),1)))
    print('Bottom of top 20% of {} score is {}'.format(subject, round(data[subject].quantile(0.8),1)))
    print('Top of bottom 20% of {} score is {}'.format(subject, round(data[subject].quantile(0.2),1)))
    print('\n')

for subject in subjects:
    print(data[subject].describe().transpose())
    print('\n')

## turn series of summary into a data frame --------
a = data['Math'].describe().to_frame().transpose()
b = data['Viet'].describe().to_frame().transpose()
c = pd.concat([a, b], axis = 0)
d = a.append(b)

all_subject_sum = [data[subject].describe().to_frame().transpose() for subject in subjects]
all_subject_sum_df = pd.concat(all_subject_sum, axis = 0)
all_subject_sum_df 
# extend it to prefixed subject combinations
subjects= list(data)[2:]
# beautify the result by rounding out number
all_subject_sum = [data[subject].describe().to_frame().transpose().round(1) for subject in subjects]
all_subject_sum_df = pd.concat(all_subject_sum, axis = 0)
all_subject_sum_df 


