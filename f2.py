import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



new_s_date=input(' Enter A Start Date For Ex: "2019-01-01": ')
new_e_date=input(' Enter A End Date For Ex: "2019-01-01": ')
c_symbol1=input('Enter Currence Symbol for ex: "INR": ')
c_symbol2=input('Enter Currence Symbol for ex: "GBP": ')


url1='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbol={}{}'.format(new_s_date,new_e_date,c_symbol1,c_symbol2)
response=requests.get(url1)
file=response.text
data=json.loads(file)

json_obj=json.dumps(data, indent=4)
with open('data.json','w') as outfile:
    outfile.write(json_obj)


    
fetch_rate1=dict()
fetch_rate2=dict()

for i in data['rates']:
    date=datetime.strptime(i,'%Y-%m-%d').date()
    fetch_rate1[date.day]=data['rates'][str(i)][c_symbol1]
    fetch_rate2[date.day]=data['rates'][str(i)][c_symbol2]

c_symbol1_plot=sorted(fetch_rate1.items())
c_symbol2_plot=sorted(fetch_rate2.items())

dates,rates1=zip(*c_symbol1_plot)
dates,rates2=zip(*c_symbol2_plot)

plt.figure(figsize=(20,20))
plt.plot(dates,rates1,label='Current'+ c_symbol1 +'Rate-'+str(max(rates1)))
plt.plot(dates,rates2,label='Current'+ c_symbol2 +'Rate-'+str(max(rates2)))

plt.xlabel('Dates From '+new_s_date+" to "+new_e_date)
plt.ylabel('Rates of '+new_s_date+' to '+ new_e_date)
plt.xticks(np.arange(32),rotation=90)
plt.title('Exchange rate of '+ c_symbol1 + '  and ' + c_symbol2+ '  against EUR')
plt.legend()
plt.show()
