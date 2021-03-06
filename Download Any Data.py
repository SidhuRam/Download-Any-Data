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
   symbol = scripname+".NS"
    
ts = TimeSeries(key = api_key,output_format = 'pandas', indexing_type='integer');

#EOD DATA
def eoddata(symbol):
    eoddata = ts.get_daily(symbol=symbol, outputsize = 'full');
    eoddf = pd.DataFrame(eoddata[0]);
    eoddf.dropna(inplace = True);
    eoddf.columns =['Date','Open','High','Low','Close','Volume']
    eoddf.sort_values(by='Date', ascending=True, inplace = True)
    eoddf = eoddf[eoddf['Volume']>1];
    #fdf.to_csv('PUT THE PATH HERE',sep = ',');
    eoddf.to_csv('C:\\Python Exercises\\DataFiles\\'+symbol+'_EODData.csv',sep = ',');
                  
#INTRADAY DATA
def intraday(symbol,intratimeframe):
    intradaydata = ts.get_intraday(symbol=symbol,interval = intratimeframe,outputsize = 'full');
    intradf = pd.DataFrame(intradaydata[0]);
    intradf.dropna(inplace = True);
    intradf.columns =['Date','Open','High','Low','Close','Volume']
    intradf.sort_values(by='Date', ascending=True, inplace = True)
    intradf.to_csv('C:\\Python Exercises\\DataFiles\\'+symbol+'_'+intratimeframe+'_IntradayData.csv',sep = ',');



#Call this function for EOD DATA
eoddata(symbol);
################################
#Call this function for Intraday Data:
intraday(symbol,intratimeframe);
