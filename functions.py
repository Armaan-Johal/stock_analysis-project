from imports import *
from settings import *


def checkURL (sym):

	try: 
		runType = True
		url = 'https://financialmodelingprep.com/api/v3/profile/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		if df.empty:
			runType = False

	except:
		print('AJ Funtion checkURL() Failed')

	return runType


# get company profile
# Includes company name, ticker, sector, industry, MarketCap, Last Dividend, Beta
def getProfile (sym):
	
	try:

		url = 'https://financialmodelingprep.com/api/v3/profile/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)
	except:
		df = []
		print('AJ Function getProfile() failed :' + sym)
		
	return df


# get Key Metrics and Ratios
# Includes EV/EBITDA, P/E, P/S, P/BV, P/FCF
def getMetrics (sym):
	try:
		url = 'https://financialmodelingprep.com/api/v3/key-metrics/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'
		
		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)
	except:
		df = []
		print('AJ Function getMetrics() failed :' + sym)
		
	return df

# get a company's historical stock price
def getStock (sym):
	try:
		
		url = 'https://financialmodelingprep.com/api/v3/historical-price-full/' + sym + '?serietype=line&apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js['historical'])
		df.date = pd.to_datetime(df.date)    
		df.set_index('date', drop=True, inplace=True)
	except:
		df = []
		print('AJ Function getStock() failed :' + sym)
	return df

# get SP500 historical daily price
def getSP500Stock ():
	try:
		
		url = 'https://financialmodelingprep.com/api/v3/historical-price-full/%5EGSPC?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js['historical'])
		df.date = pd.to_datetime(df.date)    
		df.set_index('date', drop=True, inplace=True)
		
	except:
		df = []
		print('AJ Function getSP500Stock() failed')
	return df


# gets all stock names, tickers, and exchanges (NYSE, NYSE Arc, NASDAQ)
def getAllSymbols ():
	try:
		
		url = 'https://financialmodelingprep.com/api/v3/stock/list?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		screened_exchanges = ['New York Stock Exchange', 'Nasdaq Global Select', 'NASDAQ Global Market', 'NYSE American']
		df = df[df['exchange'].isin(screened_exchanges)]
		
	except:
		df = []
		print('AJ Function getAllSymbols() failed')
	return df


def getAllScreenedSymbols ():
	try:
		
		screen = 'NYSE,NASDAQ'
		url = 'https://financialmodelingprep.com/api/v3/stock-screener?exchange=' + screen + '&apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)
		
	except:
		df = []
		print('AJ Function getAllScreenedSymbols() failed')
	return df



def getDCF (sym):

	try:   
		url = 'https://financialmodelingprep.com/api/v3/profile/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js, index=range(1))

	except:
		df = []
		print('AJ Function getDCF() failed :' + sym)
		
	return df


def getFinancials (sym):
	
	try:

		url = 'https://financialmodelingprep.com/api/v3/income-statement/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		df.date = pd.to_datetime(df.date)
		df.date = df.date.dt.year
		df = df.drop_duplicates(subset=['date'], keep='first')
		df.set_index('date', drop=True, inplace=True)
		df = df.replace('', np.nan)
		
	except:
		df = []
		print('AJ Function getFinancials() failed :' + sym)

	return df


def getBS (sym):
	
	try:
		url = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f' 

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		df.date = pd.to_datetime(df.date)
		df.date = df.date.dt.year
		df.set_index('date', drop=True, inplace=True)
		df = df.replace('', np.nan)
		
	except:
		df = []
		print('AJ Function getBS() failed :' + sym)

	return df


def getCS (sym):
	
	try:
		
		url = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		df.date = pd.to_datetime(df.date) 
		df.date = df.date.dt.year
		df.set_index('date', drop=True, inplace=True)
		df = df.replace('', np.nan)
		
	except:
		df = []
		print('AJ Function getCS() failed :' + sym)

	return df 


def getTreasury10Y ():

	try:
		sym = '^TNX'
		start = dt.datetime(2020,7,1)
		end = dt.datetime.today().strftime('%Y-%m-%d')
		df = web.DataReader(sym, 'yahoo', start, end)
		tres = df['Adj Close'][-1]
		
		
	except:
		tres = 1
		print('AJ Function getTreasury10Y() failed')
	
	return tres


