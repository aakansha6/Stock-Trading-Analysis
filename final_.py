# -*- coding: utf-8 -*-
"""
Aakansha Sawhney

Description of Problem: Python has been used to analyze the distribution of returns 
and a number of trading strategies on two datasets - Starbucks and SPY.
Starbucks is the stock chosen by me and the SPY has been provided for comparison.
The timestamp is from 2016-2020
"""
from calendar import week
from cmath import sqrt
import os
import csv
import math
from xml.dom.domreg import well_known_implementations
#import matplotlib.pyplot as plt

ticker='/Users/aakanshasawhney/Desktop/Python/Assignments/week_1_homework/akansha3_hw_1/SBUX.csv'
new_ticker='/Users/aakanshasawhney/Desktop/Python/Assignments/week_1_homework/akansha3_hw_1/SPY.csv'

try:   
    with open(ticker, newline='') as starbucks_file:
        reader = csv.DictReader(starbucks_file)
        data = list(reader)
    #print(data)

    with open(new_ticker,newline='') as spy_file:
        spy_reader = csv.DictReader(spy_file)
        spy_data = list(spy_reader)

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)

### Calculating Overall R, R+ and R- where Return percentage for Starbucks
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
#print("The list of returns for Starbuck is: ", returns)

### Calculating Overall R, R+ and R- where Return percentage for SPY
spy_returns = []
spy_prv = 0
spy_return_perc = 0

for row in spy_data:
    if spy_prv != 0:
        spy_return_perc = ((float(row['Adj Close']) - spy_prv) / spy_prv) * 100
    else:
        spy_return_perc = 0
    row['Ret Perc'] = spy_return_perc
    spy_prv = float(row['Adj Close'])
    spy_returns.append(row)
#print("The list of returns for SPY is: ", returns)

### Calculating Mean
def mean(num):
    avg=0
    if len(num) != 0:
         avg = sum(num) / len(num)
         return avg
    else:
        return ("not possible, fix your code")

    
### Calculating Standard Deviation
def standard_dev(result):
    mean = sum(result) / len(result)   # mean
    var  = sum(pow(x-mean,2) for x in result) / len(result)  # variance
    stdeV  = math.sqrt(var)  # standard deviation
    return stdeV




### Calculating the Returns Year Wise for Starbucks
for year in ['2016', '2017', '2018', '2019', '2020']:
    r = []
    rpos = []
    rneg = []
    max_rpos = []
    year_r = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    year_rpos = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    year_rneg = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    for row in returns:
        if (row['Year'] == year):
                r.append(row['Ret Perc'])
                year_r[row['Year']].append(row['Ret Perc'])
        
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    year_rpos[row['Year']].append(row['Ret Perc'])
                
                else:
                    rneg.append(row['Ret Perc'])
                    year_rneg[row['Year']].append(row['Ret Perc'])
    #print("{0}:--- R :{1}: --- R Pos :{2}: --- R Neg :{3}".format(year,mean(year_r[year]), mean(year_rpos[year]),mean(year_rneg[year])))
    max_rpos.append(mean(year_rpos[year]))
    #print("the mean (R) for year", year, "is:", mean(r))                
    #print("the mean (R+) for year", year, "is:", mean(rpos))
    #print("the mean (R-) for year", year, "is:", mean(rneg))
maximum_rpos=max(max_rpos)

### Calculating the Returns Year Wise for SPY
for year in ['2016', '2017', '2018', '2019', '2020']:
    r = []
    rpos = []
    rneg = []
    spy_max_rpos = []
    year_r = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    year_rpos = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    year_rneg = {"2016": [], "2017": [], "2018": [], "2019": [], "2020": []}
    for row in spy_returns:
        if (row['Year'] == year):
                r.append(row['Ret Perc'])
                year_r[row['Year']].append(row['Ret Perc'])
        
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    year_rpos[row['Year']].append(row['Ret Perc'])
                
                else:
                    rneg.append(row['Ret Perc'])
                    year_rneg[row['Year']].append(row['Ret Perc'])
    #print("{0}:--- R :{1}: --- R Pos :{2}: --- R Neg :{3}".format(year,mean(year_r[year]), mean(year_rpos[year]),mean(year_rneg[year])))
    spy_max_rpos.append(mean(year_rpos[year]))
spy_maximum_rpos=max(spy_max_rpos)

