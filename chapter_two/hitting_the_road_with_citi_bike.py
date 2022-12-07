# Q: How many Citi Bike rides each day
#are taken by "member" vs. "casual customers"?

# A: Choose a single day to examine
# the dataset used in this exercise was from the original
# Citi Bike system data found at: https://s3.amazonaws.com/tripdata/index.html
# filename: 202210-citibike-tripdata.csv.zip

# program Outline:
# 1. read in the data file: 202210-citibike-tripdata.csv
# 2. create variables to count: member, casual, and other
# 3. for each row:
#   a. If the user type is "member", add 1 to "member_count"
#   b. If the user type is "casual", add 1 to "casual_count"
#   c. Else, add 1 to "other_count"
# 4. print out results

# import the 'csv' library
import csv

# open the '202210-citibike-tripdata.csv' file in read mode
# this file should be in the sme folder as our Python script
source_file = open("202210-citibike-tripdata.csv","r")

#
citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)

member_count = 0
casual_count = 0
other_count = 0

for a_row in citibike_reader:
    if a_row["member_casual"] == "member":
        member_count = member_count + 1

    elif a_row["member_casual"] == "casual":
        casual_count = casual_count + 1

    else:
        other_count = other_count + 1

print("Number of members:" + str(member_count))
print("Number of casuals:" + str(casual_count))
print("Number of other users:" + str(other_count))
