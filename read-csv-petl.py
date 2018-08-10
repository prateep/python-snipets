# This Python file uses the following encoding: utf-8 

# Read csv by using petl
import petl as etl
import pprint

pp = pprint.PrettyPrinter(indent=4)

# read csv file
try:
    teble1 = etl.fromcsv('profitss.csv', delimiter=',', encoding='utf-8', errors='ignore')
    for row in teble1[1:]:
        print(row[0])
        print(row[1])
        print(row[2])  
except IOError:
      print "Error: File does not appear to exist."
      exit(0)




    
