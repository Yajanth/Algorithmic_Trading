# Algorithmic Trading Data Preparation

## Overview

This Python script is designed to assist in the data preparation phase of algorithmic trading. It utilizes multi-threading and the Yahoo Finance API to gather financial information for a list of S&P 500 stocks. The code then performs some analysis on the collected data, filters the top 50 stocks based on one-year price return, and calculates the number of shares to buy for a given portfolio size. Below are the key components and instructions for using this script.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

1. Python 3.10 installed on your system.
2. Required libraries, which can be installed using pip:
   - numpy
   - pandas
   - yfinance
   - threading
   - concurrent.futures
   - warnings

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Ensure you have a CSV file named "sp_500_stocks.csv" in the project directory. This file should contain a list of S&P 500 stock tickers.

4. Execute the script by running the following command:

5. Follow the on-screen prompts to input the size of your portfolio.

6. The script will then gather data for the selected stocks, filter the top 50 based on one-year price return, and calculate the number of shares to buy for your portfolio.

7. Review the results displayed on the screen, which will include the list of top 50 stocks and the number of shares to buy for your portfolio.

## Notes

- The script uses multi-threading to speed up data extraction from Yahoo Finance. The number of threads used is adjustable in the `max_workers` parameter within the `ThreadPoolExecutor` block.

- Make sure you have a stable internet connection, as the script relies on fetching data from the Yahoo Finance API.

- The script may display warnings if it encounters issues with fetching data for certain stocks. These warnings can be safely ignored, but it's advisable to review them to ensure data completeness.

- The filtered list of top 50 stocks and the number of shares to buy are displayed on the screen, but you can also access this data in the `stocks_dataframe` variable within the script.

