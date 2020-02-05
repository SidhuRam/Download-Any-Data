#Alphavantage Codes##
#Nifty50 = ^NSEI
#BankNifty = ^NSEBANK

import pandas as pd
from alpha_vantage.timeseries import TimeSeries

api_key = 'QWYIM8PV23DY5BE9';

### INITIALIZE THE STOCK NAME HERE -- ####
scripname = "^NSEI"
##########################################

#Available intraday timeframes = 1min, 5min,15min, 30min, 60min
### INTIATIZE INTRADAY TIMEFRAME HERE ---- ###
intratimeframe = '30min'

if scripname == "^NSEI":
    symbol = scripname
elif scripname == "^NSEBANK":
    symbol = scripname
else:
   symbol = "NSE:"+scripname
    
ts = TimeSeries(key = api_key,output_format = 'pandas', indexing_type='integer');

#EOD DATA
def eoddata(symbol):
    eoddata = ts.get_daily(symbol=symbol, outputsize = 'full');
    eoddf = pd.DataFrame(eoddata[0]);
    eoddf.dropna(inplace = True);
    eoddf = eoddf[eoddf['5. volume']>1];
    #fdf.to_csv('PUT THE PATH HERE',sep = ',');
    eoddf.to_csv('D:\\Python Exercices\\DataFiles\\EODData.csv',sep = ',');

#INTRADAY DATA
def intraday(symbol,intratimeframe):
    intradaydata = ts.get_intraday(symbol=symbol,interval = intratimeframe,outputsize = 'full');
    intradf = pd.DataFrame(intradaydata[0]);
    intradf.dropna(inplace = True);
    intradf.to_csv('D:\\Python Exercices\\DataFiles\\IntradayData.csv',sep = ',');



#Call this function for EOD DATA
eoddata(symbol);
################################
#Call this function for Intraday Data:
intraday(symbol,intratimeframe);
