import os
import csv


month_count = 0
this_month_total = 0
last_month_total = 0
total_amount = 0
revenue_change = 0
revenue_changes = []
months = []

filepath = os.path.join('budget_data.csv')
with open(filepath, 'r', newline="") as csvbank:
    budget_reader = csv.reader(csvbank, delimiter = ",")
    
    next(budget_reader)
    
    for row in budget_reader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_total = int(row[1])
        total_amount = total_amount + this_month_total
        if month_count > 1:
            revenue_change = this_month_total - last_month_total
            revenue_changes.append(revenue_change)
        last_month_total = this_month_total
        
sum_revenue_changes = sum(revenue_changes)
average_change = sum_revenue_changes/(month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")
