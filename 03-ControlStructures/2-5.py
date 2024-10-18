def get_quarter(month):
    if month >= 10:
        return 4
    elif month >= 7:
        return 3
    elif month >= 4:
        return 2
    elif month >=1:
        return 1
    
months_to_check = [12,10,9,1]

for month in months_to_check:
    quarter = get_quarter(month)
    if quarter is not None:
        print(f'Month {month} is in quarter {quarter}.')
    else:
        print(f'Month {month} is not a valid month number.')