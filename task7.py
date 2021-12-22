matrix = []
row = 0

while row != 'end':
    row = input()
    matrix.append(row)

count_row = 0
column_list = []
count_column = 0
print(matrix)
for i in range(len(matrix) - 1):
    column_list.append(matrix[i].split())
    count_column = len(matrix[i].split())
print(column_list)


# new_list = []
# for i in range(len(matrix)-1):
#     row = column_list[i]
#     for j in range(count_column):
#          new_list.append(int(row[j]))


