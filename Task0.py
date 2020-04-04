"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_rec = texts[0]
    print("First record of texts, {} texts {} at time {}".format(*first_rec))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_rec = calls[-1]
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*last_rec))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

