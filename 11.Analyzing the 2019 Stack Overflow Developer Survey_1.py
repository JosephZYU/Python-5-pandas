import csv

url = '/Users/josephyu/Documents/GitHub/data/survey_results_public.csv'

with open(url) as f:
    csv_read = csv.DictReader(f)

    counts = {
        'Yes': 0,
        'No': 0
    }

    for line in csv_read:
        counts[line['Hobbyist']] += 1

total = counts['Yes'] + counts['No']

yes_pct = counts['Yes'] / total * 100
no_pct = counts['No'] / total * 100

print(f'Yes: {yes_pct:.2f}%')
print(f'No: {no_pct:.2f}%')
