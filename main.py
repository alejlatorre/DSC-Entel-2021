
# %% 0. Librerias
import json
import requests
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
df['region_origen'] = df.apply(lambda x: get_region_from_geo(
    str(x['latitud_origen']), str(x['longitud_origen'])), axis=1)
df['region_destino'] = df.apply(lambda x: get_region_from_geo(
    str(x['latitud_destino']), str(x['longitud_destino'])), axis=1)

# %%
df.loc[df.region_origen.isnull(), 'region_origen'] = 'Callao'
df.loc[df.region_destino.isnull(), 'region_destino'] = 'Lima'

# %%
# df.to_csv(out_path + 'file_.csv')

# %%
df = pd.read_csv(out_path + 'file_with_state.csv')

# %%
df['region_destino']


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

# %%
df.head()


# %%
list_dist = []
list_times = []
for i in df['id']:
    # Obtener coordenadas
    lon_or = df.loc[df['id'] == i, 'longitud_origen'].values[0]
    lat_or = df.loc[df['id'] == i, 'latitud_origen'].values[0]
    lon_des = df.loc[df['id'] == i, 'longitud_destino'].values[0]
    lat_des = df.loc[df['id'] == i, 'latitud_origen'].values[0]
    # Uso de api
    r = requests.get(
        f"http://router.project-osrm.org/route/v1/car/{lon_or},{lat_or};{lon_des},{lat_des}?overview=false""")
    rts = json.loads(r.content)
    route = rts.get("routes")[0]
    # almacenado de valores
    distancia = route['distance']
    tiempo = route['duration']
    list_dist.append(distancia)
    list_times.append(tiempo)
print(len(list_dist), len(list_times))

df['distancia_api'] = list_dist
df['tiempo_api'] = list_times

# %%


# %%

lon_1 = -77.12269
lat = -11.965070
lon_2 = -77.13524
lat_2 = -12.07020

# call the OSMR API
r = requests.get(
    f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat};{lon_2},{lat_2}?overview=false""")
# then you load the response using the json libray
# by default you get only one alternative so you access 0-th element of the `routes`
rts = json.loads(r.content)
route_1 = rts.get("routes")[0]
# %%


# %%


route_1
# %%
