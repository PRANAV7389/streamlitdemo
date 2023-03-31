!pip install yfinance
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price app
## (Rakh lena na job mai apne company mai pleaseeeeeeee)

Shown are the stock closing price and volume of google!
""")

tickerSymbol = 'Googl'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id',start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
