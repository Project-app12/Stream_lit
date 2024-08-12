import streamlit as st
import yfinance as yf
import datetime

# Set up the page title and sidebar
st.set_page_config(page_title="Stock Market Tips", layout="wide")

st.title("Stock Market Tips")
st.write("Get the latest stock market tips and insights!")

# Sidebar inputs for stock symbol and date range
with st.sidebar:
    st.header("Input Options")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL")
    start_date = st.date_input("Start Date", datetime.date(2022, 1, 1))
    end_date = st.date_input("End Date", datetime.date.today())

# Fetch stock data from Yahoo Finance
def get_stock_data(symbol, start, end):
    stock_data = yf.download(symbol, start=start, end=end)
    return stock_data

# Display stock data and analysis
if st.button("Get Stock Data"):
    try:
        stock_data = get_stock_data(stock_symbol, start_date, end_date)
        st.subheader(f"Stock Data for {stock_symbol}")
        st.line_chart(stock_data['Close'])
        st.write(stock_data.tail())

        st.subheader("Basic Stock Analysis")
        st.write(f"**Current Price**: ${stock_data['Close'][-1]:.2f}")
        st.write(f"**Moving Average (50 days)**: ${stock_data['Close'].rolling(50).mean()[-1]:.2f}")
        st.write(f"**Moving Average (200 days)**: ${stock_data['Close'].rolling(200).mean()[-1]:.2f}")

        # Example tip based on moving averages
        if stock_data['Close'][-1] > stock_data['Close'].rolling(50).mean()[-1]:
            st.success("Tip: The stock is trading above its 50-day moving average, which may indicate a bullish trend.")
        else:
            st.warning("Tip: The stock is trading below its 50-day moving average, which may indicate a bearish trend.")
    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {e}")

st.write("Note: Always do your own research or consult a financial advisor before making investment decisions.")
