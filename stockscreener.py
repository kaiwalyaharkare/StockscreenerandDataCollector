from datetime import datetime as  dt
from tkinter.font import names
import matplotlib
import matplotlib.pyplot as plt
from   matplotlib import style
import pandas as pd
import pandas_datareader.data as web

matplotlib.style.use('seaborn-darkgrid')

def chart(ticker,start,end,labley):   
    df = web.DataReader(ticker,'yahoo',start,end)
    plt.title( labley +  " Chart ")
    plt.ylabel("Price  "+ labley)
    plt.plot(df['Adj Close'])
    plt.show()
def Bar(ticker,start,end,labley):   
    df = web.DataReader(ticker,'yahoo',start,end)
    plt.title( labley +  " Chart ")
    plt.ylabel("Price"+ labley)
    plt.bar(df['Adj Close'])
    plt.bar()
    plt.show()

        

    


