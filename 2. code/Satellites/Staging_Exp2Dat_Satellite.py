from os import get_exec_path, path
from numpy import False_
from pandas.io.parsers import read_csv
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime, time
import numpy as np


"""Connect to sqlalchemy"""
# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14
engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 

connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")

connection.autocommit= True
cur = connection.cursor()

"""Filepath location and specification"""
# Please update the path to the fNIRS-Data containing 1raSessionDR and 2daSessionDR data
PATH = '/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/1raSessionDR/**/*.dat'
PATH2 = '/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/2daSessionDR/**/*.dat'

GLOB_PATH1 =glob.glob(PATH,recursive=True) #list of all .dat files filepaths
GLOB_PATH2 =glob.glob(PATH2,recursive=True) #list of all .dat files filepaths




def dat_converter(dat_list):
    """Returns a list of df"""
    df_list=[]
    for i in range(len(dat_list)):
        df = pd.read_csv(dat_list[i],sep='\n',encoding='latin1', lineterminator='\n')
        df['Patient identifier']=i+1
        df_list.append(df)
    return df_list

df1RA_list =dat_converter(GLOB_PATH1)
df1RA = pd.concat(df1RA_list)
df1RA['Time stamp']=datetime.now()


df2da_list =dat_converter(GLOB_PATH2) 
df2da = pd.concat(df2da_list)
df2da['Time stamp']=datetime.now()

hub_key = []
for i in range(219380, 297778):
    key = i+1
    hub_key.append(key)



df1RA['fNIRS_Hub_Key'] = hub_key

hub_key2 = []
for i in range(297778, 361527):
    key = i+1
    hub_key2.append(key)

df2da['fNIRS_Hub_Key'] = hub_key2


df2da.to_sql('fNIRS_Exp2Sess2Dat_Satellite',con=engine) 
df1RA.to_sql('fNIRS_Exp2Sess1Dat_Satellite',con=engine) 