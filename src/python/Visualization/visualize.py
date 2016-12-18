import matplotlib as matplot
from pandas_datareader import data as pddata
import pandas as pd
import matplotlib.pyplot as plt
#
data = pddata.get_data_yahoo('AAPL', '2016-01-01', '2016-07-01')

closeprice = data['Close']


# data.Close.pct_change() gross return of Close price

returns = data['Close'].pct_change()[1:]
mean =returns.mean()
#returns.plot()

p_return=returns[returns>=0]
n_return = returns [returns<0]

plt.plot(p_return,marker='o', linestyle='--', color='r', label='Square')
plt.plot(n_return,marker='*', linestyle='--', color='b', label='Square')
#print(mean)
plt.show()




