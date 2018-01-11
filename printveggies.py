vegetables = [
 {'name': 'eggplant'},
 {'name': 'tomato'},
 {'name': 'corn'},
 {'name': 'potato'},
 {'name': 'corn'},
 {'name': 'corn'},
 {'name': 'kale'}
]

# Write header file to csv
import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])

	# Loop through each vegetable
	for veggie in vegetables:
		# for each vegtable write a row to the csv
		name = veggie['name']
		length = len(name)
		writer.writerow([name, length])
