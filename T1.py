import json
import matplotlib.pyplot as plt
from datetime import datetime
import collections
import numpy as np

with open('data.json') as f:
    data=json.load(f)

#start_d=datetime(2019,01,01)
#end_d=datetime(2019,01,31)

fetch_rate=dict()
for i in data['rates']:
    date=datetime.strptime(i,'%Y-%m-%d').date()
    if(date.month==1 and date.year==2019):
        fetch_rate[date.day]=data['rates'][str(i)]['INR']
        
plot_graph=sorted(fetch_rate.items())
date,rates=zip(*plot_graph)
plt.plot(date,rates,linestyle='solid')
plt.xlabel('Dates of Jan 2019')
plt.xticks(np.arange(32),rotation=90)
plt.ylabel('Rates of Jan 2019')
plt.title('Excange rate of INR against EUR')
plt.show()
