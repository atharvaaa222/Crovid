import pandas as pd
import yfinance as yf

ticker = 'KECL.NS'

# Get the balance sheet data
# ROI
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalAssets = balance_sheet.loc['TotalAssets', balance_sheet.columns[0]]

financials = yf.Ticker(ticker).get_financials()
NetIncome = financials.loc['NetIncome', financials.columns[0]]
ROI = NetIncome / TotalAssets

# OperatingCashFlow
CashFlow = yf.Ticker(ticker).get_cash_flow()
OperatingCashFlow = CashFlow.loc['OperatingCashFlow', financials.columns[0]]


# Change in Return of Assets
# 0
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalAssets = balance_sheet.loc['TotalAssets', balance_sheet.columns[0]]

financials = yf.Ticker(ticker).get_financials()
NetIncome = financials.loc['NetIncome', financials.columns[0]]
ROI0 = NetIncome / TotalAssets
# 1
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalAssets = balance_sheet.loc['TotalAssets', balance_sheet.columns[1]]

financials = yf.Ticker(ticker).get_financials()
NetIncome = financials.loc['NetIncome', financials.columns[1]]
ROI1 = NetIncome / TotalAssets
CROI = ROI0 - ROI1

# Accruals
CashFlow = yf.Ticker(ticker).get_cash_flow()
OperatingCashFlow = CashFlow.loc['OperatingCashFlow', financials.columns[0]]
balance_sheet = yf.Ticker(ticker).get_balancesheet()
TotalAssets = balance_sheet.loc['TotalAssets', balance_sheet.columns[0]]
Accruals = OperatingCashFlow/TotalAssets

# Long Term Debt
balance_sheet = yf.Ticker(ticker).get_balancesheet()
LongTermDebt0 = balance_sheet.loc['LongTermDebtAndCapitalLeaseObligation', balance_sheet.columns[0]]
balance_sheet = yf.Ticker(ticker).get_balancesheet()
LongTermDebt1 = balance_sheet.loc['LongTermDebtAndCapitalLeaseObligation', balance_sheet.columns[1]]

balance_sheet = yf.Ticker(ticker).get_balancesheet()
CurrentAssets = balance_sheet.loc['CurrentAssets', balance_sheet.columns[0]]
CurrentLiabilities = balance_sheet.loc['CurrentLiabilities', balance_sheet.columns[0]]
ratio0 = CurrentAssets / CurrentLiabilities
balance_sheet = yf.Ticker(ticker).get_balancesheet()
CurrentAssets = balance_sheet.loc['CurrentAssets', balance_sheet.columns[1]]
CurrentLiabilities = balance_sheet.loc['CurrentLiabilities', balance_sheet.columns[1]]
ratio1 = CurrentAssets / CurrentLiabilities

# Share Issued
balance_sheet = yf.Ticker(ticker).get_balancesheet()
ShareIssued0 = balance_sheet.loc['ShareIssued', balance_sheet.columns[0]]
balance_sheet = yf.Ticker(ticker).get_balancesheet()
ShareIssued1 = balance_sheet.loc['ShareIssued', balance_sheet.columns[0]]

financials = yf.Ticker(ticker).get_financials()
revenue = financials.loc['TotalRevenue', financials.columns[0]]
GrossProfit = financials.loc['GrossProfit', financials.columns[0]]
cogs = revenue - GrossProfit
grossMargin0 = (revenue - cogs)/revenue
financials = yf.Ticker(ticker).get_financials()
revenue = financials.loc['TotalRevenue', financials.columns[1]]
GrossProfit = financials.loc['GrossProfit', financials.columns[1]]
cogs = revenue - GrossProfit
grossMargin1 = (revenue - cogs)/revenue



financials = yf.Ticker(ticker).get_financials()
TotalSales = financials.loc['TotalRevenue', financials.columns[0]]
AssetTurnoverRatio0 = TotalSales/TotalAssets
financials = yf.Ticker(ticker).get_financials()
TotalSales = financials.loc['TotalRevenue', financials.columns[1]]
AssetTurnoverRatio1 = TotalSales/TotalAssets










