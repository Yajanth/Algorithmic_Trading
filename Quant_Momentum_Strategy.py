# Import necessary libraries
import numpy as np
import pandas as pd
# from scipy import stats
import math
import yfinance as yf
import threading
from concurrent.futures import ThreadPoolExecutor
import warnings
warnings.filterwarnings("ignore")
# Importing ticker names
stocks = pd.read_csv("sp_500_stocks.csv")
ind=len(stocks['Ticker'])

# Extracting data from yfinance using Multi-threading
def extract_data(lst):
    global my_columns
    global stocks_dataframe  
    stocks_dataframe=pd.DataFrame(columns=my_columns)
    my_columns = ['Ticker', 'Price',
              'One_year Price Return', 'Number of shares to Buy']
    for stock in lst:
        try:
            ticker = yf.Ticker(stock)
            data = ticker.info
            if data is not None:
                stocks_dataframe = stocks_dataframe.append(
                    pd.Series(
                        [
                            stock,
                            data.get('currentPrice', 'N/A'),
                            data.get('returnOnEquity', 'N/A'),
                            'N/A'
                        ], index= my_columns
                    ), ignore_index=True
                )
            else:
                print(stock, ': Data not found')
        except Exception as e:
            print(stock, ':', str(e))


def main():
    # Get the list of stocks (modify this as needed)
    # lst = ['AAPL', 'GOOGL']
    lst=stocks['Ticker']


    # Initialize the global stocks_dataframe
    global stocks_dataframe
    stocks_dataframe = pd.DataFrame(columns=my_columns)

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Submit tasks for each stock
        futures = [executor.submit(extract_data, stock) for stock in lst]

        # Wait for all tasks to complete
        # concurrent.futures.wait(futures)

        # Get the results from completed tasks and append them to the DataFrame
        for future in futures:
            result = future.result()
            if result is not None:
                stocks_dataframe = pd.append(result, ignore_index=True)

if __name__ == "__main__":
    main()


def pooling():
    with ThreadPoolExecutor as executor:
     lst=stocks['Ticker']
     
pooling()    



# Importing and cleaning the data
stocks_dataframe=pd.DataFrame(columns=my_columns)
stocks_dataframe=pd.read_csv('Strategy_data.csv')
stocks_dataframe.drop(columns='Unnamed: 0',inplace=True)

stocks_dataframe.sort_values('One_year Price Return',ascending=False,inplace=True)
# stocks_dataframe.reset_index(inplace=True)
stocks_dataframe=stocks_dataframe[:50]
stocks_dataframe

#calculating number of shares to buy
def portfolio_input():
    global portfolio_size
    try:
        portfolio_size=int(input('Enter The size of Portfolio:'))
    except:
        print("Invalid Input")
        # portfolio_size=float(input('Enter the value of the portfolio'))
        portfolio_input()


portfolio_input()
position_size=float(portfolio_size)/len(stocks_dataframe['Ticker'])
position_size