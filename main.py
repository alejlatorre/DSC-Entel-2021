 # %% 0. Librerias
import pandas as pd 
import numpy as np 
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

# %%
df.to_csv(out_path + 'file_with_state.csv')
# %%
