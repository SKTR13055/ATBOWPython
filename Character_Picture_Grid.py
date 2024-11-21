grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# Get the number of rows and columns
num_rows = len(grid)
num_cols = len(grid[0])
# Loop through each column
for cols in range(num_cols):
# Loop through each rows
  for rows in range(num_rows):
# Print the character in the grid at the current row and column
    print(grid[rows][cols],end="") # Use end='' to avoid new lines
  print() # Print a new line after finishing a column
