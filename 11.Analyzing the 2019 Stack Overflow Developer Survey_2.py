import csv
from collections import defaultdict, Counter

url = '/Users/josephyu/Documents/GitHub/data/survey_results_public.csv'

with open(url) as f:
    csv_read = csv.DictReader(f)

    language_counter = Counter()

    for line in csv_read:
        # language_counter[line['LanguageWorkedWith']] += 1
        languages = line['LanguageWorkedWith'].split(';')

        # 🧠 counter.update()
        language_counter.update(languages)


print(language_counter)


# total = counts['Yes'] + counts['No']

# yes_pct = counts['Yes'] / total * 100
# no_pct = counts['No'] / total * 100

# print(f'Yes: {yes_pct:.2f}%')
# print(f'No: {no_pct:.2f}%')