def getSO (sym):
	
	try:
		
		url = 'https://financialmodelingprep.com/api/v3/enterprise-values/' + sym + '?apikey=6b9e3543ba839a1f8179c1365b6e2e8f'

		data = urlopen(url).read().decode('utf-8')

		js = json.loads(data)
		df = pd.DataFrame(js)

		df.date = pd.to_datetime(df.date)
		df.date = df.date.dt.year
		df.set_index('date', drop=True, inplace=True)
		df = df.replace('', np.nan)
		df = df.numberOfShares.astype('float')
		
	except:
		df = []
		print('AJ Function getSO() failed :' + sym)

	return df


###################################################################################################################################

# Computational functions using the retrieve functions above


# Creates a dataframe with the calculated free cash flow and other metrics
def FreeCashFlow (sym):
	
	try:
	
		CS_df = getCS(sym)
		fin_df = getFinancials(sym)

		#1a
		CFO = CS_df['operatingCashFlow']
		CAPEX = CS_df['capitalExpenditure']
		FCF = CFO.add(CAPEX).head(5)

		#1b
		NetInc = fin_df['netIncome'].head(5)
		FCFR = FCF.divide(NetInc)

		#1c
		TotRev = fin_df['revenue']
		PRA1 = (TotRev[2019]-TotRev[2018])/TotRev[2018]
		PRA2 = (TotRev[2018]-TotRev[2017])/TotRev[2017]
		PRA3 = (TotRev[2017]-TotRev[2016])/TotRev[2016]
		PRA4 = (TotRev[2016]-TotRev[2015])/TotRev[2015]
		#ProjRevApr = ((0.4)*PRA1 + (0.3)*PRA2 + (0.2)*PRA3 + (0.1)*PRA4) #Gives a weight to more recent year revenues
		ProjRevApr = (PRA1 + PRA2 + PRA3 + PRA4)/4

		ProjRev_df = []
		ProjRev_df = pd.DataFrame(columns=['Projected Revenue'])
		rev = TotRev[2019]
		for i in range(4):
			rev = rev*(1+ProjRevApr)
			ProjRev_df.loc[i,'Projected Revenue']=rev

		ProjRev_df.set_index(pd.date_range('2020', periods=4, freq='Y'), drop=True, inplace=True)
		ProjRev_df['Projected Revenue'] = ProjRev_df['Projected Revenue'].astype('float')

		#1d
		netIncMarg = NetInc.head(5) / TotRev.head(5)
		netIncMarg.dropna(inplace=True)

		ProjInc_df = []
		ProjInc_df = pd.DataFrame(columns=['Projected Income'])
		#marg = netIncMarg.min()
		marg = netIncMarg.mean()
		ProjInc_df['Projected Income']= ProjRev_df['Projected Revenue']*marg
		ProjInc_df.set_index(pd.date_range('2020', periods=4, freq='Y'), drop=True, inplace=True)

		#1e
		FCFE_df = []
		FCFE_df = pd.DataFrame(columns=['Projected Free Cash Flow'])
		minFCFR = FCFR.mean()#FCFR.min()
		FCFE_df['Projected Free Cash Flow']= ProjInc_df['Projected Income']*minFCFR
		FCFE_df.set_index(pd.date_range('2020', periods=4, freq='Y'), drop=True, inplace=True)


		#Compilng all into one dataframe
		rev_Inc_FCFE_df = []
		rev_Inc_FCFE_df = pd.DataFrame(columns=['Projected Revenue', 'Net Income Margins (avg)', 'Projected Income', 'Projected Free Cash Flow'])
		rev_Inc_FCFE_df['Projected Revenue'] = ProjRev_df['Projected Revenue']
		rev_Inc_FCFE_df.loc[:,'Net Income Margins (avg)'] = marg
		rev_Inc_FCFE_df['Projected Income'] = ProjInc_df['Projected Income']
		rev_Inc_FCFE_df['Projected Free Cash Flow'] = FCFE_df['Projected Free Cash Flow']
		rev_Inc_FCFE_df.set_index(pd.date_range('2020', periods=4, freq='Y'), drop=True, inplace=True)
		rev_Inc_FCFE_df.index = rev_Inc_FCFE_df.index.year


		
	except:
		rev_Inc_FCFE_df = []
		print ('AJ Function FreeCashFlow() failed :' + sym)
		
	return rev_Inc_FCFE_df
	

