months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month = 1
for i in range(len(months)):
    print(i)
    if month == i+1:
            print(f"{i} - {months[i]}")