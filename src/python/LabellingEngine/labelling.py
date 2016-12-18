
# testing start date, testing period => return distribution ,
# buying date, holding periods (days), label (+, 0 , -), return band (+- h sigma)


# calculate h std of return in testing period,

#H0 = P_0*(1+(r_mean + h* sigma ))
# if P_T > H0 label as +1 ,  P_T<H0 label as -1
#

test_period = 20 # 20days
hold_period =5 #5 days
num_sigma = 2

import pandas as pd
import numpy as np
from pandas_datareader import data as pddata

df = pddata.get_data_yahoo('AAPL', '2000-01-01', '2016-07-01')
data = pddata.get_data_yahoo('AAPL', '2000-01-01', '2016-07-01')['Close']
returns = data.pct_change()

mean =returns.rolling(window=test_period).mean()
std =  returns.rolling(window=test_period).std()

label = pd.Series(0,data.index)

df = pd.DataFrame({'price':data, 'mean': mean , 'std':std ,'label':label})

#df =df.shift(periods=-test_period)

#array =pd.DataFrame(np.array(2,3))
#print (array)

df =df[test_period:]
#label_algo = lambda x: df.price +df.price*(df.mean +df.std* num_sigma )
df.iloc[:]['label']=1
print (df)

for x in range(0, len(df.index)-hold_period):
    #p0=row['price']*(1+row['mean']+num_sigma*row['std'])
    loc=df.iloc[x]
    p0=loc['price']*(1+loc['mean']+num_sigma*loc['std'])
    p1=loc['price']*(1+loc['mean']-num_sigma*loc['std'])
    if p0 > df.iloc[x+hold_period]['price']:
        df.iloc[x+hold_period-1]['label']=1

    if p1 < df.iloc[x+hold_period]['price']:
        df.iloc[x+hold_period-1]['label']=-1


print(df)