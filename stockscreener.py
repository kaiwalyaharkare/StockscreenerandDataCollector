import datetime as dt
import matplotlib.pyplot as plt
from   matplotlib import style
import pandas as pd
import pandas_datareader.data as web

def chart(ticker,start,end):   
    df = web.DataReader(ticker,'yahoo',start,end)
    plt.plot(df['Adj Close'])
    plt.show()


        

    


