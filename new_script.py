import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')
year = '2000'
new_query = f"(date >='{year}' and date<={year}+22)"
df_by_date = df.query(new_query)
print(df_by_date)








#year = 2000
#country_code = 'KOR'
#new_query = f"(date >= '{year}-01-01' and date <= '{int(year)+1}-12-31')"

#df_by_date = df.query(new_query)

#print(df_by_date)