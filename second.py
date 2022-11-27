class Table:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.table =[[0]*self.columns for _ in range(self.rows)]
        print (self.table)

    def set_date(self, row, col, value):
        self.table[row] [col] = value

    def n_rows(self):
        return self.rows
    def n_cols(self):
        return self.columns
    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1
 
    def delete_col(self, col):
        for row in range(self.rows):
            self.table[row].pop(col)
        self.columns -= 1
    
    def add_row(self, row):
        self.table.insert(row, [0] * self.columns)
        self.rows += 1
 
    def add_col(self, col):
        for row in range(self.rows):
            self.table[row].insert(col, 0)
        self.columns += 1
    def get_value(self, row, col):
        return (self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.columns
                else None)
    
tab = Table(2,2)
tab.set_date(1,0,9)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 
tab.add_row(1)
 
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 

    



        
