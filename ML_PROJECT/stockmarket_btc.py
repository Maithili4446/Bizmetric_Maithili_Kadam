import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_btc_data():

    ticker_symbol = "BTC-USD"
    btc = yf.Ticker(ticker_symbol)

    hist = btc.history(period="180d")
    hist = hist[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Moving Averages
    hist['MA9'] = hist['Close'].rolling(window=9).mean()
    hist['MA21'] = hist['Close'].rolling(window=21).mean()

    # Buy/Sell Logic
    hist['uptrend'] = np.where(hist['Close'] > hist['MA21'], 1, 0)
    hist['upcross'] = np.where(
        (hist['uptrend'] == 1) & (hist['uptrend'].shift(1) == 0),
        hist['Close'],
        np.nan
    )

    hist['downtrend'] = np.where(hist['Close'] < hist['MA21'], 1, 0)
    hist['downcross'] = np.where(
        (hist['downtrend'] == 1) & (hist['downtrend'].shift(1) == 0),
        hist['Close'],
        np.nan
    )

    hist.to_csv("btc_usd.csv")

    # =======================
    # PRO DASHBOARD DESIGN
    # =======================

    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,
        row_heights=[0.75, 0.25]
    )

    # Candlestick with custom colors
    fig.add_trace(go.Candlestick(
        x=hist.index,
        open=hist['Open'],
        high=hist['High'],
        low=hist['Low'],
        close=hist['Close'],
        increasing_line_color='#00ff99',
        decreasing_line_color='#ff4d4d',
        name="BTC Price"
    ), row=1, col=1)

    # MA9 (fast)
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['MA9'],
        line=dict(color='#00ffff', width=2),
        name="MA9"
    ), row=1, col=1)

    # MA21 (slow)
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['MA21'],
        line=dict(color='#ffcc00', width=2),
        name="MA21"
    ), row=1, col=1)

    # Buy markers
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['upcross'],
        mode='markers',
        marker=dict(
            size=12,
            color='#00ff99',
            symbol='triangle-up'
        ),
        name="Buy"
    ), row=1, col=1)

    # Sell markers
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['downcross'],
        mode='markers',
        marker=dict(
            size=12,
            color='#ff4d4d',
            symbol='triangle-down'
        ),
        name="Sell"
    ), row=1, col=1)

    # Volume with dynamic color
    volume_colors = np.where(hist['Close'] >= hist['Open'],
                             '#00ff99',
                             '#ff4d4d')

    fig.add_trace(go.Bar(
        x=hist.index,
        y=hist['Volume'],
        marker_color=volume_colors,
        name="Volume"
    ), row=2, col=1)

    fig.update_layout(
        template="plotly_dark",
        title={
            'text': "🚀 BTC-USD Trading Strategy Dashboard",
            'x': 0.5,
            'xanchor': 'center'
        },
        height=850,
        xaxis_rangeslider_visible=False,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )

    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    fig.show()


if __name__ == "__main__":
    get_btc_data()