# Creates a dataframe with the required rate of return
def ReqRateofReturn (sym):
	
	try: 
		#Equation = wd*rd*(1-t) + we*re

		fin_df = getFinancials(sym)
		BS_df = getBS(sym)

		#2a -- ii
		interestExpense = fin_df['interestExpense'].head(5)
		CPLTDDebt = BS_df['shortTermDebt']
		longTermDebt = BS_df['longTermDebt'].head(5)
		slDebt = CPLTDDebt + longTermDebt
		rd = interestExpense / slDebt

		incTaxExp = fin_df['incomeTaxExpense'].head(5)
		incBeforeTax = fin_df['incomeBeforeTax'].head(5)
		t = incTaxExp / incBeforeTax

		adjCostOfDebt = rd*(1-t)
		adjCostOfDebt_df = pd.DataFrame(adjCostOfDebt)
		#adjCostOfDebt_df.reset_index(inplace=True)
		adjCostOfDebt_df.columns = ['Adjusted Cost of Debt']

		#2a -- iii
		Rf = getTreasury10Y()

		beta5Y = getProfile(sym)['beta'].astype('float')[0]
		Rm = 9.0

		re = Rf + beta5Y*(Rm-Rf)
		if re >=11:
			re = 11.0
		elif re <=7:
			re = 7.0

		#2a -- iv
		#totDebt = bs_df['Total Liabilities']

		MarketCap = getProfile(sym)['mktCap'].astype('float')[0]

		totCapital = slDebt[2019] + MarketCap

		wd = slDebt[2019] / totCapital
		we = MarketCap / totCapital

		#2b
		WACC = wd + adjCostOfDebt[2019] + we*re
		RR = WACC/100
		if RR >= 0.11:
			RR = 0.11
		elif RR <= 0.07:
			RR = 0.07
		elif np.isnan(RR) == True:
			RR = 0.09

		#Compile into single dataframe
		allRR_df = []
		allRR_df = pd.DataFrame(columns=('Adjusted Cost of Debt', 
										 '10 Year Bond Rate (Rf)', 
										 'Beta (5Y)', 
										 'Expected Return of the Market (Rm)', 
										 'Market Cap', 
										 'Required Rate of Return (RR)'))

		allRR_df['Adjusted Cost of Debt'] = adjCostOfDebt_df['Adjusted Cost of Debt']
		allRR_df['10 Year Bond Rate (Rf)'] = Rf
		allRR_df['Beta (5Y)'] = beta5Y
		allRR_df['Expected Return of the Market (Rm)'] = Rm
		allRR_df['Market Cap'] = MarketCap
		allRR_df['Required Rate of Return (RR)'] = RR
		allRR_df = allRR_df[::-1].head(5)
		
	  
	except:
		
		allRR_df = []
		print ('AJ Function ReqRateofReturn() failed :' + sym)
		
	return allRR_df 


