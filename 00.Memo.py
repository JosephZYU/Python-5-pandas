# 🧭🧭🧭 df[row][col] | df.loc[row, col] | df.iloc[row, col]


# 🧭 loc is better for human-readable analysis loc更适用于文本形式分析 -> .loc[row, col]
# 🧭 If there is ONLY one filter dimension -> use df[filter] directly! 如果只有一个维度的过滤，直接使用df[filter]
# 🧭 .loc is the ultimate way of re-setting indexes -> df.loc[row, col] -> df.loc[x, y]

# 🧭 split -> Apply function -> Combine Results (https://youtu.be/txMdrV1Ut64?t=817)

"""
# 🧭 NOTE: replace / rename / map MUST come with {dict-format}!

df.rename(columns={})
df.drop(columns=[])  # BE CAUTIOUS when dropping any data!
"""

# 🧭 Each column first of all a Serie, and a 1-dimensional DataFrame! 列即一维DF

# 🧭 Recommended secure way to locate ONLY numeric columns 便捷稳健的筛选数据列的方法
# 🧠 df.select_dtypes(include=np.number) -> include=np.number

# 🧭 As long as it is a Data Frame, we can always apply filter 只要是DF就可以使用T/F进行过滤


# Concatenate - https://youtu.be/txMdrV1Ut64?t=2131 ⭐️ -> NO.08

# 🎯 how to deal with NaN with the entire DF 整体性处理所有的NaN

# ⭐️ Missing valuves over 10% cut-off

# df.isnull().mean().sort_values(ascending=False)#[:'LastHireDate'].index.tolist()

# 🧠 ⭐️ fillna("")

# df.select_dtypes(include=object).fillna('').applymap(str.upper)


"""
# 🧭 Append can even append to BOTH rows and columns all at once - the ultimate way of adding data as NoSQL style
# Append 可以同时以不定项形式，2维添加行列，非常适合不定项的NoSql模式

# 🧠 df.append({dict}, ignore_index=True) -> ignore_index=True

df = df.append({
    'name': 'Adam Smith',
    'first': 'Joseph',
    'last': 'Yu',
    'email': 'JosephYu@gmail.com',
    }, ignore_index=True)


df.drop(
    index= ,
    columns= ,
)


"""


"""


# 🧭 Replace is in most cases the best solution -> it gives you the option of trila and then use inplace=True to let it happen
# replace 是通常境况下最合适的选择！现实验，如何可行再应用，而不直接影响原始数据！

# 🧭 Replace 1 value ONLY -> replace(a, b)
# 🧭 Replace 2 or more values -> replace({dict})

df['first'].replace({
    'Corey': 'Mark_1',
    'Jane': 'Mark_2',
    'John': 'Mark_3'}, 
    inplace=True)
"""

"""
# ⭐️ Mass create new rows into existing colums 批量添加新行并入已有数据

for i in range(11, 21, 1):
    df.loc[i] = {
    'First_Name':'Joseph',
    'Last_Name':'Yu',
    'Email_Address':'josephyu@outlook.com'
    }
"""


"""

so for example
we can parse out the median salaries for
these developer types what programming
languages have the highest job
satisfaction what the most preferred
development environment is for the
different development types and
languages

"""


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
filter = (df['Date'] < '2020') & (df['Date'] >= '2019')  # Recommende for simplicity 👍👍👍

# 快速以年为单位，晒出需要的每一笔交易

Date	Symbol	Open	High	Low	Close	Volume	DayOfWeek
1749	2019-12-31 23:00:00	ETHUSD	128.33	128.69	128.14	128.54	440678.91	Tuesday
1750	2019-12-31 22:00:00	ETHUSD	128.38	128.69	127.95	128.33	554646.02	Tuesday
1751	2019-12-31 21:00:00	ETHUSD	127.86	128.43	127.72	128.38	350155.69	Tuesday
1752	2019-12-31 20:00:00	ETHUSD	127.84	128.34	127.71	127.86	428183.38	Tuesday
1753	2019-12-31 19:00:00	ETHUSD	128.69	128.69	127.60	127.84	1169847.84	Tuesday
...	...	...	...	...	...	...	...	...
10504	2019-01-01 04:00:00	ETHUSD	130.75	133.96	130.74	131.96	2791135.37	Tuesday
10505	2019-01-01 03:00:00	ETHUSD	130.06	130.79	130.06	130.75	503732.63	Tuesday
10506	2019-01-01 02:00:00	ETHUSD	130.79	130.88	129.55	130.06	838183.43	Tuesday
10507	2019-01-01 01:00:00	ETHUSD	131.62	131.62	130.77	130.79	434917.99	Tuesday
10508	2019-01-01 00:00:00	ETHUSD	130.53	131.91	130.48	131.62	1067136.21	Tuesday

8760 rows × 8 columns

"""


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

"""
# 200 - Check if there is ANY space from column names
count = 0

for i in df.columns.values.tolist():
    if ' ' in i:
        count += 1

print(count)
"""
