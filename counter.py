import csv

f = open('count_by_day.csv')
csv_f = csv.reader(f)

# the pgpCounter will correspond to each column in the csv.
pgpCounter = [0,0,0,0,0,0,0,0,0,0]
rowsRead = 0

# We going to iterate through each each column in each row.
# As we move down the rows, we add each appearances of unique
# users (as indicated by the appearance of a date) to pgpCounter.
for row in csv_f:
    if rowsRead > 0:

    	# count and increment the current row in column 2.
    	currentRow = row[1]
    	pgpCounter[0] = pgpCounter[0] + int(currentRow)

    	# count and increment the current row in column 3.
    	currentRow = row[2]
    	pgpCounter[1] = pgpCounter[1] + int(currentRow)	

    	# ... and so on.
    	currentRow = row[3]
    	pgpCounter[2] = pgpCounter[2] + int(currentRow)	

    	currentRow = row[4]
    	pgpCounter[3] = pgpCounter[3] + int(currentRow)	

    	currentRow = row[5]
    	pgpCounter[4] = pgpCounter[4] + int(currentRow)	

    	currentRow = row[6]
    	pgpCounter[5] = pgpCounter[5] + int(currentRow)	

    	currentRow = row[7]
    	pgpCounter[6] = pgpCounter[6] + int(currentRow)	

    	currentRow = row[8]
    	pgpCounter[7] = pgpCounter[7] + int(currentRow)	

    	currentRow = row[9]
    	pgpCounter[8] = pgpCounter[8] + int(currentRow)	

    	currentRow = row[10]
    	pgpCounter[9] = pgpCounter[9] + int(currentRow)	
    	
    	print pgpCounter

    rowsRead += 1
rowsRead = 0