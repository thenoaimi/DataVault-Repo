from os import get_exec_path, path
from numpy import False_
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime, time
import numpy as np




# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14
engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 

connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")
#remember to edit argument in psycopg2.connect() to YOUR database
#This is the different paths of the two files
connection.autocommit= True
cur = connection.cursor()

# Please paste the path to your data folder VMData here
PATH ='/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 1/VMData' 


EXTENSION = '.csv' 
GLOB_PATH =glob.glob(PATH + '/*csv') 


def csv_isolator(GLOB_PATH,filter):
    """Returns list of all template types"""
    csv_list =[] 
    for i in range(len(GLOB_PATH)): 
        if (filter in GLOB_PATH[i]):
            csv_list.append(GLOB_PATH[i])
    return csv_list

def meta_converter(csv_list):
    """Returns a list of df"""
    meta_list=[]
    index = range(len(csv_list))
    for i in index:
        df = pd.read_csv(csv_list[i],header=None,sep='\n',nrows=31)
        df = df[0].str.split(',', expand=True)
        meta_list.append(df.T)
    return meta_list


def add_ts(df_list):
    """Adds a timestamp and name column for each df, returns list of df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
    return df_list

def add_patientid(df_list):
    """Adds patient ID column and fills it for each patient's file, returns a list of df"""
    index = range(len(df_list))
    for i in index[0:4:1]:
        df_list[i]['patient_id']=1
    for i in index[4:8:1]:
        df_list[i]['patient_id']=2
    for i in index[8:12:1]:
        df_list[i]['patient_id']=3
    for i in index[12:16:1]:
        df_list[i]['patient_id']=4
    for i in index[16:20:1]:
        df_list[i]['patient_id']=5
    for i in index[20:24:1]:
        df_list[i]['patient_id']=6
    for i in index[24:28:1]:
        df_list[i]['patient_id']=7
    for i in index[28:32:1]:
        df_list[i]['patient_id']=8
    for i in index[32:36:1]:
        df_list[i]['patient_id']=9
    for i in index[36:40:1]:
        df_list[i]['patient_id']=10
    return df_list


csv_list = csv_isolator(GLOB_PATH,'MES_Probe1.csv')
metadf_list =meta_converter(csv_list)
metadf_listv1 = add_ts(metadf_list)
metadf_listv2 = add_patientid(metadf_listv1)
metadf_ready = pd.concat(metadf_listv2)


names = np.array(metadf_ready.iloc[0,:])
for i in range(len(names)):
    metadf_ready = metadf_ready.rename(columns={i:names[i]})
metadf_ready = metadf_ready.drop([0])

ind = []
for i in range(1920):
    ind.append(i)
metadf_ready['index'] = ind

hub_key = []
for i in range(1920):
    key = i+1
    hub_key.append(key)
metadf_ready['Experiment_Hub_Key'] = hub_key


metadf_ready.to_sql('Exp1_Metadata_Satellite',con=engine)

