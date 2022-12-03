import datetime

'''
x = datetime.datetime(2020, 5, 1, 0, 45) 

y = datetime.timedelta(minutes = 15)

z = x + y

print(x)

print(y)

print(z)


def Days_Calculation(year,month):
    if month in [1,3,5,7,8,10,12]:
        days=31
    elif month in [4,6,9,11]:
        days=30
    elif month in [2]:
        if year%4 == 0 and (year%100 != 0 or year%400==0):
            days=29
        else:
            days=28
    return days

array_timestamp = []
x=datetime.datetime(2022,5,1,0,0)
for i in range(2976):
    x+=datetime.timedelta(minutes = 15)
    array_timestamp.append(x)
print(array_timestamp)
'''

def create_timestamp_array(year,month):

    if month in [1,3,5,7,8,10,12]:

        days=31

    elif month in [4,6,9,11]:

        days=30

    elif month in [2]:

        if year%4 == 0 and (year%100 != 0 or year%400==0):

            days=29

        else:

            days=28

    array_timestamp = []

    x=datetime.datetime(year,month,1,0,0)

    for i in range(days*24*4):

        x+=datetime.timedelta(minutes = 15)

        array_timestamp.append(x)

    return array_timestamp

A=create_timestamp_array(2020,4)

print(A)








