import pandas as pd
from alpha_vantage.timeseries import TimeSeries

#Alphavantage Codes##
#Nifty50 = ^NSEI
#BankNifty = ^NSEBANK
api_key = 'QWYIM8PV23DY5BE9';
scripname = "^NSEI"
#EOD DATA
ts = TimeSeries(key = api_key,output_format = 'pandas', indexing_type='integer');
#fulldata = ts.get_daily(symbol="NSE:"+scripname, outputsize = 'full');

def eoddata():
    eoddata = ts.get_daily(symbol="NSE:"+scripname, outputsize = 'full');
    fdf = pd.DataFrame(eoddata[0]);
    fdf.dropna(inplace = True);
    fdf = fdf[fdf['5. volume']>1];
    #fdf.to_csv('PUT THE PATH HERE',sep = ',');
    fdf.to_csv('D:\\Python Exercices\\',sep = ',');

#INTRADAY DATA
def intraday():
    intradaydata = ts.get_intraday(symbol="NSE:"+scripname, outputsize = 'full');
    fdf = pd.DataFrame(intradaydata[0]);
    fdf.dropna(inplace = True);
    fdf = fdf[fdf['5. volume']>1];
    fdf.to_csv('D:\\Python Exercices\\',sep = ',');
