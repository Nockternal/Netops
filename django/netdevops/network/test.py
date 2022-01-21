months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_challenges = {
    'January': 'challenge-1',
    'February': 'challenge-2',
    'March': 'challenge-3',
    'April': 'challenge-4',
    'May': 'challenge-5',
    'June': 'challenge-6',
    'July': 'challenge-7',
    'August': 'challenge-8',
    'September': 'challenge-9',
    'October': 'challenge-10',
    'November': 'challenge-11',
    'December': 'challenge-12'
}
month = 'June'
for i in range(len(months)):
    print(i)
    if month == i+1:
            print(f"{i} - {months[i]}")

print(monthly_challenges[month])