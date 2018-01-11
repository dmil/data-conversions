import csv
from pprint import pprint

with open('veggies.tsv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

pprint(rows)