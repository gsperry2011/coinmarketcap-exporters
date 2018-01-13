from datetime import datetime
import csv

# file that contains CMC export, will also be our destination for writing output
file = '/home/greg/googledrive/crypto/historical_prices/eth_price_history_full.csv'

# blank list so we can append our data in the loop below
output = []
headers = ['date','open','high','low','close','volume','marketcap','average']
output.append(headers)

with open(file, 'rb') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
         
     for row in csvreader:

         if 'Date' in row:
             print 'Skipping header row on import file'

         else:

             origdate = row[0]
             date = datetime.strptime(origdate, '%b %d %Y')
             # remove bad date from row list
             row.pop(0)

             """
             formating our date for output.
             we convert to a str otherwise datetime will print a tuple.
             we do date.date to only output the YYYY-MM-DD with no HH:MM:SS
             """
             date = str(date.date())
             # adding converted date back to row
             row.insert(0, date)

             # add the current row, with the converted date to our output list
             output.append(row)


# output data, we will overwrite our file with our changes
with open(file, 'w') as outputfile:
   csvwriter = csv.writer(outputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

   # write outputs from output list to file
   csvwriter.writerows(output)

print 'completed'
