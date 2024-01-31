# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:54:44 2024

@author: Mokgadi Precious Mph
"""

import pandas as pd

file = pd.read_csv("data_02/data_02/iris.csv")

"""
Absolute Path:

C:/Users/Mokgadi Precious Mph/css2024_day02/data_02/data_02/iris.csv

Relative Path:
data_02/iris.csv
"""

#file = pd.read

file = pd.read_csv("data_02/data_02/Geospatial Data.txt", sep=";")

print(file)

"""
 Landcover Type Select Crop Type  ...          X          Y
0            crop           tomato  ...  30.146589 -22.894748
1            crop           tomato  ...  30.146506 -22.894734
2            crop           tomato  ...  30.146305 -22.894717
3            crop           tomato  ...  30.146147 -22.894691
4            crop           tomato  ...  30.146070 -22.894575
..            ...              ...  ...        ...        ...
87           soil             soil  ...  30.145931 -22.894080
88           soil             soil  ...  30.145929 -22.893918
89           soil             soil  ...  30.146283 -22.893956
90           soil             soil  ...  30.146436 -22.893789
91           soil             soil  ...  30.145790 -22.893725
"""

file = pd.read_excel("data_02/data_02/residentdoctors.xlsx")

print(file)
"""
 AGE  ghqscore_sum  jobsatisfaction_sum  ...  CHILDREN female HOURSWORKED
0     31          24.0                  5.0  ...       1.0      1        50.5
1     38          24.0                  8.0  ...       1.0      1        30.5
2     33          24.0                 11.0  ...       0.0      1        50.5
3     36          24.0                  9.0  ...       2.0      1        70.5
4     29          21.0                  8.0  ...       1.0      1        50.5
..   ...           ...                  ...  ...       ...    ...         ...
156   30          24.0                  5.0  ...       0.0      0       100.5
157   32          28.0                  9.0  ...       0.0      0        90.5
158   31          31.0                  5.0  ...       0.0      0        90.5
159   34          19.0                  9.0  ...       1.0      0       100.5
160   29          18.0                  8.0  ...       0.0      0        70.5
"""

file = pd.read_json("data_02/data_02/student_data.json")

print(file)
"""
 id                   field  ... amount_of_students  campus
0   1        Computer Science  ...               3000       A
1   2  Biomedical Engineering  ...               4000       B
2   3                 Physics  ...               2000       A
3   4             Mathematics  ...               3100       C
"""

file = pd.read_csv("data_02/data_02/country_data_index.csv")

print(file)
"""
  Unnamed: 0  Age Gender       Country
0            0   39      M  South Africa
1            1   25      M      Botswana
2            2   29      F  South Africa
3            3   46      M  South Africa
4            4   22      F         Kenya
5            5   35      F    Mozambique
6            6   22      F       Lesotho
7            7   49      M         Kenya
8            8   30      M         Kenya
9            9   40      F         Egypt
10          10   30      M         Sudan
"""

df = pd.read_csv("data_02/data_02/country_data_index.csv")

print(df) 

df = pd.read_csv("data_02/data_02/country_data_index.csv",index_col=0)

print(df)
"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan

"""

df = pd.read_excel("data_02/data_02/residentdoctors.xlsx")

print(df.info())
"""
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 
 """

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())
"""
#   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    object 
 
 """
 
df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())
"""
#   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    int32  
 
 """
 
 """
 Working with dates
 """
 
 df = pd.read_csv("data_02/data_02/time_series_data.csv")
 
 print(df.info())
"""
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Unnamed: 0   366 non-null    int64  
 1   Date         366 non-null    object 
 2   Temperature  366 non-null    float64
 
 """
 
 df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")
 
 print (df.info())
 
 df['Year'] = df['Date'].dt.year
 
 """
 .str
 .extract
 .astype
 """
 
 df = pd.read_csv("data_02/data_02/patient_data_dates.csv")
print(df.info())
"""
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Index     32 non-null     int64  
 1   Duration  32 non-null     int64  
 2   Date      31 non-null     object 
 3   Pulse     32 non-null     int64  
 4   Maxpulse  32 non-null     int64  
 5   Calories  30 non-null     float64
 
 """
 
