import matplotlib.pyplot as plot
import numpy as np
import statistics as stat

import pandas as pd

file=open('TD_HOSPITAL_TRAIN.csv')
patient_data=file.read()

#Getting file input and splitting it by commas
patient_data=patient_data.split('\n')
xtitle= patient_data[0].split(',')
alive_data=[]
death_data=[]
All_data=pd.read_csv('TD_HOSPITAL_TRAIN.csv')
All_data.drop(All_data[All_data['age'] > 100].index, inplace=True)
All_data.drop(All_data[All_data['temperature'] > 45].index, inplace=True)
All_data.drop(All_data[All_data['heart'] <38].index, inplace=True)
All_data.drop(All_data[All_data['bp'] <25].index, inplace=True)

#delete empty space
del patient_data[0]
del patient_data[-1]


##Ignore, this is for debugging
# print(xtitle.index('bloodchem2'))
# error_list=[]

for each_category in range(len(xtitle)):
    string_list=[]
    print(xtitle[each_category])
    for line in patient_data:
        try:
            line=line.split(',')

            if line[-1]=='0.0':
                death_data.append(float(line[each_category]))

            else:
                alive_data.append(float(line[each_category]))

        except:
            if line[each_category] not in string_list:
                string_list.append(line[each_category])

            continue

    if len(death_data)>0:
        print('dead data:',death_data)
        print('median of dead:',stat.median(death_data))
    if len(alive_data)>0:
        print('living data:',alive_data)
        print('median of alive:', stat.median(alive_data))
#
    death_data=[]
    alive_data=[]
    input("Enter to continue")
    print('\n\n\n\n\n\n\n')

#     error_list.append(line[6])
#
# print(len(error_list))
# print(error_list)


#
# #
# for each_category in xtitle:
#     try:
#         All_data.dropna(subset=[each_category],inplace=True)
#         x_data=All_data[each_category]
#         y=All_data['death']
#         plot.scatter(x_data,y, edgecolors='black')
#         plot.title(each_category+' vs alive?')
#         plot.xlabel(each_category)
#         plot.ylabel('alive?')
#         plot.show()
#
#
#
#     except:
#         print('Error for '+each_category)
#         continue
#
# x_data=All_data['disability']
# plot.figure()
# plot.bar(x_data,bins=5,color='green',edgecolor='black')
# plot.title(each_category+" vs dead or alive")
# plot.xlabel(each_category)
# plot.ylabel('frequency')

file.close()
