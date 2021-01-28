# 🧭 loc is better for human-readable analysis loc更适用于文本形式分析 -> .loc[row, col]
# 🧭 If there is ONLY one filter dimension -> use df[filter] directly! 如果只有一个维度的过滤，直接使用df[filter]
# 🧭 .loc is the ultimate way of re-setting indexes -> df.loc[row, col] -> df.loc[x, y]

# 🧭 split -> Apply function -> Combine Results (https://youtu.be/txMdrV1Ut64?t=817)

# 🧭 NOTE: replace / rename / map MUST come with {dict-format}!

# Concatenate - https://youtu.be/txMdrV1Ut64?t=2131 ⭐️ -> NO.08

"""
🧭 dtypes issues ⭐️ -> NO.09

    1. df.dtypes -> check the ENTIRE df for potential conflicts 整体考察所有col的对应数据类型

    2. na_values = ['NA', 'na', 'Missing'] when forming the dataframe 尽可能将作为string出现的Na类型批量替换成真正的NaN/None/np.nan

        df = pd.read_csv(survey_source, na_values=na_values)  # index_col = 'Respondent' 优化做法是在读取时就清洗完毕！

    3. Finally focus on the remaing text to replace manually 最后针对个别文本逐个替换

        df['YearsCode'].replace({'Less than 1 year':'0', 'More than 50 years':'51'}, inplace=True)
        df['YearsCodePro'].replace({'Less than 1 year':'0', 'More than 50 years':'51'}, inplace=True)


"""
# df['Hobbyist'].replace({'Yes': 1, 'No': 0})

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