df = pd.read_csv("data_02/data_02/patient_data_dates.csv",index_col=0)
print(df.info())
"""
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  32 non-null     int64  
 1   Date      31 non-null     object 
 2   Pulse     32 non-null     int64  
 3   Maxpulse  32 non-null     int64  
 4   Calories  30 non-null     float64

"""

df = pd.read_csv("data_02/data_02/patient_data_dates.csv",index_col=0)
print(df.info())


df.drop(index=26, inplace=True)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])

print(df.info())
"""
#   Column    Non-Null Count  Dtype         
---  ------    --------------  -----         
 0   Duration  31 non-null     int64         
 1   Date      30 non-null     datetime64[ns]
 2   Pulse     31 non-null     int64         
 3   Maxpulse  31 non-null     int64         
 4   Calories  29 non-null     float64      
 
 """
 
avg_cal = df['Calories'].mean()

df["Calories"].fillna(avg_cal, inplace = True)


"""
best practices
"""
df.dropna(inplace = True)
df = df.reset_index(drop=True)

print(df)


df.loc[7, 'Duration'] =45

df['Duration'] = df['Duration'].replace([450], 50)

print(df)
"""
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130     409.1
1         60 2020-12-02    117       145     479.0
2         60 2020-12-03    103       135     340.0
3         45 2020-12-04    109       175     282.4
4         45 2020-12-05    117       148     406.0
5         60 2020-12-06    102       127     300.0
6         60 2020-12-07    110       136     374.0
7         45 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
9         60 2020-12-10     98       124     269.0
10        60 2020-12-11    103       147     329.3
11        60 2020-12-12    100       120     250.7
12        60 2020-12-12    100       120     250.7
13        60 2020-12-13    106       128     345.3
14        60 2020-12-14    104       132     379.3
15        60 2020-12-15     98       123     275.0
16        60 2020-12-16     98       120     215.2
17        60 2020-12-17    100       120     300.0
18        60 2020-12-19    103       123     323.0
19        45 2020-12-20     97       125     243.0
20        60 2020-12-21    108       131     364.2
21        60 2020-12-23    130       101     300.0
22        45 2020-12-24    105       132     246.0
23        60 2020-12-25    102       126     334.5
24        60 2020-12-27     92       118     241.0
25        60 2020-12-29    100       132     280.0
26        60 2020-12-30    102       129     380.3
27        60 2020-12-31     92       115     243.0

"""

df = pd.read_csv("data_02/data_02/iris.csv")

print(df.columns)
"""
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'], dtype='object')

"""

col_names = df.columns

col_names = df.columns.tolist()

print(col_names)
"""
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

"""

df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)

grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean

print(mean_square_values)
"""
<bound method GroupBy.mean of <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001CCF34D7250>>
"""