# Creates a dataframe with the calculated fair value of the security
def FairValue (sym):
	
	try:
		
		RR_df = ReqRateofReturn(sym)
		FV_df = FreeCashFlow(sym)

		#3a (already function)
		so = getSO(sym)

		#4a
		pgr = 0.025

		#5a
		RR = RR_df['Required Rate of Return (RR)'][2019]
		FCFE0 = FV_df['Projected Free Cash Flow'][2020]
		TermVal = (FCFE0*(1+pgr)) / (RR-pgr)

		#5b
		disValList = []
		for j in range(4):
			#print(i)
			i = 2020 + j
			disVal = FV_df['Projected Free Cash Flow'][i] / (1+RR)**(i+1)
			disValList.append(disVal)

		disTermVal = TermVal / (1+RR)**4
		disValList.append(disTermVal)

		#6a
		TodayValue = sum(disValList)

		#7a
		FV = TodayValue / so

		stockPrice = getProfile(sym)['price'].astype('float')[0]

		fv_list1 = [stockPrice, FV]
		MarketPremium = (stockPrice - FV) / stockPrice

		allFV_df = []
		allFV_df = pd.DataFrame(columns=['Symbol', 
										 'Date', 
										 'Shares Outstanding', 
										 'Perpetual Growth Rate', 
										 'Terminal Value', 
										 'Discounted Cash Flow', 
										 'Today Value', 
										 'Fair Value', 
										 'Current Stock Price', 
										 'Market Premium (%)'])


		

		allFV_df['Symbol'] = [sym, sym, sym, sym, sym]
		allFV_df['Date'] = pd.date_range('2020', periods=5, freq='Y')
		allFV_df['Discounted Cash Flow'] = disValList
		allFV_df.loc[0, 'Shares Outstanding'] = so[2019]
		allFV_df['Perpetual Growth Rate'] = pgr
		allFV_df.loc[4, 'Terminal Value'] = TermVal
		allFV_df.loc[0, 'Today Value'] = TodayValue
		allFV_df.loc[0, 'Fair Value'] = FV[2019]
		allFV_df.loc[0, 'Current Stock Price'] = stockPrice
		allFV_df.loc[0, 'Market Premium (%)'] = MarketPremium[2019]*100

		allFV_df.reset_index(drop=True, inplace=True)
		#allFV_df.set_index(pd.date_range('2020', periods=5, freq='Y'), drop=True, inplace=True)

	except:
		
		allFV_df = []
		print('AJ Function FairValue() failed :' + sym)
		
	return allFV_df
	

# Gets the correlation between the company and the SP500     
def getCorr_SP500 (sym, d):
	
	try:
	
		c = np.nan

		stock_df = getStock(sym)
		stock_df = stock_df['close'].head(d)
		stock_df = stock_df[~stock_df.index.duplicated()]

		##########################################################

		SP_df = getSP500Stock()
		SP_df = SP_df['adjClose'].head(d)
		SP_df = SP_df[~SP_df.index.duplicated()]

		##########################################################

		dff = pd.concat([stock_df, SP_df], axis=1)

		dff= dff.astype('float')[::-1]
		c = dff['close'].corr(dff['adjClose'])


		
	except:
		c = np.nan
		print('AJ Function getCorr_SP500() failed :' + sym)
	
	return c
	
	

# Analyzes a company's basic value using various metrics and returns a dataframe with all relevant information
def Analyze_simple (sym):

	if (checkURL(sym)):
	
		try:

			df = pd.DataFrame(index=range(1))
			profile_df = getProfile(sym)
			dcf_df = getDCF(sym)
			metrics_df = getMetrics(sym).round(4)
			fv_df = FairValue(sym)

			df['Company'] = profile_df['companyName'][0] #
			df['Ticker'] = profile_df['symbol'][0] #
			df['Sector'] = profile_df['sector'][0] #
			df['Industry'] = profile_df['industry'][0] #
			df['Market Cap (M)'] = profile_df['mktCap'][0] #
			df['Market Cap (M)']= df['Market Cap (M)'].astype('float')/1000000 #
			
			df['EV/EBITDA'] = metrics_df['enterpriseValueOverEBITDA'][0] #
			df['Price / Earnings Ratio'] = metrics_df['peRatio'][0] #
			if metrics_df['dividendYield'][0]: df['Dividend Yield (%)'] = metrics_df['dividendYield'][0]*100
			df['Current Ratio'] = metrics_df['currentRatio'][0]
			df['FCF Yield (%)'] = metrics_df['freeCashFlowYield'][0]*100
			df['Debt to Equity'] = metrics_df['debtToEquity'][0]
			df['ROE (%)'] = metrics_df['roe'][0]*100
			df['Price / Book Ratio'] = metrics_df['pbRatio'][0]
			
			df['Beta'] = profile_df['beta'][0] #
			df['30 Day SP500 Correlation'] = getCorr_SP500(sym, 21) #
			df['3 Month SP500 Correlation'] = getCorr_SP500(sym, 63)
			df['1 Year SP500 Correlation'] = getCorr_SP500(sym, 253) #
			df['3 Year SP500 Correlation'] = getCorr_SP500(sym, 759) #
			df['10 Year SP500 Correlation'] = getCorr_SP500(sym, 2530)
			df['Stock Price'] = profile_df['price'][0] #
			if dcf_df['dcf'][0] == 0:
				df['DCF Fair Value'] = np.nan
			else:
				df['DCF Fair Value'] = dcf_df['dcf'][0] #

			if fv_df['Fair Value'][0] >=0:
				df['AJ DCF Fair Value'] = fv_df['Fair Value'][0].round(3) #
				df['AJ DCF Fair Value'] = df['AJ DCF Fair Value'].replace(-np.inf, np.nan)
				df['AJ DCF Fair Value'] = df['AJ DCF Fair Value'].replace(np.inf, np.nan)
				
				fv_list = [profile_df['price'][0], dcf_df['dcf'][0]]
				df['Market Premium (%)'] = (100*(profile_df['price'][0] - df['DCF Fair Value']) / profile_df['price'][0]).round(3) #     #min(fv_list)).round(3)
				df['Market Premium (%)'] = df['Market Premium (%)'].replace(np.inf, np.nan)
				df['Market Premium (%)'] =  df['Market Premium (%)'].replace(-np.inf, np.nan)
				
				df['AJ Market Premium (%)'] = fv_df['Market Premium (%)'][0].round(3) #
				df['AJ Market Premium (%)'] = df['AJ Market Premium (%)'].replace(-np.inf, np.nan)
				df['AJ Market Premium (%)'] = df['AJ Market Premium (%)'].replace(np.inf, np.nan)
				
				df['Average Market Premium (%)'] = np.nanmean([df['AJ Market Premium (%)'][0], df['Market Premium (%)'][0]]).round(3) #    #((df['AJ Market Premium (%)']+df['Market Premium (%)'])/2).round(3)

		except:
			df = []
			print('AJ Function Analyze_simple() failed :' + sym)

		return [df, profile_df, dcf_df, metrics_df, fv_df]

	else:
		return []

	


