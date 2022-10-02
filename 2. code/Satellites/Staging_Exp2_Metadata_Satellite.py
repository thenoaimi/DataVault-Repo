from os import get_exec_path, path
from numpy import False_
from pandas.io.parsers import read_csv
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
connection.autocommit= True
cur = connection.cursor()



# Please update the paths to the fNIRS-Data containing 1raSessionDR and 2daSessionDR data
PATH = '/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/1raSessionDR/**/*.txt'
PATH2 = '/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/2daSessionDR/**/*.txt'


GLOB_PATH =glob.glob(PATH,recursive=True) #list of all .dat files filepaths
GLOB_PATH2 =glob.glob(PATH2,recursive=True) #list of all .dat files filepaths


def meta_converter(txt_list):
    """Returns a list of df"""
    metadf_list=[]
    index = range(len(txt_list))
    for i in index:
        df = pd.read_csv(txt_list[i],sep='\n',encoding='latin1')
        metadf_list.append(df.T)
    return metadf_list


def add_ts1(df_list):
    """Adds a timestamp and name column for each df, returns list of df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
        df['SessionDR_Type']='1raSessionDR'
    return df_list

def add_ts2(df_list):
    """Adds a timestamp and name column for each df, returns list of df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
        df['SessionDR_Type']='2daSessionDR'
    return df_list


text_list_1RA = GLOB_PATH
metadf_list_1RA = meta_converter(text_list_1RA)
metadf_list_1RAV1 = add_ts1(metadf_list_1RA)
metafinrs1RA_ready = pd.concat(metadf_list_1RAV1)



text_list_2DA =GLOB_PATH2
metadf_list_2DA = meta_converter(text_list_2DA)
metadf_list_2DAV1 = add_ts2(metadf_list_2DA)
metafinrs2DA_ready =pd.concat(metadf_list_2DAV1)
Final_list =[metafinrs1RA_ready,metafinrs2DA_ready]

metafinrs_ready =pd.concat(Final_list)


metafinrs_ready = metafinrs_ready.rename(columns={0:'Subject', 1:'SamplingRate', 2:'waveLength_N', 3:'Wavelengths', 4:'source_N', 5:'detector_N', 6:'time_point_N',
                    7:'source_detector_key', 8:'Source_Detector_Key_Pt2', 9:'probeInfo_file'})


ind = []
for i in range(10, 110):
    ind.append(i)

hub_key = []
for i in range(7680, 7772):
    key = i+1
    hub_key.append(key)
print('min: ', min(hub_key), 'max: ', max(hub_key))


metafinrs_ready['Experiment_Hub_Key'] = hub_key


metafinrs_ready.drop('Source: Main84_TdXp_Laptop.vi<append>',axis=0,inplace=True)
metafinrs_ready.drop('Nombre de imagen               PID Nombre de sesi¢n N£m. de ses Uso de memor',axis=0,inplace=True)
metafinrs_ready.drop('Nombre de host:                            INTELIMED-PC',axis=0,inplace=True)


metafinrs_ready.to_sql('Exp2_Metadata_Satellite',con=engine)

