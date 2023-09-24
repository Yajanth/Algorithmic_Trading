# Import necessary libraries
import numpy as np
import pandas as pd
from scipy import stats
import math
import yfinance as yf
import threading
from concurrent.futures import ThreadPoolExecutor
import warnings
import concurrent
import datetime
import time
warnings.filterwarnings("ignore")

# Importing ticker names
stocks = pd.read_csv("sp_500_stocks.csv")
lst=stocks['Ticker']
# Extracting data from yfinance using Multi-threading
lst1=lst[range(0,100)]
lst2=lst[range(100,200)]
lst3=lst[range(200,300)]
lst4=lst[range(300,400)]
lst5=lst[range(400,len(lst))]
#> High-quality momentum stocks show "slow and steady" outperformance over long periods of time.

#> Low-quality momentum stocks might not show any momentum for a long time, and then surge upwards.

#The reason why high-quality momentum stocks are preferred is because low-quality momentum can often be cause by short-term news that is unlikely to be repeated in the future (such as an FDA approval for a biotechnology company).

#To identify high-quality momentum, we're going to build a strategy that selects stocks from the highest percentiles of:

#1-month price returns
#3-month price returns
#6-month price returns
#1-year price returns

# Calculate Returns for 6 months,3 months, 1 Year
end_date=datetime.date.today()

six_months_start_date=end_date-datetime.timedelta(days=180)
# three_months_start_date=end_date-datetime.timedelta(days=90)
# one_months_start_date=end_date-datetime.timedelta(days=30)

def calc_returns( ticker,start_date,end_date ):
    try:
     
     stock_data=yf.download(ticker,start_date,end_date,progress=False) #progess doesnt download the data between start date and end date
     if stock_data is not None:
      initial_price=stock_data['Adj Close'].iloc[0]
      final_price=stock_data['Adj Close'].iloc[-1]
      returns=np.floor(((final_price-initial_price)/initial_price)*100)
     else:
       print("No data found for {ticker}")
     return f"{ returns:.2f}"
    except Exception as e:
       print("Exception in:",e)

# API calss and extracting data
lst=['MSFT',"AAPL"]

def extract_data(lst):
    global my_columns
    global stocks_dataframe
    my_columns = ['Ticker',
               'Price',
            #    'Six_month_price_return',
            #    'six_month_return_percentile',
            #    'Three_month_price_return',
            #    'three_month_return_percentile',
            #    'One_month_price_return',
            #    'One_month_return_percentile',
               'One_year_Price_Return',
               'One_year_return_percentile',
               'Number of shares to Buy',
               'HQM Score']
    stocks_dataframe=pd.DataFrame(columns=my_columns)
    for stock in lst:

        try:
            tick=yf.Ticker(stock)
            data=tick.info
            if data is not None:
                stocks_dataframe=pd.concat([stocks_dataframe,
                                            pd.Series([
                                                stock,
                                                data.get('currentPrice', 'N/A'), # Returns current price if found or N/A if not found
                                                # calc_returns(stock,six_months_start_date,end_date),
                                                # calc_returns(stock,three_months_start_date,end_date),
                                                # calc_returns(stock,one_months_start_date,end_date),
                                                data.get('returnOnEquity', 'NaN'),
                                                0,
                                                'N/A',
                                                'N/A'
                                                
                                            ],index=my_columns
                                            ).to_frame().T],ignore_index=True)

            else:
                print('Data Not Found:',stock)
        except Exception as e:
            print(stock,'expection is :',str(e))
            
extract_data(lst)

def main():
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Submit tasks for each stock
        futures1 = executor.submit(extract_data, lst1)
        futures2 = executor.submit(extract_data, lst2) 
        futures3 = executor.submit(extract_data, lst3) 
        futures4 = executor.submit(extract_data, lst4) 
        futures5 = executor.submit(extract_data, lst5) 
    
        

if __name__ == "__main__":
    main()
    stocks_dataframe.to_csv('Strategy_data.csv',index=False)

time_periods=[
    'One_year',
    # "six_month",
    # "Three_month",
    # 'One_month'
    ]
# stocks_dataframe['One_year_return_percentile']=0

for i in range(0,len(stocks_dataframe.index)):
    try:
        for time_period in time_periods:
            stocks_dataframe.loc[i,percentile_return]=0
            stocks_dataframe[price_return] = pd.to_numeric(stocks_dataframe[price_return])
            price_return=f'{time_period}_Price_Return'
            percentile_return=f'{time_period}_return_percentile'
            # print(i,stocks_dataframe.loc[i,percentile_return])
            stocks_dataframe.loc[i,percentile_return] = stats.percentileofscore(stocks_dataframe[price_return], stocks_dataframe.loc[i, price_return])/100
            stocks_dataframe['One_year_return_percentile'][i] = stats.percentileofscore(stocks_dataframe[price_return], stocks_dataframe.loc[i, price_return])/100


    except Exception as e:
        print('Exception:',str(e))
from statistics import mean

for i in range(0,len(stocks_dataframe.index)):
    momentum_percentile=[]
    try:
        for time_period in time_periods:
            momentum_percentile.append(stocks_dataframe.loc[i,f'{time_period}_return_percentile'])
        stocks_dataframe['HQM Score']=mean(momentum_percentile)




    except Exception as e:
        print('Exception:',str(e))



stocks_dataframe.sort_values('HQM Score',ascending=False, inplace=True)
# stocks_dataframe.sort_values('One_year_Price_Return',ascending=False, inplace=True)
stocks_dataframe=stocks_dataframe[:50]

try:
    portfolio_size=float(input('Enter the value of the portfolio'))
except:
    print('Error: Please enter a number')
    portfolio_size=float(input('Enter the value of the portfolio'))

val=portfolio_size
val


# Position such as the amount of money invested in stock
position_size=val/len(stocks_dataframe.index)
for i in range(0,len(stocks_dataframe.index)):
    try:

     stocks_dataframe.loc[i,'Number of shares to Buy']=math.floor(position_size/stocks_dataframe['Price'][i])
    #  print(stocks_dataframe['Price'][i])
    except Exception as e:
       print("Exception:",str(e))

stocks_dataframe.to_csv('Final_Strategy.csv')   
