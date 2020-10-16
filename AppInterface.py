'''
Copyright 2020, Matthew Myrick, All rights reserved.
9/30/2020
'''
# Import Libraries
from tkinter import Tk, ttk, Button, messagebox, Label, StringVar
import tkinter as tk
from DataManagement import DataManagment
from Computation import Computation
from Widgets import Widgets

class MainApplication(tk.Frame):
    '''
    MainApplication Class Object
    argumnets:
        tk.Frame
    '''
    def __init__(self, master, **kw):
        '''
        arguments:
            master
        '''
        # Get Currency Data
        self.rawCurreniesCountries = DataManagment().currencyData()
        self.countries = self.rawCurreniesCountries[0]
        self.currencies = self.rawCurreniesCountries[1]
        self.currenciesCountries = self.rawCurreniesCountries[2]
        self.countriesCurrencies = self.rawCurreniesCountries[3]

        # Create Super Object
        super().__init__(master, **kw)
        # Initialize Tkinter Object
        self.master = master

        # Create Size of Screen
        self.master.geometry("900x600")

        # Label Title
        master.title("International Finance Application")

        # Tab Control
        self.TabControl = ttk.Notebook(self.master)

        # Call Currency Conversion Tab
        self.CurrencyConversionTab()
        # Call Bid-Ask Spread Tab Function
        self.BidAskSpreadTab()
        # Call Simple Cross Currency Tab Function
        self.SimpleCrossCurrencyTab()
        # Call Complex Cross Currency Tab Function
        self.ComplexCrossCurrencyTab()
        # Call Triangular Arbitrage Tab Function
        self.TriangularArbitrageTab()
        # Call Forwards Tab Function
        self.ForwardsTab()
        # Call Forwards Pnl Tab Function
        self.ForwardsPnlTab()

        # Pack all tabs into Window
        self.TabControl.pack(expand=1, fill="both")



    '''
    ###################################################
    BASIC CURRENCY CONVERSION TAB
    ###################################################
    '''
    def CurrencyConversionTab(self):
        '''
        This function creates the UI & UX of the Currency Conversion Tab
        '''
        # Create Currency Conversion Tab
        CurrencyConversionTab = ttk.Frame(
            self.TabControl,
            width=100, height=100
        )
        self.TabControl.add(
            CurrencyConversionTab, text="Currency Conversion"
        )

        # Create Comboboxes
        conversionCurrencyType = Widgets().ComboBox(
            tab=CurrencyConversionTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=1, columns=0, padx=10, pady=10
        )
        baseCurrencyType = Widgets().ComboBox(
            tab=CurrencyConversionTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=1, columns=1, padx=10, pady=10
        )
        inputCurrencyType = Widgets().ComboBox(
            tab=CurrencyConversionTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=1, columns=2, padx=30, pady=10
        )

        # Create labels
        ttk.Label(CurrencyConversionTab,
                  text="Select & Input Conversion Currency",
                  font=("Times New Roman", 10)).grid(
            column=0, row=0, padx=10, pady=5)
        ttk.Label(CurrencyConversionTab,
                  text="Select Base Currency",
                  font=("Times New Roman", 10)).grid(
            column=1, row=0, padx=10, pady=5)
        ttk.Label(CurrencyConversionTab,
                  text="Input Currency Conversion Amount",
                  font=("Times New Roman", 10)).grid(
            column=2, row=0, padx=10, pady=5)
        ttk.Label(CurrencyConversionTab,
                  text="Conversion\t\t",
                  font=("Times New Roman bold", 10)).grid(
            column=0, row=4, padx=10, pady=5)

        # Updated Labels
        conversionStringVar = StringVar()
        conversionLable = Label(
            CurrencyConversionTab,
            text="0.00",
            font=("Times New Roman bold", 11),
            textvariable=conversionStringVar
        ).grid(row=5, column=0)
        perStringVar = StringVar()
        perLabel = Label(
            CurrencyConversionTab,
            text="per",
            font=("Times New Roman", 10),
            textvariable=perStringVar
        ).grid(row=6, column=0)
        inputStringVar = StringVar()
        inputLabel = Label(
            CurrencyConversionTab,
            text="0.00",
            font=("Times New Roman bold", 11),
            textvariable=inputStringVar
        ).grid(row=7, column=0)

        # Create Entry Widgets
        conversionCurrencyEntry = Widgets().Entry(
            tab=CurrencyConversionTab, default="0.00", state="normal",
            row=2, column=0, padx=0, pady=0)
        baseCurrencyEntry = Widgets().Entry(
            tab=CurrencyConversionTab, default="1.00", state="readonly",
            row=2, column=1, padx=0, pady=0
        )
        conversionAmountEntry = Widgets().Entry(
            tab=CurrencyConversionTab, default="0.00", state="normal",
            row=2, column=2, padx=0, pady=0
        )

        # Conversion Button
        conversionButton = Button(
            CurrencyConversionTab, text="Convert",
            command=lambda: conversionCall()
        ).grid(
            row=3, column=1, pady=20
        )

        # Conversion Call function
        def conversionCall():
            '''
            This nested function calls the computation
            class to convert the currency, then update the program window
            '''

            # Create Try and Except Block for Error exceptions
            try:
                # Call Computation Class to Convert currency
                conversion = Computation().currencyConversion(
                    float(conversionCurrencyEntry.get()), conversionCurrencyType.get(),
                    baseCurrencyType.get(), float(conversionAmountEntry.get()),
                    inputCurrencyType.get())
                # Update tkinter Window
                conversionStringVar.set(
                    str(conversion[0])+" "+str(conversion[1])
                )
                perStringVar.set("per")
                inputStringVar.set(
                    str(conversionAmountEntry.get())+" "+str(inputCurrencyType.get())
                )
            except ZeroDivisionError:
                messagebox.showerror("Error", "Please check currencies & input boxes.")
            return

    '''
    ###################################################
    BID ASK SPREAD TAB
    ###################################################
    '''
    def BidAskSpreadTab(self):
        '''
        This function creates the UI & UX of the Bid-Ask Spread Tab
        '''
        # Create Bid Ask Spread Tab
        BidAskSpreadTab = ttk.Frame(self.TabControl)
        self.TabControl.add(BidAskSpreadTab, text="Bid-Ask Spread")

        # Create labels
        ttk.Label(BidAskSpreadTab,
                  text="Bid",
                  font=("Times New Roman", 10)).grid(
            column=1, row=1, padx=55, pady=5)
        ttk.Label(BidAskSpreadTab,
                  text="Ask",
                  font=("Times New Roman", 10)).grid(
            column=2, row=1, padx=55, pady=5)
        ttk.Label(BidAskSpreadTab,
                  text="Terms",
                  font=("Times New Roman", 10)).grid(
            column=2, row=0, padx=55, pady=5)
        ttk.Label(BidAskSpreadTab,
                  text="Exchange Amount & Type",
                  font=("Times New Roman", 10)).grid(
            column=3, row=0, padx=50, pady=5)
        ttk.Label(BidAskSpreadTab,
                  text="Computation",
                  font=("Times New Roman bold", 10)).grid(
            column=0, row=5, padx=0, pady=20)

        # Create Comboboxes
        termsCurrencyType = Widgets().ComboBox(
            tab=BidAskSpreadTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=0, columns=1, padx=10, pady=10
        )
        quoteCurrencyType = Widgets().ComboBox(
            tab=BidAskSpreadTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=2, columns=0, padx=10, pady=10
        )
        inputExchangeType = Widgets().ComboBox(
            tab=BidAskSpreadTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=1, columns=3, padx=10, pady=10
        )

        # Create Entry Widgets
        bidEntry = Widgets().Entry(
            tab=BidAskSpreadTab, default="0.00",
            state="normal", row=2, column=1, padx=20, pady=0)
        askEntry = Widgets().Entry(
            tab=BidAskSpreadTab, default="0.00",
            state="normal", row=2, column=2, padx=20, pady=0)
        exchangeEntry = Widgets().Entry(
            tab=BidAskSpreadTab, default="0.00",
            state="normal", row=2, column=3, padx=20, pady=0)

        # Create Updated Labels
        ttk.Label(BidAskSpreadTab,
                  text="Bid-Ask Spread",
                  font=("Times New Roman", 10)).grid(
            column=1, row=6, padx=20, pady=30, sticky="e")
        bidAskStringVar = StringVar()
        bidAskSpreadLabel = ttk.Label(BidAskSpreadTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=bidAskStringVar).grid(
            column=2, row=6, padx=20, pady=30, sticky="w")
        # percent bid ask spread update
        ttk.Label(BidAskSpreadTab,
                  text="Percent Bid-Ask Spread",
                  font=("Times New Roman", 10)).grid(
            column=1, row=7, padx=20, pady=30, sticky="e")
        percentBidAskStringVar = StringVar()
        perBidAskSpreadLabel = ttk.Label(BidAskSpreadTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=percentBidAskStringVar).grid(
            column=2, row=7, padx=20, pady=30, sticky="w")
        # market Maker Profit update
        ttk.Label(BidAskSpreadTab,
                  text="Market Maker Profit based on Exchange Amount",
                  font=("Times New Roman", 10), wraplength=200).grid(
            column=1, row=8, padx=20, pady=30)
        marketMakerStringVar = StringVar()
        marketMakerProfitLabel = ttk.Label(BidAskSpreadTab,
                  text="0.00", font=("Times New Roman", 10),
                  textvariable=marketMakerStringVar).grid(
            column=2, row=8, padx=20, pady=30, sticky="w")

        # Conversion Button
        conversionButton = Button(
            BidAskSpreadTab, text="Compute",
            command=lambda: computeCall()
        ).grid(
            row=4, column=3, pady=0
        )

        def computeCall():
            '''
            This nested function calls the computation
            class to solve the Bid-Ask Spread,
            then update the program window
            '''
            # Create try and accept block to handle exceptions
            global marketMakerProfit, perSpread, actSpread
            try:
                # handle conditions
                if quoteCurrencyType.get() == inputExchangeType.get():
                    # Compute arithmetic
                    spreadData = Computation().bidAskSpread(
                        bid=float(bidEntry.get()), ask=float(askEntry.get()))
                    actSpread = spreadData[0]
                    perSpread = spreadData[1]
                    marketMakerProfit = Computation().marketMakerProfit(
                        bid=float(bidEntry.get()),
                        ask=float(askEntry.get()),
                        exchangeAmount=float(exchangeEntry.get()),
                        type=1
                    )
                if termsCurrencyType.get() == inputExchangeType.get():
                    # Compute arithmetic
                    spreadData = Computation().bidAskSpread(
                        bid=float(bidEntry.get()), ask=float(askEntry.get()))
                    actSpread = spreadData[0]
                    perSpread = spreadData[1]
                    marketMakerProfit = Computation().marketMakerProfit(
                        bid=float(bidEntry.get()),
                        ask=float(askEntry.get()),
                        exchangeAmount=float(exchangeEntry.get()),
                        type=2
                    )
                # Update tkinter Window
                bidAskStringVar.set(
                    str(round(actSpread, 4))+" "+str(termsCurrencyType.get())
                )
                percentBidAskStringVar.set(
                    str(round(perSpread, 4))+" %"
                )
                marketMakerStringVar.set(
                    str(round(marketMakerProfit, 4))+" "+str(inputExchangeType.get())
                )
            except:
                messagebox.showerror("Error", "Please check currencies & input boxes.")

    '''
    ###################################################
    SIMPLE CROSS CURRENCY TAB
    ###################################################
    '''
    def SimpleCrossCurrencyTab(self):
        '''
        This function creates the UI & UX of the Complex Cross Currency Tab
        '''
        # Create Cross Currency Tab
        SimpleCrossCurrencyTab = ttk.Frame(self.TabControl)
        self.TabControl.add(SimpleCrossCurrencyTab, text="Simple Cross Currency Rate")

        # Create labels
        ttk.Label(SimpleCrossCurrencyTab,
                  text="Quotes",
                  font=("Times New Roman", 10)).grid(
            column=0, row=1, padx=55, pady=5)
        ttk.Label(SimpleCrossCurrencyTab,
                  text="Computation",
                  font=("Times New Roman bold", 10)).grid(
            column=0, row=5, padx=55, pady=5)

        # Create Entry Widgets
        exchangeEntryOne = Widgets().Entry(
            tab=SimpleCrossCurrencyTab, default="0.00",
            state="normal", row=2, column=1, padx=20, pady=0)
        termsExchangeEntryOne = Widgets().Entry(
            tab=SimpleCrossCurrencyTab, default="0.00",
            state="normal", row=2, column=2, padx=20, pady=0)
        exchangeEntryTwo = Widgets().Entry(
            tab=SimpleCrossCurrencyTab, default="0.00",
            state="normal", row=3, column=1, padx=20, pady=0)
        termsExchangeEntryTwo = Widgets().Entry(
            tab=SimpleCrossCurrencyTab, default="0.00",
            state="normal", row=3, column=2, padx=20, pady=0)

        # Create ComboBoxes
        termsCurrencyType = Widgets().ComboBox(
            tab=SimpleCrossCurrencyTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=1, columns=2, padx=10, pady=10
        )
        quoteCurrencyTypeOne = Widgets().ComboBox(
            tab=SimpleCrossCurrencyTab, data=self.currenciesCountries,
            default="GBP (British pound)",
            rows=2, columns=0, padx=10, pady=10
        )
        quoteCurrencyTypeTwo = Widgets().ComboBox(
            tab=SimpleCrossCurrencyTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=3, columns=0, padx=10, pady=10
        )

        # Computation Button
        computationButton = Button(
            SimpleCrossCurrencyTab, text="Compute",
            command=lambda: computeCall()
        ).grid(
            row=4, column=2, pady=0
        )

        # Updated Labels
        computationRowOneStringVar = StringVar()
        ttk.Label(SimpleCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=computationRowOneStringVar).grid(
            column=1, row=6, padx=55, pady=5)
        computationRowTwoStringVar = StringVar()
        ttk.Label(SimpleCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=computationRowTwoStringVar).grid(
            column=1, row=7, padx=55, pady=5)
        # Quotes
        quoteRowOneStringVar = StringVar()
        ttk.Label(SimpleCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteRowOneStringVar).grid(
            column=0, row=6, padx=55, pady=5)
        quoteRowTwoStringVar = StringVar()
        ttk.Label(SimpleCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteRowTwoStringVar).grid(
            column=0, row=7, padx=55, pady=5)

        def computeCall():
            '''
            This nested function calls the computation
            class to solve the Simple Cross Currency,
            then update the program window
            '''
            # Get data
            simpleCrossRateData = Computation().crossRateSimple(
                float(exchangeEntryOne.get()), float(termsExchangeEntryOne.get()),
                float(exchangeEntryTwo.get()), float(termsExchangeEntryTwo.get())
            )
            # Update Widgets
                # Computation
            computationRowOneStringVar.set(simpleCrossRateData[0])
            computationRowTwoStringVar.set(simpleCrossRateData[1])
                # Quotes
            quoteRowOneStringVar.set(quoteCurrencyTypeOne.get() + " / " + quoteCurrencyTypeTwo.get())
            quoteRowTwoStringVar.set(quoteCurrencyTypeTwo.get() + " / " + quoteCurrencyTypeOne.get())

    '''
    ###################################################
    COMPLEX CROSS CURRENCY TAB
    ###################################################
    '''
    def ComplexCrossCurrencyTab(self):
        '''
        This function creates the UI & UX of the Complex Cross Currency Tab
        '''
        # Create Cross Currency Tab
        ComplexCrossCurrencyTab = ttk.Frame(self.TabControl)
        self.TabControl.add(ComplexCrossCurrencyTab, text="Complex Cross Currency Rate")

        # Create Labels for tale
        # Create labels
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Quotes",
                  font=("Times New Roman", 10)).grid(
            column=0, row=1, padx=55, pady=5)
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Bid",
                  font=("Times New Roman", 10)).grid(
            column=1, row=1, padx=55, pady=5)
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Ask",
                  font=("Times New Roman", 10)).grid(
            column=2, row=1, padx=55, pady=5)
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Bid",
                  font=("Times New Roman", 10)).grid(
            column=3, row=1, padx=55, pady=5)
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Ask",
                  font=("Times New Roman", 10)).grid(
            column=4, row=1, padx=55, pady=5)
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Terms",
                  font=("Times New Roman", 10)).grid(
            column=2, row=0, padx=55, pady=5, sticky='w')
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Terms",
                  font=("Times New Roman", 10)).grid(
            column=4, row=0, padx=55, pady=5, sticky='w')
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Cross Currency",
                  font=("Times New Roman", 10)).grid(
            column=3, row=0, padx=55, pady=5, sticky='e')
        ttk.Label(ComplexCrossCurrencyTab,
                  text="Computation",
                  font=("Times New Roman bold", 10)).grid(
            column=0, row=6, padx=55, pady=5)

        # Create Entry Widgets
        bidEntryOne = Widgets().Entry(
            tab=ComplexCrossCurrencyTab, default="0.00",
            state="normal", row=2, column=1, padx=20, pady=0)
        askEntryOne = Widgets().Entry(
            tab=ComplexCrossCurrencyTab, default="0.00",
            state="normal", row=2, column=2, padx=20, pady=0)
        bidEntryTwo = Widgets().Entry(
            tab=ComplexCrossCurrencyTab, default="0.00",
            state="normal", row=3, column=1, padx=20, pady=20)
        askEntryTwo = Widgets().Entry(
            tab=ComplexCrossCurrencyTab, default="0.00",
            state="normal", row=3, column=2, padx=20, pady=20)

        # Create Comboboxes
        termsCurrencyTypeOne = Widgets().ComboBox(
            tab=ComplexCrossCurrencyTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=0, columns=1, padx=10, pady=10
        )
        quoteCurrencyTypeOne = Widgets().ComboBox(
            tab=ComplexCrossCurrencyTab, data=self.currenciesCountries,
            default="GBP (British pound)",
            rows=2, columns=0, padx=10, pady=10
        )
        quoteCurrencyTypeTwo = Widgets().ComboBox(
            tab=ComplexCrossCurrencyTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=3, columns=0, padx=10, pady=10
        )

        # Computation Button
        computationButton = Button(
            ComplexCrossCurrencyTab, text="Compute",
            command=lambda: computeCall()
        ).grid(
            row=5, column=2, pady=0
        )

        # Create Updated Labels
        # Currencies
        currenciesStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=currenciesStringVar).grid(
            column=0, row=7, padx=20, pady=30)
        # Quotes
        quoteOneBidStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteOneBidStringVar).grid(
            column=3, row=2, padx=20, pady=30)
        quoteOneAskStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteOneAskStringVar).grid(
            column=4, row=2, padx=20, pady=30)
        quoteTwoBidStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteTwoBidStringVar).grid(
            column=3, row=3, padx=20, pady=30)
        quoteTwoAskStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=quoteTwoAskStringVar).grid(
            column=4, row=3, padx=20, pady=30)

        # Computation Row One Updated Labels
        firstComputeBidOneStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=firstComputeBidOneStringVar).grid(
            column=1, row=7, padx=20, pady=30)
        firstComputeAskOneStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=firstComputeAskOneStringVar).grid(
            column=2, row=7, padx=20, pady=30)
        firstComputeBidTwoStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=firstComputeBidTwoStringVar).grid(
            column=3, row=7, padx=20, pady=30)
        firstComputeAskTwoStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=firstComputeAskTwoStringVar).grid(
            column=4, row=7, padx=20, pady=30)

        # Bid Ask Spread
        bidAskSpreadLabelStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=bidAskSpreadLabelStringVar).grid(
            column=0, row=8, padx=20, pady=30)
        bidAskSpreadOneStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=bidAskSpreadOneStringVar).grid(
            column=2, row=8, padx=20, pady=30)
        bidAskSpreadTwoStringVar = StringVar()
        ttk.Label(ComplexCrossCurrencyTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=bidAskSpreadTwoStringVar).grid(
            column=4, row=8, padx=20, pady=30)

        def computeCall():
            '''
            This nested function calls the computation
            class to solve the Bid-Ask Spread,
            then update the program window
            '''
            try:
                # Call Computation to get the Cross Curreny Data
                crossCurrencyData = Computation().crossRateComplex(
                    float(bidEntryOne.get()), float(askEntryOne.get()),
                    float(bidEntryTwo.get()), float(askEntryTwo.get()))

                # Update Widgets
                # Currencies Labels
                currenciesStringVar.set(
                    quoteCurrencyTypeTwo.get() + " / " + quoteCurrencyTypeOne.get()
                )
                # Quotes
                    # First Row
                quoteOneBidStringVar.set((crossCurrencyData[0])[0])
                quoteOneAskStringVar.set((crossCurrencyData[0])[1])
                    # Second Second
                quoteTwoBidStringVar.set((crossCurrencyData[1])[0])
                quoteTwoAskStringVar.set((crossCurrencyData[1])[1])

                # Computation Section
                    # First Row
                firstComputeBidOneStringVar.set((crossCurrencyData[2])[0])
                firstComputeAskOneStringVar.set((crossCurrencyData[2])[1])
                firstComputeBidTwoStringVar.set((crossCurrencyData[2])[2])
                firstComputeAskTwoStringVar.set((crossCurrencyData[2])[3])
                    # Bid Ask Spread
                bidAskSpreadLabelStringVar.set("Bid Ask Spread %")
                bidAskSpreadOneStringVar.set(str(crossCurrencyData[3]) + " %")
                bidAskSpreadTwoStringVar.set(str(crossCurrencyData[4]) + " %")
            except:
                messagebox.showerror("Error", "Unexpected Error has occurred please try again.")
                return None

    '''
    ###################################################
    TRIANGULAR ARBITRAGE TAB
    ###################################################
    '''
    def TriangularArbitrageTab(self):
        '''
        This function creates the UI & UX of the Complex Cross Currency Tab
        '''
        # Create Cross Currency Tab
        TriangularArbitrageTab = ttk.Frame(self.TabControl)
        self.TabControl.add(TriangularArbitrageTab, text="Triangular Arbitrage")

    '''
    ###################################################
    FORWARDS TAB
    ###################################################
    '''
    def ForwardsTab(self):
        '''
        This function creates the UI & UX of the Complex Cross Currency Tab
        '''
        # Create Cross Currency Tab
        ForwardsTab = ttk.Frame(self.TabControl)
        self.TabControl.add(ForwardsTab, text="Forwards Prem/Dis")

        # Create labels
        ttk.Label(ForwardsTab,
                  text="Terms =",
                  font=("Times New Roman", 10)).grid(
            column=3, row=2, padx=55, pady=15, sticky='e')
        ttk.Label(ForwardsTab,
                  text="Spot",
                  font=("Times New Roman", 10)).grid(
            column=3, row=0, padx=55, pady=5)
        ttk.Label(ForwardsTab,
                  text="Forward",
                  font=("Times New Roman", 10)).grid(
            column=4, row=0, padx=55, pady=5)
        ttk.Label(ForwardsTab,
                  text="Days",
                  font=("Times New Roman", 10)).grid(
            column=5, row=0, padx=55, pady=5)
        ttk.Label(ForwardsTab,
                  text="Computation",
                  font=("Times New Roman", 10)).grid(
            column=0, row=3, padx=55, pady=5)

        # Create Entry Widgets
        spotEntry = Widgets().Entry(
            tab=ForwardsTab, default="0.00",
            state="normal", row=1, column=3, padx=20, pady=0)
        forwardEntry = Widgets().Entry(
            tab=ForwardsTab, default="0.00",
            state="normal", row=1, column=4, padx=20, pady=0)
        daysEntry = Widgets().Entry(
            tab=ForwardsTab, default="0.00",
            state="normal", row=1, column=5, padx=20, pady=0)

        # Currency Types
        termsType = Widgets().ComboBox(
            tab=ForwardsTab, data=["Direct Term", "Indirect Term"],
            default="Direct Term",
            rows=2, columns=4, padx=10, pady=10
        )
        currencyTypeOne = Widgets().ComboBox(
            tab=ForwardsTab, data=self.currenciesCountries,
            default="USD (United States dollar)",
            rows=1, columns=0, padx=10, pady=10
        )
        ttk.Label(ForwardsTab,
                  text=" / ",
                  font=("Times New Roman bold", 10)).grid(
            column=1, row=1, padx=0, pady=0)
        currencyTypeTwo = Widgets().ComboBox(
            tab=ForwardsTab, data=self.currenciesCountries,
            default="EUR (Euro)",
            rows=1, columns=2, padx=10, pady=10
        )

        # Computation Button
        computationButton = Button(
            ForwardsTab, text="Compute",
            command=lambda: computeCall()
        ).grid(
            row=2, column=5, pady=0
        )

        # Updated Widgets
        premDisStringVar = StringVar()
        ttk.Label(ForwardsTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=premDisStringVar).grid(
            column=0, row=4, padx=55, pady=5, sticky='e')
        forwardResultStringVar = StringVar()
        ttk.Label(ForwardsTab,
                  text="0.00",
                  font=("Times New Roman", 10),
                  textvariable=forwardResultStringVar).grid(
            column=2, row=4, padx=55, pady=5, sticky='w')

        def computeCall():
            '''
            This nested function calls the computation
            class to solve the Simple Cross Currency,
            then update the program window
            '''
            # Call Forwards data
            forwardsData = Computation().forwardsPremDis(
                float(spotEntry.get()), float(forwardEntry.get()),
                float(daysEntry.get()), str(termsType.get())
            )

            # Update Widgets Based on Computation
            premDisStringVar.set(str(forwardsData[1]))
            forwardResultStringVar.set(str(forwardsData[0]) + " %")
            return
    '''
    ###################################################
    FORWARDS TAB
    ###################################################
    '''
    def ForwardsPnlTab(self):
        '''
        This function creates the UI & UX of the Complex Cross Currency Tab
        '''
        # Create Cross Currency Tab
        ForwardsPnlTab = ttk.Frame(self.TabControl)
        self.TabControl.add(ForwardsPnlTab, text="Forwards PNL")


if __name__ == "__main__":
    # Initialize Tkinter Object
    root = Tk()
    my_app = MainApplication(root)
    # End Process
    root.mainloop()
