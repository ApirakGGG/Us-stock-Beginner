import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def perform_stock_analysis(stock_symbol, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    print(stock_data.head())

    stock_data['Close'].plot(figsize=(10, 5), title=f'{stock_symbol} Stock Price Analysis')
    plt.show()

if __name__ == "__main__":
    stock_symbol = "AAPL", "TSLA"
    start_date = "2000-01-01"
    end_date = "2023-01-01"

    perform_stock_analysis(stock_symbol, start_date, end_date)

