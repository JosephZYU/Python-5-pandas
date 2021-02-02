import csv
from collections import defaultdict, Counter

url = '/Users/josephyu/Documents/GitHub/data/survey_results_public.csv'

with open(url) as f:
    csv_read = csv.DictReader(f)

    total = 0

    language_counter = Counter()

    for line in csv_read:
        # language_counter[line['LanguageWorkedWith']] += 1
        languages = line['LanguageWorkedWith'].split(';')

        # 🧠 counter.update()
        language_counter.update(languages)

        total += 1

# 🧠 counter.most_common(n)
# print(language_counter.most_common(5))

for language, lan_count in language_counter.most_common(10):
    lan_pct = lan_count / total * 100
    print(f'{language}: {lan_pct:.2f}%')

    # total = counts['Yes'] + counts['No']
    # yes_pct = counts['Yes'] / total * 100
    # no_pct = counts['No'] / total * 100

    # print(f'Yes: {yes_pct:.2f}%')
    # print(f'No: {no_pct:.2f}%')
