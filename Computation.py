import math
from tkinter import messagebox

class Computation():
    def interestRateParity(
            self, spot, forward, interestDomestic, interestForeign,
            borrowedDomestic, borrowedForeign, domesticType, foreignType
    ):
        '''
        This function calculates the Interest Rate Parity
        '''
        try:
            # Calculate the right side of the equation
            rightSide = float(spot*((1+interestDomestic)/(1+interestForeign)))
            if rightSide == forward:
                arbitrage = "There is no arbitrage."
                return arbitrage
            elif rightSide < forward:
                arbitrage = \
                    "IRP is not holding, implying that a profitable arbitrage opportunity exists." \
                    "Arbitrage transaction should involve borrowing in the " + domesticType + " and lending in the " + foreignType + "."
                if borrowedDomestic > 0 and borrowedForeign > 0:
                    # calculate the profits from each country and compare
                    domesticProfit = borrowedDomestic * (1+interestDomestic)
                    foreignProfit = (borrowedForeign * (1+interestForeign)) * forward
                    profit = foreignProfit - domesticProfit
                    arbitrageProfit =  "The arbitrager still has " + str(round(profit, 2)) + " " + domesticType + \
                                       " left in the account, which is arbitrage's profit"
                    return arbitrage, arbitrageProfit
                return arbitrage, 0
            elif rightSide > forward:
                arbitrage = "IRP is not holding, implying that a profitable arbitrage opportunity exists." \
                            "Arbitrage transaction should involve borrowing in the " + foreignType + " and lending in the " + domesticType + "."
                if borrowedDomestic > 0 and borrowedForeign > 0:
                    # calculate the profits from each country and compare
                    domesticProfit = borrowedDomestic * (1 + interestDomestic)
                    foreignProfit = (borrowedForeign * (1 + interestForeign)) * forward
                    profit = domesticProfit - foreignProfit
                    arbitrageProfit = "The arbitrager still has " + str(round(profit, 2)) + " " + domesticType + \
                                      " left in the account, which is arbitrage's profit"
                    return arbitrage, arbitrageProfit
                return arbitrage, 0
        except:
            messagebox.showerror("Error", "Unknown Error. Please make sure values are inputted correctly")

    def currencyConversion(
            self, conversionCurrency, conversionCurrencyType,
            baseCurrencyType, inputCurency, inputCurencyType
    ):
        '''
        This function calculates the conversion of currencies
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

    def triangularArbitrage(
            self,
            rateA, rateATypeOne, rateATypeTwo,
            rateB, rateBTypeOne, rateBTypeTwo,
            rateC, rateCTypeOne, rateCTypeTwo,
            amount, amountType
    ):
        '''
        This function calculates the triangular arbitrage profit
        '''
        # calculate arbitrage
        impliedCrossRate = rateA * rateB
        # get the round amount from cross exchange parameter
        rateCRoundIndex = len(str(float(rateC)).split('.')[1])

        # condition handle to for implied cross rate and cross rate
        if round(impliedCrossRate, rateCRoundIndex) == rateC:
            arbitrage = "There is not arbitrage opportunity."
            return arbitrage
        # condition for implied cross rate > actual cross rate
        elif round(impliedCrossRate, rateCRoundIndex) != rateC:
            # establish variables
            amount = amount
            amountType = amountType
            arbitrageProfit = 0
            # check arbitrage type for UI
            arbitrageText = ""
            if round(impliedCrossRate, rateCRoundIndex) > rateC:
                arbitrageText = str(round(impliedCrossRate, rateCRoundIndex))+" > "+str(rateC)+" Implying Arbitrage Opportunity."
            elif round(impliedCrossRate, rateCRoundIndex) < rateC:
                arbitrageText = str(round(impliedCrossRate, rateCRoundIndex))+" < "+str(rateC)+" Implying Arbitrage Opportunity."

            # exchange A conditions
            if rateATypeOne == amountType and rateATypeTwo != amountType:
                arbitrageProfit = amount / rateA
                amountType = rateATypeTwo
            elif rateATypeOne != amountType and rateATypeTwo == amountType:
                arbitrageProfit = amount * rateA
                amountType = rateATypeOne
            else:
                messagebox.showerror("Error", "Please check Exchange A Types.")
                return None

            # exchange C conditions
            if rateCTypeOne == amountType and rateCTypeTwo != amountType:
                arbitrageProfit = arbitrageProfit / rateC
                amountType = rateCTypeTwo
            elif rateCTypeOne != amountType and rateCTypeTwo == amountType:
                arbitrageProfit = arbitrageProfit * rateC
                amountType = rateCTypeOne
            else:
                messagebox.showerror("Error", "Please check Exchange C Types.")
                return None

            # exchange B conditions
            if rateBTypeOne == amountType and rateBTypeTwo != amountType:
                arbitrageProfit = arbitrageProfit / rateB
                amountType = rateBTypeTwo
                # get actual profit
                arbitrageProfit = arbitrageProfit - amount
                return arbitrageText, round(abs(arbitrageProfit), 2), amountType
            elif rateBTypeOne != amountType and rateBTypeTwo == amountType:
                arbitrageProfit = arbitrageProfit * rateB
                amountType = rateBTypeOne
                # get actual profit
                arbitrageProfit = arbitrageProfit - amount
                return arbitrageText, round(abs(arbitrageProfit), 2), amountType
            else:
                messagebox.showerror("Error", "Please check Exchange B Types.")
                return None
