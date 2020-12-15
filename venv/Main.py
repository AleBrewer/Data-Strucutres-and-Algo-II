
import csv

with open('WGUPS Package File.csv') as csv_file:
    reader_csv = csv.reader(csv_file)
    

    for line in reader_csv:
        print(line)




