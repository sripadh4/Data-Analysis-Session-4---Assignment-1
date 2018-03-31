
# coding: utf-8

# In[36]:

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
tempdf = pd.DataFrame()
tempdf['From'] = df['From_To'].str.split('_').str[0].str.capitalize()
tempdf['To'] = df['From_To'].str.split('_').str[1].str.capitalize()
df.pop('From_To')
df = pd.concat([df, tempdf[['From', 'To']]], axis=1)
delays = pd.DataFrame(df.RecentDelays.values.tolist())
delays.columns = ['delay_1', 'delay_2', 'delay_3']
df.pop('RecentDelays')
df = pd.concat([df, delays[['delay_1', 'delay_2', 'delay_3']]], axis=1)
df

