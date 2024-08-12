import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.info['regularMarketPrice']

def get_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def plot_stock_price(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title='Stock Price Over Time', xaxis_title='Date', yaxis_title='Price')
    return fig

st.title('Stock Market Tips App')

ticker = st.text_input('Enter a stock ticker (e.g., AAPL for Apple):').upper()

if ticker:
    try:
        current_price = get_stock_price(ticker)
        st.write(f"Current price of {ticker}: ${current_price:.2f}")

        data = get_stock_data(ticker)
        st.plotly_chart(plot_stock_price(data))

        # Simple moving averages
        data['SMA50'] = data['Close'].rolling(window=50).mean()
        data['SMA200'] = data['Close'].rolling(window=200).mean()

        last_price = data['Close'].iloc[-1]
        sma50 = data['SMA50'].iloc[-1]
        sma200 = data['SMA200'].iloc[-1]

        st.subheader('Stock Tips:')
        if last_price > sma50 > sma200:
            st.write("- The stock is in an uptrend. Consider buying or holding.")
        elif last_price < sma50 < sma200:
            st.write("- The stock is in a downtrend. Consider selling or avoiding.")
        else:
            st.write("- The trend is unclear. More research may be needed.")

        if data['Close'].iloc[-1] < data['Close'].iloc[-2]:
            st.write("- The stock price decreased today. It might be a buying opportunity if you're optimistic about the company.")
        else:
            st.write("- The stock price increased today. Consider taking profits if you've held the stock for a while.")

        st.write("Remember: These are simple tips. Always do thorough research and consider consulting a financial advisor before making investment decisions.")

    except Exception as e:
        st.error(f"Error: {e}. Please check the ticker symbol and try again.")
