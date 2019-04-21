#! /usr/bin/python3
import sys, os
import csv

print('welcome to my data cleaning script')
myfile = open('/home/johanes/Pycharm_Github/JCL_clients_tagging.csv')

reader = csv.reader(myfile, delimiter = ';')

data = list(reader)

outfile = open ('/home/johanes/Pycharm_Github/JCL_clients_taggingCLEAN.csv', 'w')

writer = csv.writer(outfile, delimiter = ';')
for item in data:
    fields = item
    if fields:
       fields[0] = item[0].title()
       print(fields[0])
       writer.writerow(fields)