# Analyze all the companies on the NYSE, NYSE Arc, and NASDAQ. Returns a dataframe with all relevant data (from Analyze_simple())
def Analyze_all ():

	symbols_df = getAllScreenedSymbols().head(n_securities)
	symbols_simp_df = pd.DataFrame()
	symbols_prof_df = pd.DataFrame()
	symbols_met_df = pd.DataFrame()
	symbols_f_df = pd.DataFrame()

	deleteJsonFiles ()

	for i, row in symbols_df.iterrows():
		simp_dff = []
		simp_dff = pd.DataFrame()

		try:
			sym = row.symbol
			cname = row['companyName']
			simp_dff_all = Analyze_simple(sym)
			if len(simp_dff_all) == 0:
				continue
			else:
				simp_dff = simp_dff_all[0]
				simp_dff['Exchange'] = row['exchange']

				prof_df = simp_dff_all[1]
				met_df = simp_dff_all[3]
				f_df = simp_dff_all[4]

				symbols_simp_df = symbols_simp_df.append(simp_dff, ignore_index=True)
				symbols_prof_df = symbols_prof_df.append(prof_df, ignore_index=True)
				symbols_met_df = symbols_met_df.append(met_df, ignore_index=True)
				symbols_f_df = symbols_f_df.append(f_df, ignore_index=True)

				print([sym, cname])
			
		except:
			print("Error " + row.symbol + ": " + row['companyName']+ "\n")
			continue

			
	float_cols = ['Market Cap (M)', 'EV/EBITDA', 'Price / Earnings Ratio', 'Beta', '30 Day SP500 Correlation', '1 Year SP500 Correlation', '3 Year SP500 Correlation', 'Stock Price', 'DCF Fair Value', 'AJ DCF Fair Value', 'Market Premium (%)', 'AJ Market Premium (%)', 'Average Market Premium (%)', 'Dividend Yield (%)', 'Current Ratio', 'FCF Yield (%)', 'Debt to Equity', 'ROE (%)', 'Price / Book Ratio', '3 Month SP500 Correlation', '10 Year SP500 Correlation']
	symbols_simp_df[float_cols] = symbols_simp_df[float_cols].astype('float').round(2)
	symbols_simp_df = symbols_simp_df.head(len(symbols_simp_df)).sort_values(by=['Market Cap (M)'], ascending=False)

	#symbols_simp_df = symbols_simp_df[abs(symbols_simp_df['Average Market Premium (%)']) <= 500]
	symbols_simp_df.reset_index(drop=True, inplace=True)

	cols = ['Company', 
		'Ticker',
		'Exchange',
		'Sector', 
		'Industry',
		'Market Cap (M)',
		'EV/EBITDA', 
		'Price / Earnings Ratio', 
		'Beta',
		'30 Day SP500 Correlation',
		'3 Month SP500 Correlation',
		'1 Year SP500 Correlation', 
		'3 Year SP500 Correlation',
		'10 Year SP500 Correlation',
		'Stock Price',
		'DCF Fair Value', 
		'AJ DCF Fair Value',
		'Market Premium (%)',
		'AJ Market Premium (%)',
		'Average Market Premium (%)',
		'Dividend Yield (%)',
		'Current Ratio',
		'FCF Yield (%)',
		'Debt to Equity',
		'ROE (%)',
		'Price / Book Ratio',
	   ]

	df = symbols_simp_df[cols]
	df = df.replace(-np.inf, np.nan)
	df = df.replace(np.inf, np.nan)


	df_jsonFile = jsonPath + 'df.json'
	profile_df_jsonFile = jsonPath + 'profile_df.json'
	metrics_df_jsonFile = jsonPath + 'metrics_df.json'
	fv_df_jsonFile = jsonPath + 'fv_df.json'

	df.to_json(df_jsonFile)
	symbols_prof_df.to_json(profile_df_jsonFile)
	symbols_met_df.to_json(metrics_df_jsonFile)
	symbols_f_df.to_json(fv_df_jsonFile)



	
	return df, symbols_prof_df, symbols_met_df, symbols_f_df





