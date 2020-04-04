"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_time = defaultdict(int)
for call in calls:
    if call[0] != call[1]:
        call_time[call[0]] += int(call[-1])
        call_time[call[1]] += int(call[-1])
    else:
        call_time[call[0]] += int(call[-1])
max_tel_num = ''
max_total_time = 0
for tel_num, t in call_time.items():
    if t > max_total_time:
        max_total_time = t
        max_tel_num = tel_num
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_tel_num,
                                                                                          max_total_time))

