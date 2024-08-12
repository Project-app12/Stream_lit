

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Stock Market Tips")

# Sidebar for user input
st.sidebar.header("User Input")

# Function to get user input
def user_input_features():
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AAPL")
    return stock_symbol

stock_symbol = user_input_features()

# Sample data for stock tips
tips_data = {
    "Stock Symbol": ["AAPL", "GOOGL", "AMZN", "MSFT"],
    "Tip": [
        "Consider buying on dips.",
        "Watch for earnings reports.",
        "Diversify your portfolio.",
        "Invest for the long term."
    ]
}

tips_df = pd.DataFrame(tips_data)

# Display tips based on user input
if stock_symbol in tips_df["