def round_df (df, n):

	if len(df)>0:
		new_df = df.round(int(n))
	else:
		new_df = []

	return new_df




def Analyze_simple_file (sym, exc):
	
	#try:
	df = pd.DataFrame(index=range(1))
	profile_df = getProfile(sym)
	dcf_df = getDCF(sym)
	metrics_df = getMetrics(sym).round(4)
	fv_df = FairValue(sym)

	df['Company'] = profile_df['companyName'][0] #
	df['Ticker'] = profile_df['symbol'][0] #
	df['Exchange'] = exc
	df['Sector'] = profile_df['sector'][0] #
	df['Industry'] = profile_df['industry'][0] #
	df['Market Cap (M)'] = profile_df['mktCap'][0] #
	df['Market Cap (M)']= df['Market Cap (M)'].astype('float')/1000000 #
	
	df['EV/EBITDA'] = metrics_df['enterpriseValueOverEBITDA'][0] #
	df['Price / Earnings Ratio'] = metrics_df['peRatio'][0] #
	if metrics_df['dividendYield'][0]: df['Dividend Yield (%)'] = metrics_df['dividendYield'][0]*100
	df['Current Ratio'] = metrics_df['currentRatio'][0]
	df['FCF Yield (%)'] = metrics_df['freeCashFlowYield'][0]*100
	df['Debt to Equity'] = metrics_df['debtToEquity'][0]
	df['ROE (%)'] = metrics_df['roe'][0]*100
	df['Price / Book Ratio'] = metrics_df['pbRatio'][0]
	
	df['Beta'] = profile_df['beta'][0] #
	df['30 Day SP500 Correlation'] = getCorr_SP500(sym, 21) #
	df['3 Month SP500 Correlation'] = getCorr_SP500(sym, 63)
	df['1 Year SP500 Correlation'] = getCorr_SP500(sym, 253) #
	df['3 Year SP500 Correlation'] = getCorr_SP500(sym, 759) #
	df['10 Year SP500 Correlation'] = getCorr_SP500(sym, 2530)
	df['Stock Price'] = profile_df['price'][0] #
	if dcf_df['dcf'][0] == 0:
		df['DCF Fair Value'] = np.nan
	else:
		df['DCF Fair Value'] = dcf_df['dcf'][0] #

	if fv_df['Fair Value'][0] >=0:
		df['AJ DCF Fair Value'] = fv_df['Fair Value'][0].round(3) #
		df['AJ DCF Fair Value'] = df['AJ DCF Fair Value'].replace(-np.inf, np.nan)
		df['AJ DCF Fair Value'] = df['AJ DCF Fair Value'].replace(np.inf, np.nan)
		
		fv_list = [profile_df['price'][0], dcf_df['dcf'][0]]
		df['Market Premium (%)'] = (100*(profile_df['price'][0] - df['DCF Fair Value']) / profile_df['price'][0]).round(3) #     #min(fv_list)).round(3)
		df['Market Premium (%)'] = df['Market Premium (%)'].replace(np.inf, np.nan)
		df['Market Premium (%)'] =  df['Market Premium (%)'].replace(-np.inf, np.nan)
		
		df['AJ Market Premium (%)'] = fv_df['Market Premium (%)'][0].round(3) #
		df['AJ Market Premium (%)'] = df['AJ Market Premium (%)'].replace(-np.inf, np.nan)
		df['AJ Market Premium (%)'] = df['AJ Market Premium (%)'].replace(np.inf, np.nan)
		
		df['Average Market Premium (%)'] = np.nanmean([df['AJ Market Premium (%)'][0], df['Market Premium (%)'][0]]).round(3) #    #((df['AJ Market Premium (%)']+df['Market Premium (%)'])/2).round(3)




	#appending dataframes to json
	df_jsonFile = jsonPath + 'df.json'
	profile_df_jsonFile = jsonPath + 'profile_df.json'
	dcf_df_jsonFile = jsonPath + 'dcf_df.json'
	metrics_df_jsonFile = jsonPath + 'metrics_df.json'
	fv_df_jsonFile = jsonPath + 'fv_df.json'

	appendDF(df, df_jsonFile)
	appendDF(profile_df, profile_df_jsonFile)
	appendDF(dcf_df, dcf_df_jsonFile)
	appendDF(metrics_df, metrics_df_jsonFile)
	appendDF(fv_df, fv_df_jsonFile)


	# except Exception as ex:
	# 	df = []
	# 	print('AJ Function Analyze_simple_file() failed :' + sym)

	return



