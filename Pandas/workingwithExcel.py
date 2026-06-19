import pandas as pd

df = pd.read_excel("stock_data.xlsx","Sheet1")
# print(df)

def people_change(cell):
    if cell=="n.a.":
        return 'Sam '
    else:
        return cell
    
def price_change(cell):
    if cell=="n.a.":
        return 40
    else:
        return cell
    

df['people'] = df['people'].apply(people_change)
df['price'] = df['price'].apply(price_change)

# print(df)


# df.to_excel("new.xlsx",sheet_name="STOCKS",index=False)

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as newFile:
    df_stocks.to_excel(newFile,sheet_name="STOCKS")
    df_weather.to_excel(newFile,sheet_name="WEATHER")


