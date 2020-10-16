import math
from tkinter import messagebox

class Computation():
    def currencyConversion(
            self, conversionCurrency, conversionCurrencyType,
            baseCurrencyType, inputCurency, inputCurencyType
    ):
        '''
        TThis function calculates the conversion of currencies
        '''
        try:
            # Error Message Box Exception
            if conversionCurrencyType != inputCurencyType and baseCurrencyType != inputCurencyType:
                messagebox.showerror("Error", "Please make sure currencies match.")
                return None
            elif conversionCurrencyType == inputCurencyType and baseCurrencyType == inputCurencyType:
                messagebox.showerror("Error", "All currencies are the same please check.")
            # Convert Based on Condtions
            elif conversionCurrencyType == inputCurencyType:
                conversion = inputCurency * (1/conversionCurrency)
                return round(conversion, 4), baseCurrencyType
            elif baseCurrencyType == inputCurencyType:
                conversion = inputCurency * (conversionCurrency/1)
                return round(conversion, 4), conversionCurrencyType
            # Error Message Box Exception
            else:
                messagebox.showerror("Error", "Please make sure currencies match and every input is filled.")
                return None
        except:
            messagebox.showerror("Error", "Unknown Error Please make sure values are inputted correctly")

    def bidAskSpread(self, bid, ask):
        '''
        This function calculates the bid-ask spread and % spread
        '''
        try:
            if bid > ask:
                messagebox.showerror("Error", "Bid Price cannot be larger than Asking price")
                return None
            else:
                # calculate bid ask spread and % spread
                spread = ask - bid
                spreadPer = ((ask-bid)/ask) * 100
                return spread, spreadPer
        except:
            messagebox.showerror("Error", "Unexpected Error has occurred please try again.")
            return None

    def marketMakerProfit(self, bid, ask, exchangeAmount, type):
        '''
        This function calculates the market makers profit
        '''
        try:
            if round(float(exchangeAmount), 0) == 0:
                return 0.00
            if type == 1:
                # Calculate Market Maker Profit by calling bidAskSpread Function
                perSpread = (self.bidAskSpread(bid=bid, ask=ask))[1]
                marketMakerProfit = (perSpread/100) * exchangeAmount
                return marketMakerProfit
            if type == 2:
                # Calculate Market Maker Profit by calling bidAskSpread Function
                perSpread = (self.bidAskSpread(bid=1/ask, ask=1/bid))[1]
                marketMakerProfit = (perSpread / 100) * exchangeAmount
                return marketMakerProfit
        except:
            messagebox.showerror("Error", "Unexpected Error has occurred please try again.")
            return None

    def crossRateSimple(self, q1, q2, q3, q4):
        try:
            firstSolution = (q1/q2)*(q4/q3)
            secondSolution = (q2/q1)*(q3/q4)
            return round(firstSolution, 4), round(secondSolution, 4)
        except:
            messagebox.showerror("Error", "Please make sure the inputs are correct.")
            return None

    def crossRateComplex(self, bidOne, askOne, bidTwo, askTwo):
        if bidOne > askOne or bidTwo > askTwo:
            messagebox.showerror("Error", "Please make sure the Bid is not larger than the Ask.")
            return None
        try:
            # Compute Conversion
            bidAskQuoteOneTable = [round(1/askOne, 4), round(1/bidOne, 4)]
            bidAskQuoteTwoTable = [round(1/askTwo, 4), round(1/bidTwo, 4)]

            # Compute for first line of Computation section
            bidOneComputation = bidOne * (1/askTwo)
            askOneComputation = askOne * (1/bidTwo)
            bidTwoComputation = 1/askOneComputation
            askTwoComputation = 1/bidOneComputation
            computationFirstRow = [
                round(bidOneComputation, 4), round(askOneComputation, 4),
                round(bidTwoComputation, 4), round(askTwoComputation, 4)
            ]

            # Compute Bid - Ask Spread %
            bidAskSpreadOne = round((self.bidAskSpread(bid=computationFirstRow[0], ask=computationFirstRow[1]))[1], 4)
            bidAskSpreadTwo = round((self.bidAskSpread(bid=computationFirstRow[2], ask=computationFirstRow[3]))[1], 4)

            return bidAskQuoteOneTable, bidAskQuoteTwoTable, computationFirstRow, bidAskSpreadOne, bidAskSpreadTwo
        except:
            messagebox.showerror("Error", "Make Sure All input values are correct")
            return None

    def forwardsPremDis(self, spot, forward, days, type):
        try:
            # Discount or Premium on Forward
            global forwardType
            if spot < forward:
                forwardType = "Forward Premium"
            if spot > forward:
                forwardType = "Forward Discount"
            # Computation
            if type == "Direct Term":
                result = ((forward-spot)/spot) * (360/days) * 100
                return round(result, 4), forwardType
            if type == "Indirect Term":
                result = ((spot - forward) / forward) * (360 / days) * 100
                return round(result, 4), forwardType
        except:
            messagebox.showerror("Error", "Make Sure All input values are correct")
            return None
