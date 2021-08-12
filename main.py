# %% 0. Librerías
import pandas as pd 
import numpy as np 
from geopy.geocorders import Nominatim

# %% Datos
in_path = 'data/in/'
out_path = 'data/out/'

filename = 'train.csv'
df = pd.read_csv(in_path + filename)

# %% 
geolocator = Nominatim(user_agent='scrapping_location')
