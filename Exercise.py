import csv
# csv_data = [["StudentId", "Grade"], [123456, "A"],[123678, "B"],[127896, "C"]]

# with open('person.csv', 'w') as csvFile:
    # writer = csv.writer(csvFile)
    # writer.writerows(csv_data)


# f = open("person.csv", "rt")

# reader = csv.reader(f)
# for row in reader:
    # print (row)


num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

for (a, b, c) in zip(num, color, value):
     print a, b, c
