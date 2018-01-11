# Read superhero json
import json
from pprint import pprint

with open('superheroes.json') as f:
	data = json.load(f)


# Write CSV header
import csv

with open('heroes.csv', 'w') as f:
	writer = csv.writer(f)
	header = [
		"name",
		"age",
		"secretIdentity",
		"powers",
		"squadName",
		"homeTown",
		"formed",
		"secretBase",
		"active"]
	writer.writerow(header)
	# for each superhero member, write row of data

	members = data['members']
	for m in members:
		name = m['name']
		age = m['age']
		secretIdentity = m['secretIdentity']
		squadName = data['squadName']
		homeTown = data['homeTown']
		formed = data['formed']
		secretBase = data['secretBase']
		active = data['active']

		writer.writerow([name,age,secretIdentity,powers,squadName,homeTown,formed,secretBase,active])