print("\n")
print("Question 1. Part 1 & 2.")
print("---------- 5 Tables Summary ----------")
print("\n")
for year in ['2016', '2017', '2018', '2019', '2020']:
    r = []
    rpos = []
    rneg = []
    max_rneg_weekdays = []
    max_rpos_weekdays = []
    r_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    rpos_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    rneg_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for row in returns:
        if (row['Year'] == year):
                r.append(row['Ret Perc'])
                r_weekdays[row['Weekday']].append(row['Ret Perc'])
        
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    rpos_weekdays[row['Weekday']].append(row['Ret Perc'])
                
                else:
                    rneg.append(row['Ret Perc'])
                    rneg_weekdays[row['Weekday']].append(row['Ret Perc'])
                
    print("------ Calculating Table for the year:",year," ------")
    for weekday in r_weekdays:
        print("{0}: --- Mean R: {1} --- SD R: {2} --- |R neg|: {3} --- Mean R neg: {4} --- SD R neg: {5} --- |R pos|: {6} --- Mean R pos: {7} --- SD R pos: {8}".format(weekday, 
        mean(r_weekdays[weekday]), standard_dev(r_weekdays[weekday]), 
        len(rneg_weekdays[weekday]), mean(rneg_weekdays[weekday]), standard_dev(rneg_weekdays[weekday]),
        len(rpos_weekdays[weekday]), mean(rpos_weekdays[weekday]), standard_dev(rpos_weekdays[weekday])))
        print("\n")
        #max_rpos_weekdays.append(standard_dev(rpos_weekdays[weekday]))
#max_rpos_weekday = max(max_rpos_weekdays)
#print(max_rpos_weekday)

print("\n")
print("Question 1 Part 3")
print("Question: Are there more days with negative or non-negative returns?")
print("\n")
if len(rpos) > len(rneg):
    print("Solution: Days with postive R is more")
else:
    print("Solution: Days with Negative R is more")

print("\n")
print("------ Question 2 ------")
print("Ques 2. Part 1: are there any patterns across days of the week?")
print("Observation: The Standard Deviation for R, R- and R+ has increased accross all the weeks in the Year 2020 in comparison to all the previous 4 years.")

print("Ques 2. Part 2: are there any patterns across different years for the same day of the week?")
print("Observation: No, there was no pattern observed here.")

print("Ques 2. Part 3: what are the best and worst days of the week to be invested for each year.")

print("Observation: for 2016, best - Friday and worst - tuesday | for 2017, best - Friday and worst - tuesday | for 2018, best - Friday and worst - tuesday | for 2019, best - Friday and worst - Monday | for 2020, best - Thursday and worst - tuesday")

print("Ques 2. Part 4: do these days change from year to year for your stock")
print("Observation: The best day remains same from 2016-2019 and changes only for 2020. Whereas the worst day remains same for 2016-2018 and 2020 but changes only for 2019.")
print("\n")

print("------ Question 3 ------")
### computing aggregated one table across all 5 years for Starbucks Data
print("\n")
print("----Aggregated data across all 5 years for Starbucks Stocks----")
print("\n")
max_sd_rpos = []
min_sd_rneg = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for weekday in weekdays:
        r = []
        rpos = []
        rneg = []
        r_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        rpos_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        rneg_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        for row in returns:
            if row['Weekday'] == weekday:
                r.append(row['Ret Perc'])
                r_weekdays[row['Weekday']].append(row['Ret Perc'])
            
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    rpos_weekdays[row['Weekday']].append(row['Ret Perc'])
                else:
                    rneg.append(row['Ret Perc'])
                    rneg_weekdays[row['Weekday']].append(row['Ret Perc'])

        print("{0}: --- Mean R: {1} --- SD R: {2} --- |R neg|: {3} --- Mean R neg: {4} --- SD R neg: {5} --- |R pos|: {6} --- Mean R pos: {7} --- SD R pos: {8}".format(weekday, mean(r_weekdays[weekday]), standard_dev(r_weekdays[weekday]), len(rneg_weekdays[weekday]), mean(rneg_weekdays[weekday]), standard_dev(rneg_weekdays[weekday]),len(rpos_weekdays[weekday]), mean(rpos_weekdays[weekday]), standard_dev(rpos_weekdays[weekday])))
        print("\n")
        max_sd_rpos.append(standard_dev(rpos_weekdays[weekday]))
        min_sd_rneg.append(standard_dev(rneg_weekdays[weekday]))

best_star = weekdays[max_sd_rpos.index(max(max_sd_rpos))]
worst_star = weekdays[min_sd_rneg.index(min(min_sd_rneg))]
print("Question 3. Part 1. what is the best and worst days of the week for each?")
print("Best Day of the Week", best_star,  "for Starbucks Stock:",max(max_sd_rpos))
print("Worst Day of the Week", worst_star,  " for Starbucks Stock:",min(min_sd_rneg))

 ### computing aggregated one table across all 5 years for SPY Data
