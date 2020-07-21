import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



new_s_date=input(' Enter A Start Date For Ex: "2019-01-01": ')
new_e_date=input(' Enter A End Date For Ex: "2019-01-01": ')


url1='https://api.exchangeratesapi.io/history?start_at={}&end_at={}'.format(new_s_date,new_e_date)
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
    fetch_rate1[date.day]=data['rates'][str(i)]['INR']
    fetch_rate2[date.day]=data['rates'][str(i)]['GBP']

INR_plot=sorted(fetch_rate1.items())
GBP_plot=sorted(fetch_rate2.items())

dates,rates1=zip(*INR_plot)
dates,rates2=zip(*GBP_plot)

plt.figure(figsize=(20,20))
plt.plot(dates,rates1,label='Current INR Rate-'+str(max(rates1)))
plt.plot(dates,rates2,label='Current GBP Rate-'+str(max(rates2)))

plt.xlabel('Dates From '+new_s_date+" to "+new_e_date)
plt.ylabel('Rates of Jan 2019')
plt.xticks(np.arange(32),rotation=90)
plt.title('Exchange rate of INR and GBP against EUR')
plt.legend()
plt.show()
