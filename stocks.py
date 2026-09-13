# INF601 - Advanced Programming in Python
#Ray Bednara
# Mini Project 2

import os

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

TICKERS = {
    "NVDA": "Nvidia",
    "CPB": "Campbell's",
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "VZ": "Verizon",
}

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")


def fetch_last_10_days():
    dates = None
    closes = {}
    for ticker in TICKERS:
        data = yf.download(ticker, period="1mo", interval="1d", auto_adjust=True, progress=False)
        closes[ticker] = data["Close"].squeeze().tail(10)
        if dates is None:
            dates = closes[ticker].index
    return dates, closes


def main():
    os.makedirs(CHARTS_DIR, exist_ok=True)

    dates, closes = fetch_last_10_days()

    # Store the closing prices in a single numpy array: rows = tickers, cols = days
    prices = np.array([closes[ticker].to_numpy() for ticker in TICKERS])
    print("Prices array shape (tickers x days):", prices.shape)
    print(prices)

    date_labels = [d.strftime("%m/%d") for d in dates]

    for i, (ticker, name) in enumerate(TICKERS.items()):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(date_labels, prices[i], marker="o", color="tab:blue")
        ax.set_title(f"{name} ({ticker}) - Last 10 Trading Days")
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Price (USD)")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        out_path = os.path.join(CHARTS_DIR, f"{ticker}.png")
        fig.savefig(out_path)
        plt.close(fig)
        print(f"Saved {out_path}")

    # Combined comparison chart
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (ticker, name) in enumerate(TICKERS.items()):
        ax.plot(date_labels, prices[i], marker="o", label=f"{name} ({ticker})")
    ax.set_title("Closing Prices - Last 10 Trading Days")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price (USD)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    combined_path = os.path.join(CHARTS_DIR, "combined.png")
    fig.savefig(combined_path)
    plt.close(fig)
    print(f"Saved {combined_path}")


if __name__ == "__main__":
    main()
