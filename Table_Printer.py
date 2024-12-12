#! python3
#Table_printer.py prints the table in an organized way 



def printTable(tableData):
    # Step 1: Initialize column widths
    colWidths = [0] * len(tableData)

    # Step 2: Calculate maximum widths for each column
    for col in range(len(tableData)): #len(tableData) = 3{since there are 3 sub-lists}, col = 1 and tableData[1] = fruits list and so on...
        for item in tableData[col]: #item in that particular list{tableData[1]=fruit list-> apple,orange ...}
            item_length = len(item) #len(apple) = 5 -> item_length
            if item_length > colWidths[col]: # 5 > 1 enter the condition
                colWidths[col] = item_length  #colWidths[1] = 5 ... and keeps repeating for the conditions

    # Step 3: Print the table
    for row in range(len(tableData[0])):  # Loop through the number of rows
        for col in range(len(tableData)):  # Loop through each column
            # Use `rjust()` to right-justify the string based on the corresponding width
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()  # Move to the next line after printing all columns in a row

# Example usage
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(tableData)