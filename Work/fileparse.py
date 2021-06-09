# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, col_select=None, types=None, has_headers=True, delimiter=',', silence_errors=True) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if col_select and has_headers == False:
        raise RuntimeError("select argument requires column headers")
    
    rows = csv.reader(lines, delimiter=delimiter)
    
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
    for index, row in enumerate(rows, start=1):
        try:
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
        except ValueError as e:
            if silence_errors:
                continue
            else:
                print(f'Row {index}: Couldn\'t converted {row}')
                print(f'Row {index}: Reason: {e}')

    return records
