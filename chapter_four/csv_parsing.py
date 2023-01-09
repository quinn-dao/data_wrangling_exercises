# An ex of reading data from a .csv file with Python
# The source data was sampled from the Citi Bike system data:
# https://drive.google.com/file/d/17b461NhSjf_akFWvjgNXQfqgh9iFxCu_/

# import the csv library
import csv

source_file = open("202009CitibikeTripdataExample.csv","r")

citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)

# The next() function returns the next item in an iterator
# Syntax: next(iterable, default)
# Default value is optional, return if the iterable has reached to its end.
for i in range(0,5):
    print(next(citibike_reader))
