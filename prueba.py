import os
import openpyxl
import pandas as pd
import numpy as np
import datetime

try:
    print("hello")
except:
    print("exception")
finally:
    print("world")

a=['a','b','c']

new=list(a)

print(new)

print(range(3))

m=[]
for i in range(1,3,1):
    m.append(str(i))
print(m)


class create_timestamp_for_dataframe():

    def __init__(self,year,month):

        self.year=year

        self.month=month

    def create_timestamp_array(self):

        if self.month in [1,3,5,7,8,10,12]:

            self.days=31

        elif self.month in [4,6,9,11]:

            self.days=30

        elif self.month in [2]:

            if self.year%4 == 0 and (self.year%100 != 0 or self.year%400==0):

                self.days=29

            else:

                self.days=28

        self.array_timestamp = []

        x=datetime.datetime(self.year,self.month,1,0,0)

        for i in range(self.days*24*4):

            x+=datetime.timedelta(minutes = 15)

            self.array_timestamp.append([x])

        return self.array_timestamp 

timestamps=create_timestamp_for_dataframe(2022,5)
array_timestamp=timestamps.create_timestamp_array()
print(array_timestamp)