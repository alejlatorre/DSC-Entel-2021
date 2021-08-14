
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
df = pd.read_csv(out_path + 'file_with_state.csv')

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
df['id'].value_counts().sort_values(ascending=False)


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


df['distancia_km'] = df['distancia']/1000

# %%


# %%

df = df[df['distancia_km'] <= 275]


# %%
sns.set_style('whitegrid')
sns.boxplot(df.distancia_km)
# %%
df.shape[0]

# %%
list_dist = []
list_times = []
for i in df['id']:
    # Obtener coordenadas
    lon_or = df.loc[df['id'] == i, 'longitud_origen'].values[0]
    lat_or = df.loc[df['id'] == i, 'latitud_origen'].values[0]
    lon_des = df.loc[df['id'] == i, 'longitud_destino'].values[0]
    lat_des = df.loc[df['id'] == i, 'latitud_destino'].values[0]
    # Uso de api
    r = requests.get(
        f"http://router.project-osrm.org/route/v1/car/{lon_or},{lat_or};{lon_des},{lat_des}?overview=false""")
    rts = json.loads(r.content)
    try:
        route = rts.get("routes")[0]
        # almacenado de valores
        distancia = route['distance']
        tiempo = route['duration']
        list_dist.append(distancia)
        list_times.append(tiempo)
    except:
        list_dist.append(0)
        list_times.append(0)
print(len(list_dist), len(list_times))

df['distancia_api'] = list_dist
df['tiempo_api'] = list_times


# %%

df = df.loc[df['distancia_api'] != 0]


# %%


df.to_csv(out_path + 'file_cleaned.csv')

# %%

test_data = pd.read_csv(in_path + 'test.csv')

# %%

test_data

# %%
test_data.columns = map(str.lower, test_data.columns)
test_data.columns = map(str.strip, test_data.columns)


# %%

test_data['region_origen'] = test_data.apply(lambda x: get_region_from_geo(
    str(x['latitud_origen']), str(x['longitud_origen'])), axis=1)
test_data['region_destino'] = test_data.apply(lambda x: get_region_from_geo(
    str(x['latitud_destino']), str(x['longitud_destino'])), axis=1)


# %%

test_data.loc[test_data.region_origen.isnull(), 'region_origen'] = 'Callao'
test_data.loc[test_data.region_destino.isnull(), 'region_destino'] = 'Lima'


# %%%%


test_data.loc[(test_data['region_destino'] != test_data['region_origen']) & (
    test_data['region_destino'] != 'Lima')]


# %%

test_data.to_csv(out_path + 'test_with_states.csv')


# %%

list_dist = []
list_times = []
for i in test_data['id']:
    # Obtener coordenad
    lat_or = test_data.loc[test_data['id'] == i, 'latitud_origen'].values[0]
    lon_or = test_data.loc[test_data['id'] == i, 'longitud_origen'].values[0]
    lat_des = test_data.loc[test_data['id'] == i, 'latitud_destino'].values[0]
    lon_des = test_data.loc[test_data['id'] == i, 'longitud_destino'].values[0]
    # Uso de api
    r = requests.get(
        f"http://router.project-osrm.org/route/v1/car/{lon_or},{lat_or};{lon_des},{lat_des}?overview=false""")
    rts = json.loads(r.content)
    try:
        route = rts.get("routes")[0]
        distancia = route['distance']
        tiempo = route['duration']
        list_dist.append(distancia)
        list_times.append(tiempo)
    except:
        list_dist.append(0)
        list_times.append(0)
print(len(list_dist), len(list_times))

test_data['distancia_api'] = list_dist
test_data['tiempo_api'] = list_times

# %%

test_data.loc[test_data['distancia_api'] == 0]


# %%
test_data.to_csv(out_path + 'test_cleaned.csv')
# %%
