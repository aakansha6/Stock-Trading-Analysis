# -*- coding: utf-8 -*-

from cmath import sqrt
import os
import csv
import math

ticker='/Users/aakanshasawhney/Desktop/Python/Assignments/week_1_homework/week_1_homework/SBUX.csv'

try:   
    with open(ticker, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    #print(data)

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)

returns = []
prv = 0
return_perc = 0

for row in data:
    if prv != 0:
        return_perc = ((float(row['Adj Close']) - prv) / prv) * 100
    else:
        return_perc = 0
    row['Ret Perc'] = return_perc
    prv = float(row['Adj Close'])
    returns.append(row)
#print("The list of returns is: ", returns)

def mean(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t
    avg = sumOfNumbers / len(num)
    return avg

def standard_dev(result):
    mean = sum(result) / len(result)   # mean
    var  = sum(pow(x-mean,2) for x in result) / len(result)  # variance
    stdeV  = math.sqrt(var)  # standard deviation
    return stdeV

for year in ['2016', '2017', '2018', '2019', '2020']:
    r = []
    rpos = []
    rneg = []
    for row in returns:
        if (row['Year'] == year):
                r.append(row['Ret Perc'])
                print("the mean for year", year, "and day", row["Weekday"], "is:", mean(r) )
        
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                
                else:
                    rneg.append(row['Ret Perc'])
              
    #print("The mean for the list R  for Year", year, "is: ", mean(r))
    #print("The mean for the list R Positive for Year", year, "is: ", mean(rpos))
    #print("The mean for the list R Negative for Year", year, "is: ", mean(rneg))
    #print("The SD for the list R  for Year", year, "is: ", standard_dev(r))
    #print("The SD for the list R Positive for Year", year, "is: ", standard_dev(rpos))
    #print("The SD for the list R Negative for Year", year, "is: ", standard_dev(rneg))

for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        r = []
        rpos = []
        rneg = []
        r_weekday = {"Weekday":[],"Mean R":[],"SD R":[],"|R neg|":[],"Mean R neg":[], "SD R neg":[],"|R pos|":[],"Mean R pos":[], "SD R pos":[]}
        for row in returns:
            if row['Weekday'] == weekday:
                r.append(row['Ret Perc'])
            
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    
                else:
                    rneg.append(row['Ret Perc'])
        r_weekday["Weekday"].append(weekday)
        r_weekday["Mean R"].append(mean(r))
        r_weekday["SD R"].append(standard_dev(r))
        r_weekday["|R neg|"].append(len(rneg))
        r_weekday["Mean R neg"].append(mean(rneg))
        r_weekday["SD R neg"].append(standard_dev(rneg))
        r_weekday["|R pos|"].append(len(rpos))
        r_weekday["Mean R pos"].append(mean(rpos))
        r_weekday["SD R pos"].append(standard_dev(rpos))
        print(r_weekday) 
        #print("The MEAN for the list R  for", weekday, "is: ", mean(r))
        #print("The MEAN for the list R Positive for", weekday, "is: ", mean(rpos))
        #print("The MEAN for the list R Negative for", weekday, "is: ", mean(rneg))
        #print("The SD for the list R  for", weekday, "is: ", standard_dev(r))
        #print("The SD for the list R Positive for", weekday, "is: ", standard_dev(rpos))
        #print("The SD for the list R Negative for", weekday, "is: ", standard_dev(rneg))   


if len(rpos) > len(rneg):
    print("Days with postive R is more")



