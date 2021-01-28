# 🧭 loc is better for human-readable analysis loc更适用于文本形式分析 -> .loc[row, col]
# 🧭 If there is ONLY one filter dimension -> use df[filter] directly! 如果只有一个维度的过滤，直接使用df[filter]
# 🧭 .loc is the ultimate way of re-setting indexes -> df.loc[row, col] -> df.loc[x, y]

# 🧭 split -> Apply function -> Combine Results (https://youtu.be/txMdrV1Ut64?t=817)

# 🧭 NOTE: replace / rename / map MUST come with {dict-format}!

df['Hobbyist'].replace({'Yes': 1, 'No': 0})

"""
String series:

df[].str.contains()
df[].str.replace()
df[].str.upper()
df[].str.lower()
df[].str.split()


# 🎯 对收入进行类似百分比的分段式截取
# 🎯 根据high salary过滤，获得各个国家高薪岗位分布图

df['SocialMedia'].value_counts(normalize=True)*100

Reddit                      17.023343
YouTube                     16.379076
WhatsApp                    15.807051
Facebook                    15.606902
Twitter                     13.498822
Instagram                    7.414996
I don't use social media     6.577685
LinkedIn                     5.330602

"""


# 200 - Check if there is ANY space from column names
count = 0

for i in df.columns.values.tolist():
    if ' ' in i:
        count += 1

print(count)
