"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tel_nums = set([_item[0] for _item in texts] +
               [_item[1] for _item in texts] +
               [_item[0] for _item in calls] +
               [_item[1] for _item in calls])
print("There are {} different telephone numbers in the records".format(len(tel_nums)))