print("\n")
print("----Aggregated data across all 5 years for SPY Stocks----")
print("\n")   
max_sd_rpos = []
min_sd_rneg = []
for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        r = []
        rpos = []
        rneg = []
        r_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        rpos_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        rneg_weekdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        for row in spy_returns:
            if row['Weekday'] == weekday:
                r.append(row['Ret Perc'])
                r_weekdays[row['Weekday']].append(row['Ret Perc'])
            
                if row['Ret Perc'] >= 0:
                    rpos.append(row['Ret Perc'])
                    rpos_weekdays[row['Weekday']].append(row['Ret Perc'])
                else:
                    rneg.append(row['Ret Perc'])
                    rneg_weekdays[row['Weekday']].append(row['Ret Perc'])

        print("{0}: --- Mean R: {1} --- SD R: {2} --- |R neg|: {3} --- Mean R neg: {4} --- SD R neg: {5} --- |R pos|: {6} --- Mean R pos: {7} --- SD R pos: {8}".format(weekday, mean(r_weekdays[weekday]), standard_dev(r_weekdays[weekday]), len(rneg_weekdays[weekday]), mean(rneg_weekdays[weekday]), standard_dev(rneg_weekdays[weekday]),len(rpos_weekdays[weekday]), mean(rpos_weekdays[weekday]), standard_dev(rpos_weekdays[weekday])))
        print("\n")
        max_sd_rpos.append(standard_dev(rpos_weekdays[weekday]))
        min_sd_rneg.append(standard_dev(rneg_weekdays[weekday]))
        
       
        
#print(max_sd_rpos)
#print(min_sd_rneg)
print("Question 3. Part 1. what is the best and worst days of the week for each?")
best_spy = weekdays[max_sd_rpos.index(max(max_sd_rpos))]
worst_spy = weekdays[min_sd_rneg.index(min(min_sd_rneg))]
print("Best Day of the Week", best_spy,  "for SPY Stock:",max(max_sd_rpos))
print("Worst Day of the Week", worst_spy,  " for SPY Stock:",min(min_sd_rneg))

print("\nQuestion 3. Part 2.")
if best_star == best_spy:
    print("Same Best day for both ")
else:
    print("Different Best day for both ")

if worst_star == worst_spy:
    print("Same Worst day for both ")
else:
    print("Different Worst day for both ")


print("\n")
print("\n")
### Question 4. Part 1 ###
invested = 100
print("Money invested:$ ",invested)
print("\n")
print("Question 4. Part 1. How much much money will you have on the last trading day of 2020 for Starbucks:")
str_max_return = maximum_rpos*invested
print("Solution: The maximum return by end of 2020 would be:", str_max_return)
print("\n")
### Question 4. Part 2 ###
invested = 100
print("Question 4. Part 2. How much much money will you have on the last trading day of 2020 for SPY:")
spy_max_return = spy_maximum_rpos*invested
print("Solution: The maximum return by end of 2020 would be:", spy_max_return)
print("\n")

### Question 5. Part 1 ###
print("\n")
print("\n")
print("Question 5 Part 1")
print("\n")
### Starbuck ###
num_of_records = len(data)
open_price = float(data[0]['Open'])
print("Open Price for Starbucks:$",open_price)
close_price = float(data[num_of_records - 1]['Close'])
print("Close Price for Starbucks:$",close_price)
percent_change = float((close_price / open_price - 1) * 100)
final_money = invested * (percent_change / 100 + 1)
print("Money on the last day of trading for Starbucks is:$", final_money)

### SPY ###
spy_num_of_records = len(spy_data)
spy_open_price = float(spy_data[0]['Open'])
print("Open Price for SPY:$",spy_open_price)
spy_close_price = float(spy_data[spy_num_of_records - 1]['Close'])
print("Close Price  for SPY:$",spy_close_price)
spy_percent_change = float((spy_close_price / spy_open_price - 1) * 100)
spy_final_money = invested * (spy_percent_change / 100 + 1)
print("Money on the last day of trading for SPY is:$", spy_final_money)

print("\n")
print("Question 5 Part 2")
print("how do these results compare with results obtained in question 4?")
print("Solutions:")
if str_max_return > final_money:
    print("the intra-day trading return is better than long term trading for Starbucks")
else:
    print("the long-term trading return is better than intra-day trading for Starbucks")

if spy_max_return > spy_final_money:
    print("the intra-day trading return is better than long term trading for SPY")
else:
    print("the long-term trading return is better than intra-day trading for SPY")


print("\n")
print("\n")
print("Question 6")
print("\n")

print("We gain more for Starbucks by missing worst days")
print("We gain more for SPY by missing worst days as well")
print("The maximum return increased for Starbucks and didn't change much for SPY")
new_rpos = list()
sort_rpos = rpos.sort(reverse=True)
best_rpos = sort_rpos[0:9]
for item1, item2 in rpos,best_rpos:
    new_rpos.append(rpos - best_rpos)
overall_profit = list()
overall_profit = sum(rneg) + sum(new_rpos)
print("New Overall Profit without 10 best:", overall_profit)


n = 10
sort_rpos = rpos.sort(reverse=True)
new_rpos = sort_rpos[n:]
print(new_rpos)
sum_rneg = float(sum(rneg))
sum_new_rpos = float(sum(new_rpos))
overall_profit = float(sum_rneg+ sum_new_rpos)
print("New Overall Profit without 10 best:", overall_profit)

print("We gain more for Starbucks by missing worst days")
print("We gain more for SPY by missing worst days as well")
print("The maximum return increased for Starbucks and didn't change much for SPY")