def fixDateTimeAsString (df):
	datetime_cols = [col for col in df.columns if df[col].dtype == 'datetime64[ns]']
	df[datetime_cols] = df[datetime_cols].astype(str)
	return df



def appendDF (df, jsonFile):

	try:

		if 'Date' in df.columns:
			df.Date = pd.to_datetime(df.Date)
		if 'date' in df.columns:
			df.date = pd.to_datetime(df.date)

		if not os.path.isfile(jsonFile):
			df_json = df.to_json(date_unit='ns')
			with open(jsonFile, mode='w') as f:
				f.write(df_json)
		else:
			prev_df = pd.read_json(jsonFile)
			df_json = df.to_json(date_unit='ns')
			new_df = pd.DataFrame(json.loads(df_json))
			all_df = pd.concat([prev_df, new_df], ignore_index=True)
			all_df_json = all_df.to_json(date_unit='ns')
			all_df_df = pd.DataFrame(json.loads(all_df_json))

			#Write too file
			all_df_df.to_json(jsonFile)

	except:
		print('AJ Function appendDF() failed')

	return




def deleteJsonFiles ():

	df_jsonFile = jsonPath + 'df.json'
	profile_df_jsonFile = jsonPath + 'profile_df.json'
	dcf_df_jsonFile = jsonPath + 'dcf_df.json'
	metrics_df_jsonFile = jsonPath + 'metrics_df.json'
	fv_df_jsonFile = jsonPath + 'fv_df.json'

	cmd = 'rm ' + df_jsonFile + ' ' + profile_df_jsonFile + ' ' + dcf_df_jsonFile + ' ' + metrics_df_jsonFile + ' ' + fv_df_jsonFile

	os.system(cmd)

	return






def Analyze_simple_wrapper (sym, exc):

	simp_dff_all = Analyze_simple_file(sym, exc)

	return



