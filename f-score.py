import store as st

#Profitability
def roa():
    return 1 if st.ROI > 0 else 0
    
def operating_Cash_Flow():
    return 1 if st.OperatingCashFlow > 0 else 0

def croa():
    return 1 if st.CROI > 0 else 0 

def Accruals():
    return 1 if st.Accruals > st.ROI else 0

#Leverage, Liquidity and Source of Funds
def Leverage():
    return 1 if st.LongTermDebt0 > st.LongTermDebt1 else 0

def Liquidity():
    return 1 if st.ratio0 > st.ratio1 else 0

def shares():
    return 1 if st.ShareIssued0 <= st.ShareIssued1 else 0

#Operating Efficiency
def Gross():
    return 1 if st.grossMargin0 > st.grossMargin1 else 0

# AssetTurnoverRatio
def ato():
    return 1 if st.AssetTurnoverRatio0 > st.AssetTurnoverRatio1 else 0


def sum():
    f = roa()+operating_Cash_Flow()+croa()+Accruals()+Leverage()+Liquidity()+shares()+Gross()+ato()
    print(f)

sum()