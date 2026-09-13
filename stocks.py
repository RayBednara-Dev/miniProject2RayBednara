# INF601 - Advanced Programming in Python
#Ray Bednara
# Mini Project 2

import yfinance as yf

TICKERS = {
    "NVDA": "Nvidia",
    "CPB": "Campbell's",
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "VZ": "Verizon",
}


def main():
    for ticker, name in TICKERS.items():
        data = yf.download(ticker, period="1mo", interval="1d", auto_adjust=True, progress=False)
        print(f"\n{name} ({ticker}) - Last 10 Trading Days")
        print(data.tail(10))


if __name__ == "__main__":
    main()