df1 = pd.read_csv("data_02/data_02/person_split1.csv")
df2 = pd.read_csv("data_02/data_02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index=True)

df1 = pd.read_csv("data_02/data_02/person_education.csv")
df2 = pd.read_csv("data_02/data_02/person_work.csv")

df_merge_inner = pd.merge(df1,df2,on="id")

print(df)
"""
    id first_name     last_name                          email       ip_address
0    1      Ozzie    Everington   oeverington0@marketwatch.com    50.218.126.57
1    2   Sharlene     Bearsmore      sbearsmore1@shinystat.com   117.146.130.90
2    3    Yolanda        Adamou                 yadamou2@ow.ly    241.32.63.240
3    4    Myranda        Kloser         mkloser3@parallels.com    74.193.226.83
4    5    Winonah     Sandeford  wsandeford4@timesonline.co.uk  239.251.207.237
5    6      Ivory       Wingatt              iwingatt5@com.com    116.87.10.137
6    7       Egor  De Beauchamp        edebeauchamp6@wufoo.com   151.131.138.28
7    8      Jobie       Pashler              jpashler7@sun.com   188.154.228.79
8    9    Charity         Libby           clibby8@edublogs.org   47.216.160.225
9   10      Sadye       Poacher               spoacher9@nhs.uk    29.57.154.142
10  10      Sadye       Poacher               spoacher9@nhs.uk    29.57.154.142
11  11      Jaime       McGrill         jmcgrilla@virginia.edu      22.65.19.34
12  12      Perla      McKevany         pmckevanyb@yahoo.co.jp     182.44.72.83
13  13     Mickey        Domico          mdomicoc@stanford.edu   204.200.186.61
14  14     Brigid      Plaschke           bplaschked@yahoo.com   33.247.110.109
15  15     Vinita        Rapley          vrapleye@marriott.com   145.114.16.112
16  16   Gennifer        Coupar               gcouparf@gnu.org  250.228.216.206
17  17     Dorita     Wilbraham         dwilbrahamg@uol.com.br    103.54.57.216
18  18    Thaxter         Gunby            tgunbyh@skyrock.com  175.214.186.108
19  19    Iseabal        Cabble          icabblei@netvibes.com    111.74.212.26
20  20     Darcey        Bissex              dbissexj@blog.com   62.197.134.253

"""
import pandas as pd

df = pd.read_csv("data_02/data_02/iris.csv")

print(df)
"""
    sepal_length  sepal_width  petal_length  petal_width           class
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

"""
df["class"] = df["class"].str.replace("Iris-","")

print(df["class"])
"""
0         setosa
1         setosa
2         setosa
3         setosa
4         setosa
   
145    virginica
146    virginica
147    virginica
148    virginica
149    virginica
Name: class, Length: 150, dtype: object

"""
df = df[df['sepal_length'] > 5]

print(df)
"""
     sepal_length  sepal_width  petal_length  petal_width      class
0             5.1          3.5           1.4          0.2     setosa
5             5.4          3.9           1.7          0.4     setosa
10            5.4          3.7           1.5          0.2     setosa
14            5.8          4.0           1.2          0.2     setosa
15            5.7          4.4           1.5          0.4     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

"""

df = df[df["class"] =="virginica"]

print(df)

"""
     sepal_length  sepal_width  petal_length  petal_width      class
100           6.3          3.3           6.0          2.5  virginica
101           5.8          2.7           5.1          1.9  virginica
102           7.1          3.0           5.9          2.1  virginica
103           6.3          2.9           5.6          1.8  virginica
104           6.5          3.0           5.8          2.2  virginica
105           7.6          3.0           6.6          2.1  virginica
107           7.3          2.9           6.3          1.8  virginica
108           6.7          2.5           5.8          1.8  virginica
109           7.2          3.6           6.1          2.5  virginica
110           6.5          3.2           5.1          2.0  virginica
111           6.4          2.7           5.3          1.9  virginica
112           6.8          3.0           5.5          2.1  virginica
113           5.7          2.5           5.0          2.0  virginica
114           5.8          2.8           5.1          2.4  virginica
115           6.4          3.2           5.3          2.3  virginica
116           6.5          3.0           5.5          1.8  virginica
117           7.7          3.8           6.7          2.2  virginica
118           7.7          2.6           6.9          2.3  virginica
119           6.0          2.2           5.0          1.5  virginica
120           6.9          3.2           5.7          2.3  virginica
121           5.6          2.8           4.9          2.0  virginica
122           7.7          2.8           6.7          2.0  virginica
123           6.3          2.7           4.9          1.8  virginica
124           6.7          3.3           5.7          2.1  virginica
125           7.2          3.2           6.0          1.8  virginica
126           6.2          2.8           4.8          1.8  virginica
127           6.1          3.0           4.9          1.8  virginica
128           6.4          2.8           5.6          2.1  virginica
129           7.2          3.0           5.8          1.6  virginica
130           7.4          2.8           6.1          1.9  virginica
131           7.9          3.8           6.4          2.0  virginica
132           6.4          2.8           5.6          2.2  virginica
133           6.3          2.8           5.1          1.5  virginica
134           6.1          2.6           5.6          1.4  virginica
135           7.7          3.0           6.1          2.3  virginica
136           6.3          3.4           5.6          2.4  virginica
137           6.4          3.1           5.5          1.8  virginica
138           6.0          3.0           4.8          1.8  virginica
139           6.9          3.1           5.4          2.1  virginica
140           6.7          3.1           5.6          2.4  virginica
141           6.9          3.1           5.1          2.3  virginica
142           5.8          2.7           5.1          1.9  virginica
143           6.8          3.2           5.9          2.3  virginica
144           6.7          3.3           5.7          2.5  virginica
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

"""

df.to_csv("output/pulsar.csv")