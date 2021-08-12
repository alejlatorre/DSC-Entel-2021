 # %% 0. Librerias
import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# %% Datos
in_path = 'data/in/'
out_path = 'data/out/'

filename = 'train.csv'
df = pd.read_csv(in_path + filename)

df.columns = map(str.lower, df.columns)
df.columns = map(str.strip, df.columns)

# %% 
geolocator = Nominatim(user_agent='scrapping_location')

def get_region_from_geo(latitude, longitude):
    try:
        return geolocator.reverse(str(latitude) + ', ' + str(longitude)).raw['address']['state']
    except:
        return np.nan

# %%
df['region_origen'] = df.apply(lambda x: get_region_from_geo(str(x['latitud_origen']), str(x['longitud_origen'])), axis=1)
df['region_destino'] = df.apply(lambda x: get_region_from_geo(str(x['latitud_destino']), str(x['longitud_destino'])), axis=1)
df.loc[df.region_origen.isnull(), 'region_origen'] = 'Callao'
df.loc[df.region_destino.isnull(), 'region_destino'] = 'Lima'

# %%
# df.to_csv(out_path + 'file_.csv')

# %%
# region_origen = []
# region_destino = []
# for i, row in df[df.region_origen.isnull()].iterrows():
#     region_origen.append(geolocator.reverse(str(row['latitud_origen']) + ',' + str(row['longitud_origen'])).raw['address']['city'])
# for i, row in df[df.region_destino.isnull()].iterrows():
#     try:
#         region_destino.append(geolocator.reverse(str(row['latitud_destino']) + ',' + str(row['longitud_destino'])).raw['address']['region'])
#     except:
#         np.nan

# %%
plt.figure(figsize=(15, 15))
sns.heatmap(pd.crosstab(df.region_origen, df.region_destino))
plt.show()

