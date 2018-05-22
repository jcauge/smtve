import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import stats
import collections as cl

######################################
########  Start of the code ##########
######################################

start_time = time.time()

####### Opening of the files  #########
ae15_path = "C:\\Users\\jca02\\Documents\\Prueba smartive\\pfc_tra\\ae15.csv"
ae19_path = "C:\\Users\\jca02\\Documents\\Prueba smartive\\pfc_tra\\ae19.csv"
ae20_path = "C:\\Users\\jca02\\Documents\\Prueba smartive\\pfc_tra\\ae20.csv"

ae15 = pd.read_csv(filepath_or_buffer= ae15_path, header = 0)
ae19 = pd.read_csv(filepath_or_buffer= ae19_path, header = 0)
ae20 = pd.read_csv(filepath_or_buffer= ae20_path, header = 0)

# Subseting the most important parameters
ae15_obj = ae15[['date_time', 'power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]
ae19_obj = ae19[['date_time', 'power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]
ae20_obj = ae20[['date_time', 'power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]

# DELETING DUPLICATES
ae15_obj = ae15_obj.drop_duplicates(subset='date_time')
ae19_obj = ae19_obj.drop_duplicates(subset='date_time')
ae20_obj = ae20_obj.drop_duplicates(subset='date_time')

ae15_obj = ae15[['power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]
ae19_obj = ae19[['power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]
ae20_obj = ae20[['power', 'bearing_temp', 'gen_1_speed', 'gen_bearing_temp', 'temp_oil_mult', 'temp_out_nacelle']]


# Deleting Outliers - Rows with any 0
ae15_obj = ae15_obj[~(ae15_obj == 0).any(axis=1)]
ae19_obj = ae19_obj[~(ae19_obj == 0).any(axis=1)]
ae20_obj = ae20_obj[~(ae20_obj == 0).any(axis=1)]

# Deleting outliers - NaN values
ae15_obj = ae15_obj.dropna(axis = 0)
ae19_obj = ae19_obj.dropna(axis = 0)
ae20_obj = ae20_obj.dropna(axis = 0)

# Deleting outliers using the FSCORE method

ae15_obj = ae15_obj[(np.abs(stats.zscore(ae15_obj)) < 3).all(axis=1)]



########################################
 # Descriptive analysis starts here  #
########################################

# Max, min and range of values
min15 = ae15_obj.min()
min19 = ae19_obj.min()
min20 = ae20_obj.min()

max15 = ae15_obj.max()
max19 = ae19_obj.max()
max20 = ae20_obj.max()

rg15 = max15 - min15
rg19 = max19 - min19
rg20 = max20 - min20

# mean and sd
mean15 = np.mean(ae15_obj, axis = 0)
mean19 = np.mean(ae19_obj, axis = 0)
mean20 = np.mean(ae20_obj, axis = 0)

std15 = np.std(ae15_obj, axis = 0)
std19 = np.std(ae19_obj, axis = 0)
std20 = np.std(ae20_obj, axis = 0)

cnt15 = cl.Counter(ae15_obj['bearing_temp'])
cnt15_mc = cnt15.most_common()
cnt15_mc.sort()

unicos15 = [item[0] for item in cnt15_mc]
frec15 = [item[1] for item in cnt15_mc]


# plt.hist(ae15_obj['bearing_temp'], bins = len(unicos15), color='tan')
# plt.bar(unicos15, frec15, color ='tan')
# plt.show
