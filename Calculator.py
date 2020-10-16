import pandas

def balanceOfPaymentsIdentity():
    print("BCA = Balance on the Current Account")
    print("BKA = Blance on the Capital Account")
    print("BRA = Balance on the Reserve account")
    print("\nBCA + BKA + BRA = 0")
    print(
        "BCA > BKA = Import Country"
        "\n\t- Deficit"
        "\nBCA < BKA = Export Country"
        "\n\t- Surplus"
    )
    print("See pg 64 (87 PDF) for balance of Payments sheet")
    print("See pg 66 (89 PDF) for J-curve effect")

def parityRealizedProfit(usdInterest, otherInterest, forwardExchange, spotExchange, otherCountry):
    'usd'
    borrowedUSD = float(input("Amount borrowed(USD): "))
    capitalGainsUSD = borrowedUSD * (1+usdInterest)
    print("USD")
    print("Capital Account Balance(USD): $", capitalGainsUSD)
    print("Unrealized Gains(USD): $", capitalGainsUSD-borrowedUSD)

    'other'
    borrowedOther = borrowedUSD/spotExchange
    capitalGainsOther = borrowedOther * (1+otherInterest)
    print("\n"+otherCountry)
    print("Capital Account Balance("+otherCountry+"):", capitalGainsOther)
    print("Unrealized Gains("+otherCountry+"):", (capitalGainsOther - borrowedOther))
    otherToUSD = capitalGainsOther * forwardExchange
    print("Conversion(USD): $", otherToUSD)
    if otherToUSD == capitalGainsUSD:
        print("The two accounts are equal.")
    elif otherToUSD > capitalGainsUSD:
        print("You will save", (otherToUSD-capitalGainsUSD), "investing with", otherCountry, ".")
    elif otherToUSD < capitalGainsUSD:
        print("You will save", (capitalGainsUSD-otherToUSD), "investing with USD.")

def interestRateParity(interestLeft, forwardExchange, spotExchange, interestRight, years, otherCountry="Other Country"):
    print("**See page 164 in book for formula**\n")
    newInterestLeft = interestLeft*years
    newInterestRight = interestRight*years
    LHS = 1+(newInterestLeft)
    RHS = (forwardExchange/spotExchange) * (1+(newInterestRight))
    if RHS == LHS:
        print(RHS, "=", LHS)
        print("The IRP is holding.")
    elif LHS > RHS:
        print(LHS, ">", RHS)
        print("The IRP is not holding.")
        print("Implying a profitable arbitrage exists.")
        print("Borrow in", otherCountry, "since interest rate is lower.")
        print("Lend in the United States.")
    elif LHS < RHS:
        print(LHS, "<", RHS)
        print("The IRP is not holding.")
        print("Implying a profitable arbitrage exists.")
        print("Borrow in United States since interest rate is lower.")
        print("Lend in", otherCountry+".")
    user = input("Would you like to know realized profit in USD?\n:")
    if user.capitalize() == "Yes":
        parityRealizedProfit(newInterestLeft, newInterestRight, forwardExchange, spotExchange, otherCountry = otherCountry)
    else:
        print("Process Finished.")
