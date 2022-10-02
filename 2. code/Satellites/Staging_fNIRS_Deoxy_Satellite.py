from os import get_exec_path, path
from numpy import False_
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime
import numpy as np




# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14
engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 

connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")
connection.autocommit= True
cur = connection.cursor()



# Please paste the path to your data folder VMData here
PATH ='/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 1/VMData/'

EXTENSION = '.csv' 
GLOB_PATH =glob.glob(PATH + '/*csv') 


def csv_isolator(GLOB_PATH,filter):
    """Returns list of all template types"""
    csv_list =[] 
    for i in range(len(GLOB_PATH)): 
        if (filter in GLOB_PATH[i]):
            csv_list.append(GLOB_PATH[i])
    return csv_list

def csv_converter(csv_list):
    """Extracts filtered csv file, return as list of dataframe object"""
    df_list =[]
    for file in csv_list:
        df = pd.read_csv(file,skiprows=40,index_col=None) 
        df_list.append(df)
    return df_list

def add_nts(df_list):
    """Adds a timestamp and name column for each df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
        df['fNIRS_type']=np.nan
    return df_list

def add_stimuli(df_listv1):
    """Adds stimuli column and populate with appropriate type,returns a list of dataframe objects"""
    index = range(len(df_listv1))
    for i in index[0::4]: #All MOTO probes
        df_listv1[i]['fNIRS_type']='moto'
    for i in index[1::4]: #All rest probes
        df_listv1[i]['fNIRS_type']='rest'
    for i in index[2::4]: #all vimo probes
        df_listv1[i]['fNIRS_type']='vimo'
    for i in index[3::4]: #all viso probes
        df_listv1[i]['fNIRS_type']='viso'
    return df_listv1


deoxy_list =csv_isolator(GLOB_PATH,'Deoxy') 

df_list = csv_converter(deoxy_list)

df_listv1 = add_nts(df_list)

df_listv2 = add_stimuli(df_listv1) 

df_ready =pd.concat(df_listv2) 

ind = []
for i in range(9):
    for n in range(11204):
        ind.append(i+1)

for i in range(100836, 109690):
    ind.append(10)
df_ready['Patient_ID'] = ind

hub_key = []
for i in range(109690):
    key = i+1
    hub_key.append(key)


df_ready['fNIRS_Hub_Key'] = hub_key


df_ready.to_sql('fNIRS_Deoxy_Satellite',con=engine)

