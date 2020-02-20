import csv
import decimal

regions = []
region_units = {}
region_revenue = {}
region_avg_revenue = {}

current_region = ""
current_units = 0
current_revenue = 0
current_avg_revenue = 0

f = open("500000 Sales Records.csv",'rt')

reader = csv.reader(f)

header_row = next(reader)

for row in reader:
    current_region = row[0]
    current_units = row[8]
    current_revenue = row[11]
    current_avg_revenue = decimal.Decimal(row[11]) / decimal.Decimal(row[8])

    if not current_region in region_units:
        region_units[current_region] = current_units
    else:
        region_units[current_region] = \
            int(region_units[current_region]) + int(current_units)

    if not current_region in region_revenue:
        region_revenue[current_region] = current_revenue
    else:
        region_revenue[current_region] = \
            decimal.Decimal(region_revenue[current_region]) + decimal.Decimal(current_revenue)

    if not current_region in region_avg_revenue:
        region_avg_revenue[current_region] = current_avg_revenue
    else:
        region_avg_revenue[current_region] = \
            (decimal.Decimal(current_revenue[current_region]) + decimal.Decimal(current_revenue)) \
            / (decimal.decimal((region_units[current_region])) + decimal.Decimal(current_units))


print("Regions analysed: "),
regions = list(region_units.keys())
for n in regions:
    print(n + " /"),
print(" \n")

print("Total: " + str(len(regions)) + " regions. \n")

for (u,a,r) in zip(region_units,region_avg_revenue,region_revenue):
    print(u + "\n")
    print("Total units solde: " + str(region_units[u]))
    print("Average revenue per unit: " + "$" + str(region_avg_revenue[a]))
    print("Total revenue of sales: " + "$" + str(region_revenue[r]) + "\n")









