# create a list that contains the num of pages
# in each chapter of a book
page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# var for tracking the page counts, starts at 0
total_pages = 0

# var for tracking the chapters with more than 30 pages, starts at 0
over_30 = 0

# var for tracking the chapters with fewer than OR EXACTLY 30 pages
# starts at 0
under_30 = 0

for a_number in page_counts:
    total_pages = total_pages + a_number

    # check if a chapter has more than 30 pages
    if a_number >30:
        over_30 = over_30 + 1
    # check if a chapter has fewer than 30 pages
    else:
        under_30 = under_30 + 1

# print out various results
print("Total pages: "+str(total_pages))
print("Number of chapters more than 30 pages: "+str(over_30))
print("Number of chapters fewer than or exactly 30 pages: "+str(under_30))

# let us  build a custom func called count_pages()
def count_pages(page_count_list):
    # var for tracking the page counts, starts at 0
    total_pages = 0

    # var for tracking the chapters with more than 30 pages, starts at 0
    over_30 = 0

    # var for tracking the chapters with fewer than OR EXACTLY 30 pages
    # starts at 0
    under_30 = 0

    for a_number in page_counts:
        total_pages = total_pages + a_number

        # check if a chapter has more than 30 pages
        if a_number >30:
            over_30 = over_30 + 1
        # check if a chapter has fewer than 30 pages
        else:
            under_30 = under_30 + 1

    print("Total pages: "+str(total_pages))
    print("Number of chapters more than 30 pages: "+str(over_30))
    print("Number of chapters fewer than or exactly 30 pages: "+str(under_30))

print("Using the custom func approach:")
count_pages(page_counts)
