# 🧭 loc is better for human-readable analysis loc更适用于文本形式分析 -> .loc[row, col]
# 🧭 If there is ONLY one filter dimension -> use df[filter] directly! 如果只有一个维度的过滤，直接使用df[filter]
# 🧭 .loc is the ultimate way of re-setting indexes -> df.loc[row, col] -> df.loc[x, y]

# 🧭 NOTE: replace / rename / map MUST come with {dict-format}!

df['Hobbyist'].replace({'Yes': 1, 'No': 0})

"""
String series:

df[].str.contains()
df[].str.replace()
df[].str.upper()
df[].str.lower()
df[].str.split()

"""
# 🎯 根据high salary过滤，获得各个国家高薪岗位分布图


# 200 - Check if there is ANY space from column names
count = 0

for i in df.columns.values.tolist():
    if ' ' in i:
        count += 1

print(count)