def Analyze_all_MP ():


	symbols_df = getAllScreenedSymbols().head(n_securities)
	symbols_simp_df = pd.DataFrame()
	symbols_prof_df = pd.DataFrame()
	symbols_met_df = pd.DataFrame()
	symbols_f_df = pd.DataFrame()

	processes = []

	deleteJsonFiles ()

	try:

		for i, row in symbols_df.iterrows():
			simp_dff = []
			simp_dff = pd.DataFrame()

			sym = row.symbol
			cname = row['name']
			exc = row['exchange']


			p = multiprocessing.Process(target=Analyze_simple_wrapper, args=(sym, exc,))
			processes.append(p)
			p.start()

			time.sleep(5)

			print([sym, cname])

		for p in processes:
			p.join()
			
	except:
		print("Error " + row.symbol + ": " + row['name']+ "\n")
		#continue

	df_jsonFile = jsonPath + 'df.json'
	profile_df_jsonFile = jsonPath + 'profile_df.json'
	dcf_df_jsonFile = jsonPath + 'dcf_df.json'
	metrics_df_jsonFile = jsonPath + 'metrics_df.json'
	fv_df_jsonFile = jsonPath + 'fv_df.json'

	symbols_simp_df = pd.read_json(df_jsonFile)
	symbols_prof_df = pd.read_json(profile_df_jsonFile)
	symbols_dcf_df = pd.read_json(dcf_df_jsonFile)
	symbols_met_df = pd.read_json(metrics_df_jsonFile)
	symbols_f_df = pd.read_json(fv_df_jsonFile)

			
	float_cols = ['Market Cap (M)', 'EV/EBITDA', 'Price / Earnings Ratio', 'Beta', '30 Day SP500 Correlation', '1 Year SP500 Correlation', '3 Year SP500 Correlation', 'Stock Price', 'DCF Fair Value', 'AJ DCF Fair Value', 'Market Premium (%)', 'AJ Market Premium (%)', 'Average Market Premium (%)', 'Dividend Yield (%)', 'Current Ratio', 'FCF Yield (%)', 'Debt to Equity', 'ROE (%)', 'Price / Book Ratio', '3 Month SP500 Correlation', '10 Year SP500 Correlation']
	symbols_simp_df[float_cols] = symbols_simp_df[float_cols].astype('float').round(2)
	symbols_simp_df = symbols_simp_df.head(len(symbols_simp_df)).sort_values(by=['Market Cap (M)'], ascending=False)

	#symbols_simp_df = symbols_simp_df[abs(symbols_simp_df['Average Market Premium (%)']) <= 500]
	symbols_simp_df.reset_index(drop=True, inplace=True)

	cols = ['Company', 
		'Ticker',
		'Exchange',
		'Sector', 
		'Industry',
		'Market Cap (M)',
		'EV/EBITDA', 
		'Price / Earnings Ratio', 
		'Beta',
		'30 Day SP500 Correlation',
		'3 Month SP500 Correlation',
		'1 Year SP500 Correlation', 
		'3 Year SP500 Correlation',
		'10 Year SP500 Correlation',
		'Stock Price',
		'DCF Fair Value', 
		'AJ DCF Fair Value',
		'Market Premium (%)',
		'AJ Market Premium (%)',
		'Average Market Premium (%)',
		'Dividend Yield (%)',
		'Current Ratio',
		'FCF Yield (%)',
		'Debt to Equity',
		'ROE (%)',
		'Price / Book Ratio',
	   ]

	df = symbols_simp_df[cols]
	df = df.replace(-np.inf, np.nan)
	df = df.replace(np.inf, np.nan)


	#ts = datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H-%M-%S')
	ts = datetime.strftime(datetime.now(), '%Y-%m-%d')

	df_jsonFile_new = df_jsonFile.replace('.json', '_'+ts+'.json')
	profile_df_jsonFile = profile_df_jsonFile.replace('.json', '_'+ts+'.json')
	dcf_df_jsonFile = dcf_df_jsonFile.replace('.json', '_'+ts+'.json')
	metrics_df_jsonFile = metrics_df_jsonFile.replace('.json', '_'+ts+'.json')
	fv_df_jsonFile = fv_df_jsonFile.replace('.json', '_'+ts+'.json')


	df.to_json(df_jsonFile_new)
	symbols_prof_df.to_json(profile_df_jsonFile)
	symbols_dcf_df.to_json(dcf_df_jsonFile)
	symbols_met_df.to_json(metrics_df_jsonFile)
	symbols_f_df.to_json(fv_df_jsonFile)
	
	return 
















