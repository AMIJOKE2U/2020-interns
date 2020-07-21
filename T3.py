import json
import matplotlib.pyplot as plt
from datetime import datetime
#import collections
import numpy as np

with open('data.json') as f:
    data=json.load(f)

with open('latest-rates.json') as f1:
    data1=json.load(f1)
INR_lrate=data1['rates']['INR']
GBP_lrate=data1['rates']['GBP']


fetch_rate1=dict()
fetch_rate2=dict()



for i in data['rates']:
    date=datetime.strptime(i,'%Y-%m-%d').date()
    if(date.month==1 and date.year==2019):
        fetch_rate1[date.day]=data['rates'][str(i)]['INR']
        fetch_rate2[date.day]=data['rates'][str(i)]['GBP']
        
INR_plot=sorted(fetch_rate1.items())
GBP_plot=sorted(fetch_rate2.items())
date,rates1=zip(*INR_plot)
date,rates2=zip(*GBP_plot)
plt.plot(date,rates1, label='Current INR Rate-'+str(INR_lrate))
plt.plot(date,rates2, label='Current INR Rate-'+str(GBP_lrate))
#plt.plot(label='Current INR Rate-'+str(INR_lrate))
plt.xlabel('Dates of Jan 2019')
plt.xticks(np.arange(32),rotation=90)
plt.ylabel('Rates of Jan 2019')
plt.title('Excange rate of INR and GBP against EUR')
plt.legend()
plt.show()




