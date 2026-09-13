### INF601 - Advanced Programming in Python
### Ray Bednara
### Mini Project 2


# Stock Price Charts

Pull recent stock prices with yfinance and chart them with matplotlib.

## Description

This project uses the `yfinance` library to pull the last 10 trading days of closing
prices for five stocks: Nvidia (NVDA), Campbell's (CPB), Apple (AAPL), Microsoft (MSFT),
and Verizon (VZ). The closing prices are loaded into a numpy array (tickers x days), and
a line chart is generated for each stock with matplotlib. The charts are saved as PNG
files into a `charts/` directory, which is created automatically if it doesn't exist.

## Getting Started

### Dependencies

* Windows 10/11
* Python 3.13
* Internet connection (yfinance pulls live data)
* Install required libraries with:
```
pip install -r requirements.txt
```

### Installing

* Clone or download this repository
* No file/folder modifications are needed; the `charts/` output directory is created
  automatically when the program runs

### Executing program

* Run the script from the project root:
```
python stocks.py
```
* The script will:
    * Download the last 10 trading days of closing prices for each ticker
    * Print the prices as a numpy array to the console
    * Save one chart per ticker to `charts/`

## Help

If `yfinance` fails to pull data, check your internet connection and confirm the ticker
symbols are still valid on Yahoo Finance.
```
python stocks.py
```

## Authors

Ray Bednara
ray.bednara@gmail.com

## Version History

* 0.3
    * Removed the extra combined comparison chart, keeping one chart per ticker
* 0.2
    * Added numpy array storage and matplotlib chart generation to `charts/`
* 0.1
    * Initial release: yfinance pull of last 10 trading days per ticker

## License

## AI Usage

I used Claude Code to write `stocks.py`: pulling stock data with yfinance, storing it in
a numpy array, and charting it with matplotlib. I had it break the script down to just
the yfinance pull so I could understand that part, then build the numpy/matplotlib
pieces back on top, and remove an extra chart it added that I hadn't asked for.
