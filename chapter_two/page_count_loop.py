# create a list that contains the num of pages
# in each chapter of a book
page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# var for tracking the page counts, starts at 0
total_pages = 0

# for every item in the list, add it to the total page count
for a_number in page_counts:
    total_pages = total_pages + a_number

print(total_pages)

# reset total page count
total_pages = 0

for a_number in page_counts:
    print("Top of loop!")
    print("The current item is:")
    print(a_number)
    total_pages =  total_pages + a_number
    print("The running total is:")
    print(total_pages)
    print("Bottom of loop!")

# Python cannot concat str and int so we use str() method
# to convert int into str type
print("Here's the total pages: " + str(total_pages))

# use the sum() method approach
print("Total pages using sum method: " + str(sum(page_counts)))
