import csv 
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)


print(file_data)