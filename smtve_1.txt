import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
import numpy as np
import time


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

# LIST OF LENGHTS TO COMPARE DUPLICATES

# list_of_len = [len(ae15_obj), len(ae19_obj), len(ae20_obj)]

# DELETING DUPLICATES

ae15_obj = ae15_obj.drop_duplicates(subset='date_time')
ae19_obj = ae19_obj.drop_duplicates(subset='date_time')
ae20_obj = ae20_obj.drop_duplicates(subset='date_time')

#NEW LIST OF LENGHTS TO COMPARE DUPLICATES
#new_len = [len(ae15_obj), len(ae19_obj), len(ae20_obj)]

# print(list_of_len)
# print(new_len)

plt_x = ae15_obj['date_time']
plt_y = ae15_obj['power']

# time series sctterplot https://stackoverflow.com/questions/43459786/plot-timeseries-scatterplot

plt.scatter(plt_x, plt_y)
plt.show


