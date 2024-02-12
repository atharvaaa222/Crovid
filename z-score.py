import pandas as pd
import yfinance as yf

ticker = 'FIVESTAR.NS'

# Get the balance sheet data
# WorkingCapital
balance_sheet = yf.Ticker(ticker).get_balancesheet()
CurrentAssets = balance_sheet.loc['CurrentAssets', balance_sheet.columns[0]]
CurrentLiabilities = balance_sheet.loc['CurrentLiabilities', balance_sheet.columns[0]]
WorkingCapital = CurrentAssets - CurrentLiabilities
print(CurrentAssets)
# TotalAssets
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalAssets = balance_sheet.loc['TotalAssets', balance_sheet.columns[0]]
print(TotalAssets)
# RetainedEarnings
balance_sheet = yf.Ticker(ticker).get_balancesheet()
RetainedEarnings = balance_sheet.loc['RetainedEarnings', balance_sheet.columns[0]]
print(RetainedEarnings)
# EBIT
financials = yf.Ticker(ticker).get_financials()
EBIT = financials.loc['EBIT', financials.columns[0]]
print(EBIT)
# Market Cap
stock = yf.Ticker(ticker).get_info()
StockPrice = stock['currentPrice']
TotalStock = stock['sharesOutstanding']
MarketCap = StockPrice * TotalStock
print(MarketCap)
# TotalLiabilitiesNetMinorityInterest
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalLiabilities = balance_sheet.loc['TotalLiabilitiesNetMinorityInterest', balance_sheet.columns[0]]
print(TotalLiabilities)
# TotalRevenue
financials = yf.Ticker(ticker).get_financials()
TotalSales = financials.loc['TotalRevenue', financials.columns[0]]
print(TotalSales)
print ("---------------------------------------------------")






















a = WorkingCapital / TotalAssets
b = RetainedEarnings / TotalAssets
c = EBIT / TotalAssets
d = MarketCap / TotalLiabilities
e = TotalSales / TotalAssets

print(a)
print(b)
print(c)
print(d)
print(e)
def z():
    z = 1.2*a + 1.4*b + 3.3*c + 0.6*d + 1.0*e
    print(z)
    
print("=================================")    
z()