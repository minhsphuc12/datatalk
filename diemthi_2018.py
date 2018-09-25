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
import numpy as np
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



path_hagiang = 'C://Users//phucn//Documents//git//datatalk//datatalk//diem_thi_THPT_2018//THPT_2018_Ha_Giang.csv'
path_toanquoc = 'C://Users//phucn//Documents//git//datatalk//datatalk//diem_thi_THPT_2018//THPT_2018_Quoc_gia.csv'

score_hagiang = pd.read_csv(path_hagiang)
score_toanquoc = pd.read_csv(path_toanquoc)
score_hagiang.head()
score_toanquoc.head()

# check if distrubtion of Ha Giang different statistically with other places

# make a function to easily apply different times
def fast_summary_score(data):    
    subjects = list(data)[2:10]
    all_subject_sum = [data[subject].describe().to_frame().transpose().round(1) for subject in subjects]
    all_subject_sum_df = pd.concat(all_subject_sum, axis = 0)
    return(all_subject_sum_df)

fast_hagiang = fast_summary_score(score_hagiang)
fast_toanquoc = fast_summary_score(score_toanquoc)

fast_hagiang['mean'] - fast_toanquoc['mean']
fast_hagiang['75%'] - fast_toanquoc['75%']

# analyze via viasualization
import matplotlib.pyplot as plt
weights_hagiang = np.ones_like(score_hagiang['Math'].dropna())/float(len(score_hagiang['Math'].dropna()))
n1, a1, a2 = plt.hist(x = score_hagiang['Math'][~np.isnan(score_hagiang['Math'])], bins = 50, color = 'firebrick',
                            alpha = 0.7, rwidth = 0.85, range = [0,10], weights = weights_hagiang)
n1
bins
patches
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Value', size = 40)
plt.ylabel('Frequency', size = 40)
plt.text(23,45, r'$\mu=15, b= 3$')
maxfreq = n.max()

#plt.ylim(ymax = np.ceil(maxfreq/10) * 10 if maxfreq % 10 else maxfreq +10)


weights_toanquoc = np.ones_like(score_toanquoc['Math'].dropna())/float(len(score_toanquoc['Math'].dropna()))
n, bins, patches = plt.hist(x = score_toanquoc['Math'][~np.isnan(score_toanquoc['Math'])], bins = 50, color = 'royalblue'
                            , alpha = 0.7, rwidth = 0.85, range = [0,10], weights = weights_toanquoc)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Value', size = 40)
plt.ylabel('Frequency', size = 40)
plt.text(23,45, r'$\mu=15, b= 3$')
maxfreq = n.max()
#plt.ylim(ymax = np.ceil(maxfreq/10) * 10 if maxfreq % 10 else maxfreq +10)


line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')














