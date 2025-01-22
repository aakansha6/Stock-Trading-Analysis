# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import csv

ticker='SBUX'
input_dir = r'/Users/aakanshasawhney/Desktop/Python/Assignments/week_1_homework/week_1_homework'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.readlines()
    print('opened file for ticker: ', ticker)
  
    with open('SBUX.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)

    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)













