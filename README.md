Here's a README for your code:

# Momentum-Based Stock Selection Strategy

This Python script is designed to implement a momentum-based stock selection strategy using historical stock price data obtained from Yahoo Finance. The strategy selects stocks with high momentum by considering their price returns over different time periods.

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Strategy Overview](#strategy-overview)
- [Code Structure](#code-structure)

## Introduction

The script uses the `yfinance` library to fetch historical stock price data for a list of S&P 500 stocks. It calculates various price returns, including 1-year,6-months price returns, and assigns a percentile score to each stock based on its returns. The stocks are then ranked by their percentile scores to identify high-quality momentum stocks.

## Dependencies

The script relies on the following Python libraries:

- `numpy`
- `pandas`
- `scipy.stats`
- `math`
- `yfinance`
- `threading`
- `concurrent.futures`
- `datetime`

You can install these libraries using `pip` if you haven't already:

```bash
pip install numpy pandas scipy yfinance
```

## Usage

1. Clone or download the repository to your local machine.

2. Make sure you have the required dependencies installed (see the Dependencies section).

3. Prepare a CSV file containing the list of S&P 500 stock tickers (e.g., "sp_500_stocks.csv").

4. Run the script by executing the `momentum_strategy.py` file.

```bash
python Quant_Momentum_Strategy.py
```

5. Follow the on-screen instructions to enter the size of your investment portfolio.

6. The script will generate a CSV file named "Final_Strategy.csv" containing the selected stocks and the number of shares to buy for each stock based on your portfolio size.

## Strategy Overview

The strategy ranks stocks based on their percentile scores for different time periods, including 1-year price returns. High percentile scores indicate strong momentum. The selected stocks are then allocated to your portfolio based on your specified portfolio size.

## Code Structure

- **Data Extraction**: The script uses `yfinance` to extract historical stock price data for the S&P 500 stocks in parallel using multi-threading.

- **Returns Calculation**: It calculates various price returns (e.g., 1-year returns) for each stock.

- **Percentile Ranking**: Stocks are ranked by their percentile scores for different time periods, and the `scipy.stats` library is used for percentile calculations.

- **Portfolio Allocation**: The script determines the number of shares to buy for each selected stock based on your portfolio size.

- **Output**: The final list of selected stocks and their allocation details are saved in a CSV file for your reference.

This script provides a simple yet effective way to identify high-quality momentum stocks based on historical price returns.

