import csv
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path):
	with open("people.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)


def append_data(file_path, name, title, city, state, region):
	fieldnames = ['name', 'title', 'city', 'state', 'region']
	next_id = get_length(file_path)
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({
			"name":  name,
			"title": title,
			"city": city,
			"state": state,
			"region": region,
		})


append_data("people.csv", "John", "Dr", "New York", "NY", "")


filename = "people.csv"
temp_file = NamedTemporaryFile(delete=False)

def data_edit(state=None, region=None):
	with open(filename, "rb") as csvfile, temp_file:
		reader = csv.DictReader(csvfile)
		fieldnames = ['name', 'title', 'city', 'state', 'region']
		writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			if int(row['state']) == ["WI"]:
				row['region'] = "Midwest"
				print(row)
			elif int(row['state']) == ["CO"]:
				row['region'] = "West"
				print(row)
			elif int(row['state']) == ["NY"]:
				row['region'] = "Northeast"
				print(row)
			else:
				pass
			writer.writerow(row)
		return True


shutil.move(temp_file.name, filename)
