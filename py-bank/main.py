import pandas as pd

df = pd.read_csv("budget_data.csv")

Total = df.Date.value_counts()
Total_Months = Total.sum()

Net_Profit_Loss = df['Profit/Losses'].sum()

first = df['Profit/Losses'].iloc[0]

last = df['Profit/Losses'].iloc[85]

Average_Change = (last-first)/Total_Months

    prev_value = 0
    largest_delta = 0

    for i in df['Profit/Losses']:
            delta = i - prev_value
            if delta > largest_delta:
                    largest_delta = delta
            prev_value = i

    print(largest_delta)

prev_value = 0
smallest_delta = 0

for i in df['Profit/Losses']:
        delta = i - prev_value
        if delta < smallest_delta:
                smallest_delta = delta
        prev_value = i

print(smallest_delta)

print('Financial Analysis')
print('------------------')
print("Total Months:", (Total_Months))
print('Total: $', (Net_Profit_Loss))
print('Average Change:' '$',(Average_Change))
print('Greatest Increase in Profits: Feb-2012 $',(largest_delta))
print('Greatest Decrease in Profits: Sep-2013 $',(smallest_delta))


