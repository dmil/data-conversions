# Read superhero json
import json
from pprint import pprint

with open('superheroes.json') as f:
    data = json.load(f)

all_powers = []

# Get members
members = data['members']
# Loop over the members
for m in members:
	powers = m['powers']

	for p in powers:
		# for each member, get their powers
		all_powers.append(p)



# remove duplicates
unique_powers = list(set(powers))
print unique_powers
