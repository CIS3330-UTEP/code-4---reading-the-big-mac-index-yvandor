import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')"
    df_result = df.query(query)
    avg_dollar = round(df_result['dollar_price'].mean(),2)
    iso_a3 = ['iso_a3']
    return avg_dollar

def get_big_mac_price_by_country(country_code):
    df=pd.read_csv(big_mac_file)
    query = f"(iso_a3 == '{country_code}')"
    df_result = df.query(query)
    mean_dollar_price = df_result['dollar_price'].mean()
    mean_dollar_price_two_decimals = round (mean_dollar_price,2)
    return mean_dollar_price_two_decimals

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    New_query = f" (date >= '{year}-01-01' and date <= '{year}-12-31') "
    df_result = df.query(New_query)
    index_min_value = df_result['dollar_price'].idxmin()
    df_result.loc[index_min_value]['dollar_price']
    cheapest_big_mac_price = df_result.loc[index_min_value]
    row = New_query
    country_name = (['name'])
    iso_a3 = ['iso_a3']
    return f"{country_name}({iso_a3}index_min_value): ${cheapest_big_mac_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    New_query = f" (date >= '{year}-01-01' and date <= '{year}-12-31') "
    df_result = df.query(New_query)
    index_max_value = df_result['dollar_price'].idxmax()
    df_result.loc[index_max_value]['dollar_price']
    expensive_big_mac_price = df_result.loc[index_max_value]
    return index_max_value

if __name__ == "__main__":
    year= int(input("Enter the year:"))
    country_code = input("enter the country code:").upper()
    result_a = get_big_mac_price_by_year(year,country_code)
    print(f"The price of a big mac in {year}, loacation:{country_code}, was {result_a}.")
    result_b = get_big_mac_price_by_country (country_code)
    print(f"The mean price of a bigmac is currently {result_b}.")
    result_c = get_the_cheapest_big_mac_price_by_year(year)
    print(f"{result_c}")
    result_d = get_the_most_expensive_big_mac_price_by_year(year)
    print(f"{result_d}")