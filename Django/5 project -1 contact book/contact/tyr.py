from datetime import datetime

# Example date strings
date_str1 = '2024-09-01 12:00:00'
date_str2 = '2024-09-03 15:30:00'

# Convert strings to datetime objects
date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
print(type(date1))
# Calculate the difference
difference = date2 - date1

print(f"Difference: {difference}")
