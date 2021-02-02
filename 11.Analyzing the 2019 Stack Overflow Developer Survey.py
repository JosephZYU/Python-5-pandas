import csv

url = '/Users/josephyu/Documents/GitHub/data/survey_results_public.csv'

with open(url) as f:
    csv_read = csv.DictReader(f)

    yes_count = 0
    no_count = 0

    for line in csv_read:
        if line['Hobbyist'] == 'Yes':
            yes_count += 1
        elif line['Hobbyist'] == 'No':
            no_count += 1


total = yes_count + no_count

print(yes_count / total)
print(no_count / total)
