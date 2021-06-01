# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, col_select=None, types=None, has_headers=True, delimeter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as file:
        rows = csv.reader(file, delimiter=delimeter)

        # Read the file headers
        if has_headers:
            headers = next(rows) 
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if col_select:
                indices = [headers.index(colname) for colname in col_select]
                headers = col_select
            else:
                indices = []
        else:
            indices = []
        
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]
                
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            
            if has_headers:
                record = dict(zip(headers, row))               
            else:
                record = tuple(row)
                
            records.append(record)

    return records