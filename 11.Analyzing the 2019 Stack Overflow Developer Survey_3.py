# Break down most popular languages by developer type
# https://youtu.be/_P7X8tMplsw?t=2130

import csv
from collections import defaultdict, Counter

url = '/Users/josephyu/Documents/GitHub/data/survey_results_public.csv'

with open(url) as f:
    csv_read = csv.DictReader(f)

    dev_type_info = {}

    for line in csv_read:
        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })

            languages = line['LanguageWorkedWith'].split(';')
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1

for dev_type, info in dev_type_info.items():
    print(dev_type)

    for language, lan_count in info['language_counter'].most_common(5):
        lan_pct = lan_count / info['total'] * 100
        print(f'{language}: {lan_pct:.2f}%')
        print()
