# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:48:35 2018

@author: Κωστας

requires the facebook data to be downloaded in .json format
outputs 3 csv files
a csv file with the number of messages for each conversation (including group chats)
a csv file with the the year, month, day, and hour for each message send of receved (no reactions)
a csv file with the the year, month, day, and hour where friends added

enter the path of the unzipped foleder to the variable folder_path

"""
import os
import json
import datetime
import calendar
import csv


folder_path='......'
        
    
path=folder_path+'\\messages'
name_list=[]

for root,dirs,files in os.walk(path):
    name=root.split('\\')
    if len(name)>=4:
        name_list.append(name[3])
    
name_list=list(set(name_list))  # remove duplicates
name_list.pop(name_list.index('stickers_used'))
name_list.sort()
print(len(name_list),'conversations found!')

year=[]
month=[]
day=[]
week_day=[]
hour=[]
mine=[]
tot_msg=[]
my_msg=[]
name_list3=[]
# the legnth of the lists year, month, day, week_day, hour are the total number of messages sent/receved
# the lenght of the lists tot_msg and my_msg are the total number of conversations found

for cnv_name in name_list:
#    print('Now prossesing conversation',cnv_name)
    
    json_file_path=path+'\\'+cnv_name+'\\message.json'
    jfile=open(json_file_path,'r',encoding='utf-8',errors='ignore')
    dataz=json.load(jfile)
    jfile.close
    
#    try:
#        if len(dataz['title'])>=1:
#            name_list3.append(dataz['title'])
#        else:
#            name_list3.append(cnv_name)
#    except KeyError:
#        name_list3.append(dataz['thread_path'][0])
    
    
    
    n=(len(dataz['messages']))  # total messages
    mymsg=0
    tot_msg.append(n)
    my_msg.append(n)    
    #για οσους εχουν σβησει το φβ δεν θα φαινονται τα μνμ τους...δλδ θα φαινονεται σαν να μιλουσα μονος

    
    for i in range(0,n):
        
        try:
            if dataz['messages'][i]['sender_name']=='Konstantinos Konstantinidis':
                mymsg +=1
                mine.append('user')
            mine.append('others')
        
            
            ymdh=datetime.datetime.fromtimestamp(dataz['messages'][i]['timestamp'])
            year.append(ymdh.year)
#            month.append(ymdh.month)
            if ymdh.month==1:
                month.append('January')
            elif ymdh.month==2:
                month.append('February')
            elif ymdh.month==3:
                month.append('March')
            elif ymdh.month==4:
                month.append('April')
            elif ymdh.month==5:
                month.append('May')
            elif ymdh.month==6:
                month.append('June')
            elif ymdh.month==7:
                month.append('July')
            elif ymdh.month==8:
                month.append('August')
            elif ymdh.month==9:
                month.append('September')
            elif ymdh.month==10:
                month.append('October')
            elif ymdh.month==11:
                month.append('November')
            elif ymdh.month==12:
                month.append('December')
            else:
                print('error in months')
            day.append(ymdh.day)
            day_of_the_week=calendar.weekday(ymdh.year,ymdh.month,ymdh.day)
            if day_of_the_week==0:
                week_day.append("Monday")
            elif day_of_the_week==1:
                week_day.append("Tuesday")
            elif day_of_the_week==2:
                week_day.append("Wednesday")
            elif day_of_the_week==3:
                week_day.append("Thursday")
            elif day_of_the_week==4:
                week_day.append("Friday")
            elif day_of_the_week==5:
                week_day.append("Saturday")
            elif day_of_the_week==6:
                week_day.append("Sunday")
            else:
                print("error in weekdays")
            hour.append(ymdh.hour)
            
            my_msg.pop()
            my_msg.append(mymsg)
            
            
        except KeyError:
            break            
name_list2=[]
for i in range(0,len(name_list)):
#    print(name_list[i])
    name_list2.append(name_list[i].split('_')[0])


final_msg=[['conversation name','total messages','my messages']]
for row in range(1,len(my_msg)+1):
    final_msg.append([name_list2[row-1],tot_msg[row-1],my_msg[row-1]])
      
with open('fb_report_msg.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(final_msg)
print('number of messages sent/receved report generated')

final_time=[['year','month','weekday','hour','mine']]
for row in range(1,len(year)+1):
    final_time.append([year[row-1],month[row-1],week_day[row-1],hour[row-1],mine[row-1]])

with open('fb_report_msg_time.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(final_time)
print('time of messages report generated')



#   friend analysis

path=folder_path+'\\friends\\friends.json'

jfile=open(path,'r',encoding='utf-8',errors='ignore')
datazz=json.load(jfile)
jfile.close

year=[]
month=[]
day=[]
week_day=[]
hour=[]

n=len(datazz['friends'])
for i in range(0,n):
    ymdh=datetime.datetime.fromtimestamp(datazz['friends'][i]['timestamp'])
    year.append(ymdh.year)
    
    if ymdh.month==1:
        month.append('January')
    elif ymdh.month==2:
        month.append('February')
    elif ymdh.month==3:
        month.append('March')
    elif ymdh.month==4:
        month.append('April')
    elif ymdh.month==5:
        month.append('May')
    elif ymdh.month==6:
        month.append('June')
    elif ymdh.month==7:
        month.append('July')
    elif ymdh.month==8:
        month.append('August')
    elif ymdh.month==9:
        month.append('September')
    elif ymdh.month==10:
        month.append('October')
    elif ymdh.month==11:
        month.append('November')
    elif ymdh.month==12:
        month.append('December')
    else:
        print('error in months')
        
    day.append(ymdh.day)
    day_of_the_week=calendar.weekday(ymdh.year,ymdh.month,ymdh.day)
    if day_of_the_week==0:
        week_day.append("Monday")
    elif day_of_the_week==1:
        week_day.append("Tuesday")
    elif day_of_the_week==2:
        week_day.append("Wednesday")
    elif day_of_the_week==3:
        week_day.append("Thursday")
    elif day_of_the_week==4:
        week_day.append("Friday")
    elif day_of_the_week==5:
        week_day.append("Saturday")
    elif day_of_the_week==6:
        week_day.append("Sunday")
    else:
        print("error in weekdays")
    hour.append(ymdh.hour)
        
final_time=[['year','month','weekday','hour']]
for row in range(1,len(year)+1):
    final_time.append([year[row-1],month[row-1],week_day[row-1],hour[row-1]])

with open('fb_report_friend_time.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(final_time)
print('time of friends made report generated')
