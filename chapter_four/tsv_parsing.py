# An ex of reading data from a .tsv file with Python
# The source data was downloaded as a .tsv file:
# from Jed Shugerman's Google Sheet on prosecutor politicians:
# https://docs.google.com/spreadsheets/d/1E6Z-jZWbrKmit_4lG36oyQ658Ta6Mh25HCOBaz7YVrA

# import the csv library
import csv

tsv_source_file = open("Shugerman Research on Rise of Prosecutor Politicians - Supreme Court Justices.tsv","r")

# delimiter can be specified/substituted
politicians_reader = csv.DictReader(tsv_source_file, delimiter = '\t')

print(politicians_reader.fieldnames)

print(next(politicians_reader))
