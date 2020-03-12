def seatsInTheater(nCols, nRows, col, row):
    print((nCols - (col - 1)) * (nRows - row))

nCols = 16
nRows = 11
col = 5
row = 3

seatsInTheater(nCols, nRows, col, row)
