import requests

def get_stock_data(symbol, api_key):
    base_url = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_INTRADAY'
    interval = '5min'

    params = {
        'function': function,
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get('Time Series (5min)')
        
        if time_series:
            latest_data = list(time_series.items())[0]
            print(f"Symbol: {symbol}")
            print(f"Latest Timestamp: {latest_data[0]}")
            print(f"Open: {latest_data[1]['1. open']}")
            print(f"High: {latest_data[1]['2. high']}")
            print(f"Low: {latest_data[1]['3. low']}")
            print(f"Close: {latest_data[1]['4. close']}")
            print(f"Volume: {latest_data[1]['5. volume']}")
        else:
            print(f"No data available for {symbol}")
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
   
    api_key = '21933802-e06e-4ea5-8ba5-95f3583be963'
    stock_symbol = 'wrapper'

    get_stock_data(stock_symbol, api_key)
